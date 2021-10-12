import React from "react";
import MeetingDetails from "../assets/components/new-meeting/MeetingDetails"
import LocationDetails from "../assets/components/new-meeting/LocationDetails"
import BuildingView from "../assets/components/new-meeting/BuildingView"
import FloorView from "../assets/components/new-meeting/FloorView"

import { FaCircle } from 'react-icons/fa';
import { RiUserSettingsLine, RiCalendarLine } from 'react-icons/ri';
import { MdLockOutline, MdSystemSecurityUpdate } from 'react-icons/md';
import { ImAttachment } from 'react-icons/im';
import { BsThreeDots } from 'react-icons/bs';

export default class NewMeeting extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'building': '',
            'selectedFloor': '',
            'floors': {
                0: 'ground floor',
                1: 'first floor',
                2: 'second floor',
                3: 'third floor'
            }
        }

        this.setBuilding = this.setBuilding.bind(this);
        this.setFloor = this.setFloor.bind(this);
        this.setFloors = this.setFloors.bind(this);
    }

    componentDidUpdate(){
        console.log(this.state.selectedFloor)
    }

    setBuilding(building){
        this.setState({
            'building': building
        })
    }

    setFloors(floors){
        this.setState({
            'floors': floors
        })
    }

    setFloor(floor){
        this.setState({
            'selectedFloor': floor
        })
    }

    render(){
        return(
            <div className="window-container">
                <div className="tab">
                    <div><FaCircle /> Busy</div>
                    <div><MdLockOutline /> Mark as Private</div>
                    <div><RiUserSettingsLine /> Attendee Options</div>
                    <div><RiCalendarLine /> Scheduling Assistant</div>
                    <div><ImAttachment /> Attach</div>
                    <div><BsThreeDots/></div>
                </div>
                <div className="content-container">
                    {this.state.building != '' && this.state.selectedFloor == '' &&
                        <BuildingView
                            selectedBuilding={this.state.building}
                            setFloor={this.setFloor}
                            floors={this.state.floors}
                            selectedFloor={this.state.selectedFloor}/>
                    }
                    {this.state.building != '' && this.state.selectedFloor != '' &&
                        <FloorView
                            selectedBuilding={this.state.building}
                            selectedFloor={this.state.selectedFloor}/>
                    }
                    {this.state.building == '' &&
                        <MeetingDetails />
                    }
                    <LocationDetails 
                        setBuilding={this.setBuilding}
                        setFloor={this.setFloor}
                        building={this.state.building}
                        selectedFloor={this.state.selectedFloor}
                        floors={this.state.floors}
                        />
                </div>
            </div>
        );
    }
}