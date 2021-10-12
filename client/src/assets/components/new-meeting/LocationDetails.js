import React from "react";

export default class LocationDetails extends React.Component {
    constructor(props){
        super(props);

        this.clearFilter = this.clearFilter.bind(this);  
    }

    clearFilter(){
        this.props.setBuilding("")
        this.props.setFloor("","")
        this.forceUpdate()
    }

    render(){
        return(
            <div className="right-panel">
                <div className="tab">
                    <div className="selected">Room Finder</div>
                    <div>Scheduler</div>
                </div>
                <div className="content">
                    <div className="row">
                        <div>Building</div>
                        <div onClick={() => this.clearFilter()} >Clear Filters</div>
                    </div>
                    <select onChange={(e) => this.props.setBuilding(e.target.value)}>
                        <option disabled selected={this.props.building == ""} value> Select a building </option>
                        <option name="foundry">Foundry</option>
                        <option name="axle">Axle</option>
                    </select>
                    <div className="row double">
                        <div>
                            <div>Capacity</div>
                            <select disabled>
                                <option disabled selected value> Any </option>
                            </select>
                        </div>
                        <div>
                            <div>Floor</div>
                            <select disabled={this.props.building == ""} onChange={(e) => this.props.setFloor(e.target.key, e.target.value)}>
                                <option disabled selected value> Select a floor </option>
                                {this.props.building != "" && Object.entries(this.props.floors).map(([key, value]) => 
                                    <option id={key} value={value}>{value}</option>
                                )}
                            </select>
                        </div>
                    </div>
                    <div className="row">Features</div>
                    <select disabled>
                        <option disabled selected value> No features available </option>
                    </select>
                </div>
            </div>
        );
    }
}