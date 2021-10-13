import React from "react";
import NewMeeting from './pages/NewMeeting'
import Calendar from './pages/Calendar'

import { BsToggleOff, BsToggleOn } from "react-icons/bs"

export default class Home extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            toggle: true
        }
        
        this.toggle = this.toggle.bind(this)
    }

    toggle(){
        this.setState({
            toggle: !this.state.toggle
        })
    }
    
    render(){
        return(
            <div className="container">
                {this.state.toggle ? <NewMeeting /> : <Calendar />}
                <h1 className="toggle">{this.state.toggle ? <BsToggleOn onClick={() => this.toggle()} /> : <BsToggleOff onClick={() => this.toggle()}/>}</h1>
            </div>
        );
    }
}