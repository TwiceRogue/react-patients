import React, { Component } from 'react'
import Cell from './Cell'


class TableRow extends Component {
    constructor(props){
        super(props)
        this.state = {columns:20}
    }

    componentWillMount(){
        // this.setState({rowID:this.props.rowID,
        //             columnsInfo:this.props.columnsInfo,
        //             columnsCate:this.props.columnsCate})
        
    }

    static defaultProps = {
        patientData: [],
        columnsInfo:[{}],
        columnsCate:{}
      }


    render(){

        const patientData = this.props.patientData
        const columnsCell = []
        for(let i =0;i<this.props.columnsInfo.length;i++){
           
            columnsCell.push(
                <Cell key = {i} rowID ={this.state.rowID} columnID ={i} patientColumnData = {this.props.patientData[this.props.columnsInfo[i]['attributename']]} 
                         columnName = {this.props.columnsInfo[i]['attributename']}
                         category = {this.props.columnsInfo[i]['category']}
                         columnsCate = {this.props.columnsCate[this.props.columnsInfo[i]['attributename']]}
                         columnStage = {this.props.columnsCate[this.props.columnsInfo[i]['stage']]}/>
            )
        }
        console.log(columnsCell)
        return(
           <tr>
               {columnsCell}
           </tr>
        
        )
    }

}

export default TableRow