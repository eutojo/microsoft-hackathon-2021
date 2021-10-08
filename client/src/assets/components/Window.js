import React from "react";

export default class Window extends React.Component {
    render(){
        return(
            <div className="window-container">
                <div className="toolbar">
                    <div>Busy</div>
                    <div>Mark as Private</div>
                    <div>Attendee Options</div>
                    <div>Scheduling Assistant</div>
                    <div>Attach</div>
                    <div>...</div>
                </div>
                <div className="content-container">
                    <div className="left-pane"></div>
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
                            <div>Location</div>
                        </div>
                        <div>
                            <div>Reminder</div>
                        </div>
                    <div className="right-pane"></div>
                </div>
            </div>
        );
    }
}