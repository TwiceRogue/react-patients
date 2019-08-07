import React, { Component } from 'react';
import * as d3 from "d3";
import { connect } from 'react-redux'
import { tsImportEqualsDeclaration } from '@babel/types';
import { faShower } from '@fortawesome/fontawesome-free-solid';


class Cell extends Component {

    constructor(props){
        super(props)
        this.state = {
            category: undefined
        }
    }

    static defaultProps = {
        columnsInfo: [{}],
        columnName:""    
      }


    componentDidMount(){
        const props = this.props

        
    //    console.log(this.props.columnName) 
       this.drawSVG.bind(this)(props)   // 立即执行才会绘制
    }

    componentWillReceiveProps(props) {
        //debugger
        this.drawSVG.bind(this)(props)   // 立即执行才会绘制
    }

    drawSVG(props){
        this.setState({
            rowID:props.rowID,
            columnID:props.columnID,
            columnName:props.columnName,
            category:props.category,
            data:props.patientColumnData,
            columnsCate:props.columnsCate,
            columnStage:props.columnStage,
            visible: true
        });

        var tr_width = 80
        var th_height = 20
        var rect_r = 10
        d3.select(this._rootNode).select('svg').remove()
        const svg = d3.select(this._rootNode).append("svg").attr("width", 80).attr("height", 20);
        if(props.category=='numerical'){

        var rScale = d3.scaleLinear().range([0, tr_width]).domain([props.columnsCate["low"],props.columnsCate["high"]]);

        svg.append("rect")
            .attr("class", "rectTable")
            .attr("width", rScale(props.patientColumnData))
            .attr("height", th_height)
            .attr("rx", 3)
            .attr("ry", 3)
            .attr("transform", "translate(" + 0 + "," + 3 + ")")
            .attr("fill",'orange')
            .attr("opacity",0.5);
        svg.append('text')
            .text(props.patientColumnData.toFixed(2))
            .attr('fill', 'black')
            .attr('x', rScale(props.patientColumnData))
            .attr('y', th_height / 2)
            .attr('text-anchor', 'right')
            .style('font-size', '10px')
            .attr('dy', 8);

        }
        else if(props.category=='categorical'){
            svg.append("rect")
            .attr("class", "tableRect")
            .attr("x", 0)
            .attr("y", th_height / 4)
            .attr("width", 10)
            .attr("height", 10)
            .attr("fill", 'orange');//localColorScale(query_patient[column_names[col]])

            svg.append('text')
            .text(props.patientColumnData).attr('fill', 'black')
            .attr('x', rect_r * 1.5)
            .attr('y', th_height / 2 - rect_r / 2)
            .attr('text-anchor', 'left')
            .style('font-size', '12px')
            .attr('dy', 8);
        }
        else if(props.category == 'string'){

            svg.append("text")
            .attr("class", "textTable")
            .text(props.patientColumnData) //
            .attr('text-anchor', 'middle')
            .attr("transform", "translate(" + tr_width / 2 + "," + th_height / 2 + ")")
            
        }

        else {

            svg.append("text")
            .attr("class", "textTable")
            .text(props.patientColumnData)
            .attr('text-anchor', 'middle')
            .attr("transform", "translate(" + tr_width / 2 + "," + th_height / 2 + ")");
        }
    }

    _setRef(componentNode){
        this._rootNode = componentNode;
    }

    render() {
        return(
            <td className={this.props.visible ? 'show-table-cell':'hidden'}>
            <div className={`cell ${this.state.category} `} ref={this._setRef.bind(this)}/>
            </td>
        )

    }


}


function mapStateToProps(state,ownProps) {
    console.log(state)
    
    return {    
      visible: state.columnName==ownProps.columnName ? state.visibility:true,
      columnName:state.columnName
    }
  }
  

  
  
export default Cell = connect(mapStateToProps)(Cell)