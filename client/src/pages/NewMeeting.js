import React from "react";
import MeetingDetails from "../assets/components/new-meeting/MeetingDetails"
import LocationDetails from "../assets/components/new-meeting/LocationDetails"
import BuildingView from "../assets/components/new-meeting/BuildingView"
import FloorView from "../assets/components/new-meeting/FloorView"

import { FaCircle } from 'react-icons/fa';
import { RiUserSettingsLine, RiCalendarLine } from 'react-icons/ri';
import { MdLockOutline } from 'react-icons/md';
import { ImAttachment } from 'react-icons/im';
import { BsThreeDots } from 'react-icons/bs';

export default class NewMeeting extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'building': {
                'id': '',
                'name': ''
            },
            'selectedFloor': {
                'id': '',
                'name': ''
            },
            'floors': {}
        }

        this.setBuilding = this.setBuilding.bind(this);
        this.setFloor = this.setFloor.bind(this);
        this.setFloors = this.setFloors.bind(this);
    }

    setBuilding(bid, building){
        this.setState({
            'building': {
                'id': bid,
                'name': building
            }
        })
    }

    setFloors(floors){
        this.setState({
            'floors': floors
        })
    }

    setFloor(id, floor){
        this.setState({
            'selectedFloor': {
                'id': id,
                'name': floor
            }
        })
    }

    render(){
        return(
            <div className="window-container">
                <div className="tab">
                    <div><FaCircle className="busy" /> Busy</div>
                    <div><MdLockOutline /> Mark as Private</div>
                    <div><RiUserSettingsLine /> Attendee Options</div>
                    <div><RiCalendarLine /> Scheduling Assistant</div>
                    <div><ImAttachment /> Attach</div>
                    <div><BsThreeDots/></div>
                </div>
                <div className="content-container">
                    {this.state.building['name'] != '' && this.state.selectedFloor['id'] ==  "" &&
                        <BuildingView
                            selectedBuilding={this.state.building}
                            setFloors={this.setFloors}
                            setFloor={this.setFloor}
                            floors={this.state.floors}
                            selectedFloor={this.state.selectedFloor}/>
                    }
                    {this.state.building['name'] != '' && this.state.selectedFloor['id'] != "" &&
                        <FloorView
                            selectedBuilding={this.state.building}
                            selectedFloor={this.state.selectedFloor}
                            setFloor={this.setFloor}
                            />
                    }
                    {this.state.building['name'] == '' &&
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