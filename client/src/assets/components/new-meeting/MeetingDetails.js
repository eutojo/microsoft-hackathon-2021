import React from "react";
import { IoLocationOutline } from 'react-icons/io5';

export default class MeetingDetails extends React.Component {
    render(){
        return(
            <div className="left-panel">
                <div>
                    <div>New Event</div>
                </div>
                <div>
                    <div>Add Required People</div>
                </div>
                <div>
                    <div>Time</div>
                </div>
                <div>
                    <div>Repeat</div>
                </div>
                <div>
                    <div><IoLocationOutline/> Location</div>
                </div>
                <div>
                    <div>Reminder</div>
                </div>
            </div>
        );
    }
}