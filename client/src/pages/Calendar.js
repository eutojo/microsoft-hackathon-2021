import React from "react"
import {IoIosArrowBack} from 'react-icons/io'
import {ImBin} from 'react-icons/im'
import { FaCircle } from 'react-icons/fa';
import {AiFillCheckCircle} from 'react-icons/ai'
import { IoLocationOutline} from 'react-icons/io5';
import MapDetails from "../assets/components/calender-view/MapView";
export default class Calendar extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            toggle: false
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
            <div className="window-container mobile-container">
                
                {/* map here */}
                <div className="mobile">
                    <div className="tab">
                        <h3><IoIosArrowBack /></h3>
                        <h3>Calender</h3>
                        <h3><ImBin /></h3>
                    </div>
                    <div className="info-container">
                        <div className="info-section">
                            <h2><FaCircle style={{'fill': '#3787e9'}}/></h2>
                            <div className="data">
                                <h2>General Monthly Catcbup</h2>
                                <h3>Thursday, 29 February 2022, 10:30am</h3>
                            </div>
                        </div>
                        <div className="info-section">
                            <h2><AiFillCheckCircle style={{'fill': 'green'}} /></h2>
                            <div className="data">
                                <h2>Accepted</h2>
                            </div>
                        </div>
                        <div className="info-section">
                            <div className="data last">
                                <h3>Hello Mate, looking good there for a catchup hahahahhahaahhahahahah</h3>
                            </div>
                        </div>
                    </div>    
                    <div className="info-container">
                        <div className="info-section">
                            <h2><IoLocationOutline /></h2>
                            <div className="data">
                                <h2>Foundry Level 1 Room 08</h2>
                            </div>
                            <div className="data-button" onClick={() => this.toggle()}>
                                <h2>Navigate</h2>
                            </div>
                        </div>
                        <div className="info-section map">
                            {this.state.toggle && <MapDetails />}
                        </div>    
                    </div>    
                </div>
            </div>
        );
    }
}