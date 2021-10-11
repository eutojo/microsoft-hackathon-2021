import React from "react";
import MeetingDetails from "../assets/components/new-meeting/MeetingDetails"
import LocationDetails from "../assets/components/new-meeting/LocationDetails"
import BuildingView from "../assets/components/new-meeting/BuildingView"

export default class NewMeeting extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'building': '',
            'floor': ''
        }

        this.setBuilding = this.setBuilding.bind(this);
    }

    setBuilding(building){
        console.log(building);
        this.setState({
            'building': building
        })
    }

    render(){
        return(
            <div className="window-container">
                <div className="tab">
                    <div>Busy</div>
                    <div>Mark as Private</div>
                    <div>Attendee Options</div>
                    <div>Scheduling Assistant</div>
                    <div>Attach</div>
                    <div>...</div>
                </div>
                <div className="content-container">
                    {this.state.building != '' &&
                        <BuildingView selectedBuilding={this.state.building}/>
                    }
                    {this.state.building == '' &&
                        <MeetingDetails />
                    }
                    <LocationDetails setBuilding={this.setBuilding}/>
                </div>
            </div>
        );
    }
}