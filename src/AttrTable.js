import React, { Component } from 'react'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import  './index.css'
import { connect } from 'react-redux'
import Cell from './Cell'
import {
    faEye, faEyeSlash
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

        for(let i=0;i< props.columnsInfo.length;i++){
            if(props.columnsInfo[i]['attributename']!='id' && props.columnsInfo[i]['category']=='string'){
                Visibility[props.columnsInfo[i]['attributename']] = false
            }
            else{
                Visibility[props.columnsInfo[i]['attributename']] = true
            }
        }
        this.setState({
            Visibility:Visibility
        })
        this.props.SetInvisible(Visibility)
     
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
                        <FontAwesomeIcon icon={this.state.Visibility[attr['attributename']]? faEye:faEyeSlash} onClick={this.handleClickVisible.bind(this,attr['attributename'])} />
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

      handleClickVisible(columnName){
        console.log(this.state)
        let  nowVisibility = this.state.Visibility
        nowVisibility[columnName] = !nowVisibility[columnName]
        this.setState({
            Visibility:nowVisibility
        })

        this.props.SetInvisible(nowVisibility)
        
       

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

//需要渲染什么数据

function mapStateToProps(state) {
    return {
      visibility: state.Visibility
    }
  }
  
//需要触发什么行为

function mapDispatchToProps(dispatch) {
    return {
      SetInvisible: (visibility) => {dispatch({ type: 'SetInvisible',visibility:visibility})}
    }
  }



AttrTable = connect(mapStateToProps,mapDispatchToProps)(AttrTable)

export default AttrTable