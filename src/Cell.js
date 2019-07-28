import React, { Component } from 'react'
import { tsImportEqualsDeclaration } from '@babel/types';


class Cell extends Component {

    constructor(props){
        super(props)
    
    }

    componentDidMount(){
        this.setState({rowID:this.props.rowID,
                       columnID:this.props.columnID})

    }



    render(){

        return(
            <td>
            <div className = 'cell' >
                {this.props.patientColumnData}
            </div>
            </td>
        )

    }


}

export default Cell