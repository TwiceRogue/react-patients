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

    static defaultProps = {
        patientData: []
      }


    render(){

        const patientData = this.props.patientData
        const columnsCell = []
        for(let i =0;i<this.props.columnsNumber;i++){
            columnsCell.push(
                <Cell key = {i} rowID ={this.state.rowID} columnID ={i} patientColumnData = {this.props.patientData[i]}/>
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