import React from "react";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            selected: 0
        }

        this.selectFloor = this.selectFloor.bind(this);
        this.hoverFloor = this.hoverFloor.bind(this);
    }

    componentDidMount(){
        this.selectFloor(0);
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
                <h1>{this.props.selectedBuilding}</h1>
                <div className="floor-display">
                    {Object.entries(this.props.floors).map(([key, value]) => 
                        <div className="floor" id={"floor-"+key} onClick={() => this.selectFloor(key, value)} onMouseOver={() => this.hoverFloor(value)} onMouseOut={() => this.hoverFloor("")}></div>
                    )}
                </div>
                <h2 id="floor-name">
                </h2>
            </div>
        );
    }
}