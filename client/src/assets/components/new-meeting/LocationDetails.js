import React from "react";
import { FaWheelchair } from "react-icons/fa";
import { AiFillSound } from "react-icons/ai";
import { ImDisplay } from "react-icons/im";
import { BsCameraVideo } from "react-icons/bs"

export default class LocationDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            buildings: '',
            floorList: this.props.floorList,
        }

        this.setBuilding = this.setBuilding.bind(this);
        this.setFloor = this.setFloor.bind(this);
        this.clearFilter = this.clearFilter.bind(this);  
        this.getBuildings = this.getBuildings.bind(this);
    }

    componentDidMount(){
        this.getBuildings()
    }

    clearFilter(){
        this.props.setBuilding('', '')
        this.props.setFloor('', '')
        this.props.setRoom('', '')
        this.props.setRooms([])
        this.forceUpdate()
    }

    async getBuildings(){
        fetch('/buildings/get')
        .then(res => res.json())
        .then(res => this.setState({
            buildings: res
        }))
    }

    setBuilding(building){
        const element = document.getElementById("select-building")
        const bid = element.options[element.selectedIndex].id

        this.props.setBuilding(bid, building)
    }

    setFloor(floor){
        const element = document.getElementById("select-floor")
        const fid = element.options[element.selectedIndex].id

        this.props.setFloor(fid, floor)
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
                    <select id="select-building" onChange={(e) => this.setBuilding(e.target.value)}>
                        <option disabled selected={this.props.building['name'] == ""} value> Select a building </option>
                        {this.state.buildings != "" && Object.entries(this.state.buildings).map(([key, value]) =>
                        <option id={value["building_id"]}>{value["name"]}</option>)}
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
                            <select id="select-floor" disabled={this.props.building == ""} onChange={(e) => this.setFloor(e.target.value)}>
                                <option disabled selected value> Select a floor </option>
                                {this.props.building["name"] != "" && Object.entries(this.props.floors).map(([key, value]) => 
                                    <option id={value["floor_id"]} value={value["floor_id"]}>{value["floor_id"]}</option>
                                )}
                            </select>
                        </div>
                    </div>
                    <div className="row">Features</div>
                    <select disabled>
                        <option disabled selected value> No features available </option>
                    </select>
                    {this.props.room['name'] == '' && 
                    <div className="room-list">
                        {this.props.roomList.length > 0 && this.props.roomList.map((value) => 
                        <div onClick={() => this.props.setFloor(value["room_id"], value["room_name"])}>
                            {value["room_name"]}
                        </div>)}
                    </div>}
                    
                    {this.props.room['name'] != '' && 
                    <div className="room-details">
                        <h2>{this.props.room['name']}</h2>
                        <div><FaWheelchair /> Accessibility </div>
                        <div><AiFillSound /> Sound </div>
                        <div><ImDisplay /> Display </div>
                        <div><BsCameraVideo /> Video </div>
                        <div className="button">Book Room</div>
                        <div className="button" onClick={() => this.props.setRoom("", "")}>Cancel</div>
                    </div>}
                </div>
            </div>
        );
    }
}