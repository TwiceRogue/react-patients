import React, { Component } from 'react'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import  './index.css'

import {
    faEye
} from '@fortawesome/fontawesome-free-solid'
import { exportSpecifier } from '@babel/types';


class AttrTable extends Component{
    constructor(){
        super()
    }


    static defaultProps = {
        columnsNumber: undefined,
        columnsInfo :[],
        columnsCate : undefined
      }

      componentWillReceiveProps(props){
        var Visibility = {}

        for(let i in props.columnsInfo){
            if(i['attributename']!='id' && i['category']=='string'){
                Visibility[i['attributename']] = false
            }
            else{
                Visibility[i['attributename']] = true
            }
        }
        this.setState({
            Visibility:Visibility
        })
     
    }

    genRows(props){
          const rows = props.columnsInfo.map( (attr,index)=>
            <tr className='attrTr' key={index}>
                <td className='attrTableTdWide'> 
                    <div className = 'mytddivclass'>
                        {attr['attributename']}
                    </div>
                </td>
                <td className='attrTableTdWide'>
                    <div className = 'mytddivclass' >
                        {attr['category']}                        
                    </div>
                </td>
                <td className='attrTableTdNarrow'>
                    <div className = 'mytddivclass'>
                        <FontAwesomeIcon icon={faEye} onClick={this.handleClickVisible.bind(this)}/>
                    </div>
                </td>
                <td className='attrTableTdNarrow'>
                    <input type="text" value = {attr['weight']} className='inputW1'>
                    </input>
                </td>
            </tr>
          

          )
          return rows
      }
      genHead(props){
        const attrTableHeadName = ['Attributes','Stages','Visibility','Weights']

       const attrTableHead = attrTableHeadName.map(
            (name)=>
            <th>
                {name}
            </th>

            
        )
        return attrTableHead
      }

      handleClickVisible(){
        console.log(this.state.Visibility)
      }


    render(){
        
        
        return(
            <div className={this.props.className}>
                <table className = 'tableAttr'>
                    <thead> 
                        <tr>{this.genHead(this.props)}</tr>
                    </thead>
                    <tbody> {this.genRows(this.props)}</tbody>
                </table>
            </div>
        
        )
    }
    
}

export default AttrTable