import React from "react";
import { IoLocationOutline,  IoPersonOutline} from 'react-icons/io5';
import { GoQuote } from 'react-icons/go';
import { BiTime } from 'react-icons/bi';
import { FiRepeat, FiBell} from 'react-icons/fi';

export default class MeetingDetails extends React.Component {
    render(){
        return(
            <div className="left-panel meeting-details">
                <div className="entry">
                    <div><GoQuote /><div>New Event</div></div>
                </div>
                <div className="entry">
                    <div><IoPersonOutline /><div>Add Required People</div></div>
                </div>
                <div className="entry">
                    <div><BiTime/><div>Time</div></div>
                </div>
                <div className="entry">
                    <div><FiRepeat /><div>Repeat</div></div>
                </div>
                <div className="entry">
                    <div><IoLocationOutline/><div>Location</div></div>
                </div>
                <div className="entry">
                    <div><FiBell /><div>Reminder</div></div>
                </div>
            </div>
        );
    }
}