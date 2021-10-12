import React from "react";
import { AiOutlineClose } from 'react-icons/ai';

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floorplan: ''
        }
    }

    componentDidMount(){
        this.getFloor()
    }

    async getFloor(){
        fetch('/floor/' + this.props.selectedFloor)
        .then(res => res.json())
        .then(res => this.setState({
            floorplan: res
        }))

    }

    render(){
        return(
            <div className="left-panel building-view floor-view">
                <div className="row title">
                    <h1 style={{"margin-left":"1em"}}></h1>
                    <h1>{this.props.selectedBuilding}</h1>
                    <h1 onClick={() => this.props.setFloor("")} style={{"cursor":"pointer"}}><AiOutlineClose /></h1>
                </div>
                <div>
                    {this.props.floorplan != "" && Object.entries(this.state.floorplan).map(([floor, value]) => 
                        <div className="plan row">
                            {value.map((points) => <div className={`plan column ${points.includes(255) ? `color` : `no-color`}`} > </div>)}
                        </div>
                    )}
                </div>
                <h2>{this.props.selectedFloor}</h2>
            </div>
        );
    }
}