import React from "react";
import Window from './assets/components/Window'

export default class Home extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            time: ''
        }

        this.fetchTime = this.fetchTime.bind(this);
    }


    async fetchTime(){
        fetch('/time')
        .then(res => res.json())
        .then(data => this.setState(
            {
                'time': data.time,
            }
        ))
    }

    componentDidMount(){
        this.fetchTime();
    }

    render(){
        return(
            <div className="container">
                <Window />
            </div>
        );
    }
}