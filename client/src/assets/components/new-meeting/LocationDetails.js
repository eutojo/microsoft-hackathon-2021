import React from "react";

export default class LocationDetails extends React.Component {
    constructor(props){
        super(props);

        this.setBuilding = this.setBuilding.bind(this);        
    }

    setBuilding(e){
        this.props.setBuilding(e.target.value);
    }
    render(){
        return(
            <div className="right-panel">
                <div className="tab">
                    <div>Room</div>
                    <div>Schedule</div>
                </div>
                <div className="content">
                    Building
                    <select onChange={(e) => this.setBuilding(e)}>
                        <option disabled selected value> -- select an option -- </option>
                        <option name="foundry">Foundry</option>
                        <option name="axle">Axle</option>
                    </select>
                </div>
            </div>
        );
    }
}