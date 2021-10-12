import React from "react";

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floorplan: ''
        }
    }

    componentDidMount(){
        this.getFloor()
    }

    async getFloor(){
        fetch('/floor/' + this.props.selectedFloor)
        .then(res => res.json())
        .then(res => this.setState({
            floorplan: res
        }))

    }

    render(){
        return(
            <div className="left-panel building-view floor-view">
                {this.props.selectedBuilding}
                <div>
                    {this.props.floorplan != "" && Object.entries(this.state.floorplan).map(([floor, value]) => 
                        <div className="plan row">
                            {value.map((points) => <div className={`plan column ${points.includes(255) ? `color` : `no-color`}`} > </div>)}
                        </div>
                    )}
                </div>
                {this.props.selectedFloor}
            </div>
        );
    }
}