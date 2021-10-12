import React from "react";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            selected: 0
        }

        this.selectFloor = this.selectFloor.bind(this);
    }

    componentDidMount(){
        this.selectFloor(0);
    }

    selectFloor(floor){
        console.log(floor)
        this.props.setFloor(floor)
        this.forceUpdate()
    }

    render(){
        return(
            <div className="left-panel building-view">
                {this.props.selectedBuilding}
                <div className="floor-display">
                    {Object.entries(this.props.floors).map(([key, value]) => 
                        <div className={`floor ${this.props.selectedFloor == key ? "selected" : ""}`} id={"floor-"+key} onClick={() => this.selectFloor(key)}></div>
                    )}
                </div>
                <div>
                    {this.props.floors[this.props.selectedFloor]}
                </div>
            </div>
        );
    }
}