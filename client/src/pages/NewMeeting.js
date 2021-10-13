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
            'selectedRoom':{
                'id': '',
                'name': ''
            },
            'floors': {},
            'roomList': []
        }

        this.setBuilding = this.setBuilding.bind(this);
        this.setFloor = this.setFloor.bind(this);
        this.setFloors = this.setFloors.bind(this);
        this.setRoom = this.setRoom.bind(this);
        this.setRoomList = this.setRoomList.bind(this);
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

    setRoom(id, room){
        this.setState({
            'selectedRoom': {
                'id': id,
                'name': room
            }
        })
    }

    setRoomList(list){
        this.setState({
            roomList: list
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
                            setRooms={this.setRoomList}
                            setRoom={this.setRoom}
                            floors={this.state.floors}
                            selectedFloor={this.state.selectedFloor}/>
                    }
                    {this.state.building['name'] != '' && this.state.selectedFloor['id'] != "" &&
                        <FloorView
                            selectedBuilding={this.state.building}
                            setFloors={this.setFloors}
                            setRooms={this.setRoomList}
                            selectedFloor={this.state.selectedFloor}
                            room={this.state.selectedRoom}
                            setFloor={this.setFloor}
                            setRoom={this.setRoom}
                            />
                    }
                    {this.state.building['name'] == '' &&
                        <MeetingDetails />
                    }
                    <LocationDetails 
                        setBuilding={this.setBuilding}
                        setFloor={this.setFloor}
                        setRoom={this.setRoom}
                        setRooms={this.setRoomList}
                        building={this.state.building}
                        floor={this.state.selectedFloor}
                        floors={this.state.floors}
                        room={this.state.selectedRoom}
                        roomList={this.state.roomList}
                        />
                </div>
            </div>
        );
    }
}