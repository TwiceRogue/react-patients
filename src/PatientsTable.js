import React, { Component } from 'react'
import PropTypes from 'prop-types'
import TableHead from './TableHead'
import TableRow from './TableRow';
import { tsAnyKeyword } from '@babel/types';
import { PassThrough } from 'stream';

class PatientsTable extends Component{
    constructor(props){
        super(props)
        this.state = {columnsNumber:20,
                      rowsNumber:50}
    }

    static defaultProps = {
      columnsNumber: 20,
      columnsInfo:[{}]
    }



    render(){
        let rows = [];
        const {
                className,
                columns,
                dataSource,
                pagination,
                rowSelection,
                style,
                emptyText,
                isLastNoOp
              } = this.props;
        const { rowCheck } = this.state;

        const tableTr = [] 
        for (var i=0;i<this.state.rowsNumber;i++) {
          tableTr.push( 
           <TableRow key = {i} rowID = {i} patientData = {this.props.allPatientsData[i]} columnsNumber={this.props.columnsNumber} columnsInfo={this.props.columnsInfo} 
            columnsCate = {this.props.columnsCate}/>
          )
        }

        return (
                <div className={`table-box ${className}`}>
                  <table style={style}>
                    {/* 表头部分 */}
                    <TableHead 
                    headData = {this.props.allPatientsData} 
                    columnsNumber={this.props.columnsNumber} 
                    columnsInfo={this.props.columnsInfo} 
                    columnsCate = {this.props.columnsCate}/>
                    <tbody>
                      {
                        // dataSource.map((data, i) => {
                        //   return (
                        //    <TableRow patientData = {data} />
                        //   )
                        // })
                        tableTr
                            
                        

                      }
                    </tbody>
                  </table>

                  {/* <ListNone list={dataSource} text={emptyText} />
                  <Pager {...pagination} /> */}

                </div>
              );
            }
          
        
    
    
}

export default PatientsTable