import React from "react";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floors: {
                0: 'ground floor',
                1: 'first floor',
                2: 'second floor',
                3: 'third floor'
            },
            selected: 0
        }

        this.selectFloor = this.selectFloor.bind(this);
    }

    componentDidMount(){
        console.log(this.state.floors)
        this.selectFloor(0);
    }

    selectFloor(floor){
        this.setState({
            'selected':floor,
        })
        this.forceUpdate()
    }

    render(){
        return(
            <div className="left-panel building-view">
                {this.props.selectedBuilding}
                <div className="floor-display">
                    {Object.entries(this.state.floors).map(([key, value]) => 
                        <div className={`floor ${this.state.selected == key ? "selected" : ""}`} id={"floor-"+key} onClick={() => this.selectFloor(key)}></div>
                    )}
                </div>
                <div>
                    {this.state.floors[this.state.selected]}
                </div>
            </div>
        );
    }
}