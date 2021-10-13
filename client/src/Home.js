import React from "react";
import NewMeeting from './pages/NewMeeting'

export default class Home extends React.Component{
    render(){
        return(
            <div className="container">
                <NewMeeting />
            </div>
        );
    }
}