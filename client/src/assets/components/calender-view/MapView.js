import React from "react";

export default class MapDetails extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            rooms: [],
            viewbox: '',
        }

        this.getRooms = this.getRooms.bind(this)
        this.getInstructions = this.getInstructions.bind(this)
        this.calculate = this.calculate.bind(this)
    }

    componentDidMount(){
        this.getRooms()
        this.getInstructions()
    }

    async getRooms(){
        fetch("/buildings/get/FDY/FDY-L0")
        .then(res => res.json())
        .then(res => this.setState({
            rooms: res['floor_data']['room'],
            viewbox: res['floor_data']['viewbox']
        }))
    }

    async getInstructions(){
        if(this.props.instructions.length == 0){
            fetch("/instructions/")
            .then(res => res.json())
            .then(res => this.props.setInstructions(res))
        }
    }

    calculate(start, end){
        if((end-start) == 0){
            return 5
        }
        return Math.abs(end-start)
    }

    render(){
        return(
            <div className="mobile-map">
                <div className="svg-container">
                    <svg
                            style={{'width': '100%', 'border': '1px solid white'}}
                            xmlns="http://www.w3.org/2000/svg"
                            id="Layer_1"
                            data-name="Layer 1"
                            viewBox={this.state.viewbox != '' ? this.state.viewbox : ''}
                        >
                        {this.state.rooms.length > 0 && this.state.rooms.map((entry) => 
                            entry['type'] == 'rect' ?
                            <rect 
                                x={entry["x"]}
                                y={entry["y"]}
                                width={entry["width"]}
                                height={entry["height"]}
                                fill={entry["fill"]}
                                stroke={entry["stroke"]}
                                className={`navigate ${entry["className"]}`}
                                id={entry["room_id"]}
                                /> :
                            <div></div>
                        )}
                        {this.props.instructions.length > 0 && this.props.instructions.map((entry) => 
                            !((entry["draw_start_x"] == entry["draw_end_x"]) && (entry["draw_start_y"] == entry["draw_end_y"])) && <rect 
                                x={entry["draw_start_x"]}
                                y={entry["draw_start_y"]}
                                width={this.calculate(entry["draw_start_x"], entry["draw_end_x"])}
                                height={this.calculate(entry["draw_start_y"], entry["draw_end_y"])}
                                fill="yellow"
                                stroke="#000000"
                            />
                        )}
                    </svg>
                </div>
            </div>    
        )
    }
}