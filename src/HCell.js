import React, { Component } from 'react'
import { tsImportEqualsDeclaration } from '@babel/types';


class HCell extends Component {

    constructor(props){
        super(props)
    
    }

    componentDidMount(){
        this.setState({columnName:this.props.columnName,
                       columnID:this.props.columnID})

    }



    render(){

        return(
            <td>
            <div className = 'Hcell' >
                {this.props.columnName}
            </div>
            </td>
        )

    }


}

export default HCell