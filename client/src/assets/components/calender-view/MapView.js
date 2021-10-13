import React from "react";

export default class MapDetails extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            rooms: [],
            viewbox: ''
        }

        this.getRooms = this.getRooms.bind(this)
    }

    componentDidMount(){
        this.getRooms()
    }

    async getRooms(){
        fetch("/buildings/get/FDY/FDY-L1")
        .then(res => res.json())
        .then(res => this.setState({
            rooms: res['floor_data']['room'],
            viewbox: res['floor_data']['viewbox']
        }))
    }

    render(){
        return(
            <div className="mobile-map">
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
                    </svg>
            </div>    
        )
    }
}