import React, { Component } from 'react'
import HCell from './HCell';


class TableHead extends Component {
    constructor(props){
        super(props)
        this.state = {size:20}
    }


    static defaultProps = {
        columnsInfo: [{}]   
      }


    render(){
        const HeadCell = []
        for(let i =0;i<this.props.columnsNumber-1;i++){  // 这里confidence 多一个会越界 在下面的时候
            HeadCell.push(
                <HCell key = {i} columnName={this.props.columnsInfo[i]['attributename']} columnID ={i} columnsInfo = {this.props.columnsInfo[i]} />
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