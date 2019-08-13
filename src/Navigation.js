import React, { Component } from 'react'
import { exportSpecifier } from '@babel/types';


class Navigation extends Component{


    componentDidMount(){

    }


    render(){
        return(
            <div className= 'pointsRule row'>
               
                <ul>
                    <li className="stageNavLi"   ><a ><span className="stageNavSpan">入院</span><i></i></a></li>
                    <li className="stageNavLi" ><a ><span className="stageNavSpan">早期评估</span><i ></i></a></li>
                    <li className="stageNavLi" ><a ><span className="stageNavSpan">术前</span><i ></i></a></li>
                    <li className="stageNavLi" ><a ><span className="stageNavSpan">术中</span><i ></i></a></li>
                    <li className="stageNavLi" ><a ><span className="stageNavSpan">术后</span><i ></i></a></li>
                    <li className="stageNavLi" ><a ><span className="stageNavSpan">出院</span><i ></i></a></li>
                </ul>
            
            </div>
        
        )
    }
    
}

export default Navigation