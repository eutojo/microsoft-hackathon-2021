import React from "react";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            selected: 0,
            current_building: ''
        }

        this.loadBuilding = this.loadBuilding.bind(this);
        this.selectFloor = this.selectFloor.bind(this);
        this.hoverFloor = this.hoverFloor.bind(this);
    }

    componentDidMount(){
        this.loadBuilding()
    }

    async loadBuilding(){
        fetch("/buildings/get/" + this.props.selectedBuilding['id'])
        .then(res => res.json())
        .then(res => this.props.setFloors(res['floors']))
    }

    hoverFloor(floor){
        const element = document.getElementById("floor-name")
        element.innerHTML = floor;
    }

    selectFloor(id, floor){
        this.hoverFloor("")
        this.props.setFloor(id, floor)
        this.forceUpdate()
    }

    render(){
        return(
            <div className="left-panel building-view">
                <h1>{this.props.selectedBuilding['name']}</h1>
                <div className="floor-display">
                    {Object.entries(this.props.floors).map(([key, value]) => 
                        <div className="floor" id={"floor-"+value["floor_id"]} onClick={() => this.selectFloor(value["floor_id"], value["floor_name"])} onMouseOver={() => this.hoverFloor(value["floor_name"])} onMouseOut={() => this.hoverFloor("")}></div>
                    )}
                </div>
                <h2 id="floor-name">
                </h2>
            </div>
        );
    }
}