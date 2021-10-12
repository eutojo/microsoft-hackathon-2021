import React from "react";
import { AiOutlineClose } from 'react-icons/ai';

export default class MeetingDetails extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            floorplan: '',
            currentFloor: ''
        }
    }

    componentDidMount(){
        this.getFloor()
    }

    componentDidUpdate(prevProps){
        if (this.props.selectedFloor != prevProps.selectedFloor && this.props.selectedFloor['id'] != ""){
            console.log(this.props.selectedFloor['name'])
            this.getFloor()
            this.forceUpdate()
        }
    }

    async getFloor(){
        this.setState({
            currentFloor: this.props.selectedFloor['name']
        })

        fetch('/floor/' + this.props.selectedFloor['id'])
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
                    <h1 onClick={() => this.props.setFloor("","")} style={{"cursor":"pointer"}}><AiOutlineClose /></h1>
                </div>
                <div>
                    {this.props.floorplan != "" && Object.entries(this.state.floorplan).map(([floor, value]) => 
                        <div className="plan row">
                            {value.map((points) => <div className={`plan column ${points.includes(255) ? `color` : `no-color`}`} > </div>)}
                        </div>
                    )}
                </div>
                <h2>{this.state.currentFloor}</h2>
            </div>
        );
    }
}