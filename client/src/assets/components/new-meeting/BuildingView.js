import React from "react";

export default class MeetingDetails extends React.Component {
    render(){
        return(
            <div className="left-panel">
                {this.props.selectedBuilding}
            </div>
        );
    }
}