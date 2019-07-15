import React, { Component } from 'react'
import PropTypes from 'prop-types'
import TableHead from './TableHead'
import TableRow from './TableRow';
import { tsAnyKeyword } from '@babel/types';

class PatientsTable extends Component{
    constructor(props){
        super(props)
        this.state = {columnsNumber:20,
                      rowsNumber:50}
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
           <TableRow key = {i} rowID = {i}/>
          )
        }

        return (
                <div className={`table-box ${className}`}>
                  <table style={style}>
                    {/* 表头部分 */}
                    <TableHead/>
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