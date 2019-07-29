import React, { Component } from 'react'
import HCell from './HCell';
import { EACCES } from 'constants';


class TableHead extends Component {
    constructor(props){
        super(props)
        this.state = {size:20}
    }


    static defaultProps = {
        columnsInfo: [{}],
        columnsCate:{}   
      }


    render(){
        const HeadCell = []
        const allpatientsDictData = this.props.headData
        var eachColunmData ={}
        
        for(let i=0;i<this.props.columnsInfo.length;i++){
            var temp =[]
            var columnName = this.props.columnsInfo[i]['attributename']
            for(let j=0;j<allpatientsDictData.length;j++){
                temp.push(allpatientsDictData[j][columnName])
            }
            eachColunmData[columnName] = temp
        }
        for(let i =0;i<this.props.columnsInfo.length;i++){  // 这里confidence 多一个会越界 在下面的时候
            HeadCell.push(
                <HCell key = {i} 
                columnName={this.props.columnsInfo[i]['attributename']} 
                columnID ={i} 
                columnsInfo = {this.props.columnsInfo[i]} 
                category = {this.props.columnsInfo[i]['category']}
                eachColunmData = {eachColunmData[this.props.columnsInfo[i]['attributename']]}
                columnsCate = {this.props.columnsCate[this.props.columnsInfo[i]['attributename']]}/>
            )
        }

        return(
           <thead>
                <tr>{
                    HeadCell
                }
                </tr>
           </thead>
        
        )
    }

}

export default TableHead