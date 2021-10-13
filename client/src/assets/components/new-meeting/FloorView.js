import React from "react";
import { AiOutlineClose } from 'react-icons/ai';
import { IoPersonRemoveOutline } from "react-icons/io5";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floorplan: '',
            selectedRoom: '',
            viewbox: ''
        }

        this.selectRoom = this.selectRoom.bind(this)
    }

    componentDidMount(){
        this.getFloor()
    }

    componentDidUpdate(prevProps){
        if (this.props.selectedFloor != prevProps.selectedFloor && this.props.selectedFloor['id'] != ""){
            this.getFloor()
            this.forceUpdate()
        }

        if (this.props.room != prevProps.selectedRoom && this.props.room['name'] == ''){
            const prevId = this.state.selectedRoom
            const prevEl = document.getElementById(prevId)
            if ( prevEl && prevEl.classList.contains("selected")){
                prevEl.classList.remove("selected")
            }
        }
    }

    selectRoom(id, room){
        const prevId = this.state.selectedRoom
        const prevEl = document.getElementById(prevId)
        if ( prevEl && prevEl.classList.contains("selected")){
            prevEl.classList.remove("selected")
        }

        const newEl = document.getElementById(id)
        if ( newEl ){
            newEl.classList.add("selected")
        }

        this.setState({
            selectedRoom: id
        })

        this.props.setRoom(id, room)
    }

    async getFloor(){
        this.setState({
            currentFloor: this.props.selectedFloor['name']
        })

        fetch('/buildings/get/' + this.props.selectedBuilding["id"] + "/" + this.props.selectedFloor['id'])
        .then(res => res.json())
        .then(res => this.setState({
            floorplan: res['floor_data']['room'],
            viewbox: res['floor_data']['viewbox']
        }))
    }

    render(){
        return(
            <div className="left-panel building-view floor-view">
                <div className="row title">
                    <h1 style={{"marginLeft":"1em"}}></h1>
                    <h1>{this.props.selectedBuilding["name"]}</h1>
                    <h1 onClick={() => this.props.setFloor("","")} style={{"cursor":"pointer"}}><AiOutlineClose /></h1>
                </div>
                <div>
                    <svg
                        style={{'width': '100%', 'border': '1px solid white'}}
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
                                id={entry["room_id"]}
                                onClick={() => this.selectRoom(entry["room_id"], entry["room_name"])}
                                /> :
                            <div></div>
                        )}
                    </svg>

                </div>
                <h2>{this.state.currentFloor}</h2>
            </div>
        );
    }
}