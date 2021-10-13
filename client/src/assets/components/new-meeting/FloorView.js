import React from "react";
import { AiOutlineClose } from 'react-icons/ai';

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floorplan: '',
            currentFloor: '',
            viewbox: ''
        }
    }

    componentDidMount(){
        this.getFloor()
    }

    componentDidUpdate(prevProps){
        if (this.props.selectedFloor != prevProps.selectedFloor && this.props.selectedFloor['id'] != ""){
            console.log(this.props.selectedFloor['name'])
            this.getFloor()
            this.forceUpdate()
        }
    }

    async getFloor(){
        this.setState({
            currentFloor: this.props.selectedFloor['name']
        })

        console.log(this.props.selectedFloor['name'])

        fetch('/floor/' + this.props.selectedFloor['id'])
        .then(res => res.json())
        .then(res => this.setState({
            floorplan: res['floors'],
            viewbox: res['viewbox']
        }))
        .then(console.log(this.state.floorplan))

        // console.log(this.state.floorplan)

    }

    render(){
        return(
            <div className="left-panel building-view floor-view">
                <div className="row title">
                    <h1 style={{"margin-left":"1em"}}></h1>
                    <h1>{this.props.selectedBuilding}</h1>
                    <h1 onClick={() => this.props.setFloor("","")} style={{"cursor":"pointer"}}><AiOutlineClose /></h1>
                </div>
                <div>
                    <svg
                        style={{'width': '100%'}}
                        xmlns="http://www.w3.org/2000/svg"
                        id="Layer_1"
                        data-name="Layer 1"
                        viewBox={this.state.viewbox != '' ? this.state.viewbox : ''}
                    >
                        {this.state.floorplan != "" && this.state.floorplan.length > 0 && this.state.floorplan.map((entry) => 
                            entry['type'] == 'rect' ?
                            <rect 
                            x={entry["x"]}
                            y={entry["y"]}
                            width={entry["width"]}
                            height={entry["height"]}
                            fill={entry["fill"]}
                            stroke={entry["stroke"]}
                            className={entry["className"]}
                                /> :
                            <div></div>
                        )}
                    </svg>

                </div>
                <h2 onClick={() => console.log(this.state.floorplan)}>{this.state.currentFloor}</h2>
            </div>
        );
    }
}