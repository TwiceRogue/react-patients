import React, { Component } from 'react'
import Cell from './Cell'


class TableRow extends Component {
    constructor(props){
        super(props)
        this.state = {columns:20}
    }

    componentWillMount(){
        this.setState({rowID:this.props.rowID})
    }



    render(){

        const patientData = this.props.patientData
        const columnsCell = []
        for(let i =0;i<this.state.columns;i++){
            columnsCell.push(
                <Cell key = {i} rowID ={this.state.rowID} columnID ={i}/>
            )
        }
        return(
           <tr>
               {columnsCell}
           </tr>
        
        )
    }

}

export default TableRow