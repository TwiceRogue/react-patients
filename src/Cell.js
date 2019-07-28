import React, { Component } from 'react';
import * as d3 from "d3";
import { tsImportEqualsDeclaration } from '@babel/types';


class Cell extends Component {

    constructor(props){
        super(props)
    
    }

    componentDidMount(){
        this.setState({rowID:this.props.rowID,
                       columnID:this.props.columnID,
                       columnName:this.props.columnName,
                       category:this.props.category,
                       data:this.props.patientColumnData,
                       columnsCate:this.props.columnsCate,
                      
                        });
        
       this.drawSVG.bind(this)()

    }


    drawSVG(){
        var tr_width = 80
        var th_height = 20
        const svg = d3.select(this._rootNode).append("svg").attr("width", 80).attr("height", 20);
        if(this.props.category=='numerical'){

        var rScale = d3.scaleLinear().range([0, tr_width]).domain([this.props.columnsCate["low"],this.props.columnsCate["high"]]);

        svg.append("rect")
            .attr("class", "rectTable")
            .attr("width", rScale(this.props.patientColumnData))
            .attr("height", th_height)
            .attr("rx", 3)
            .attr("ry", 3)
            .attr("transform", "translate(" + 0 + "," + 3 + ")")
            .attr("fill",'orange')
            .attr("opacity",0.5);
        svg.append('text')
            .text(this.props.patientColumnData.toFixed(2))
            .attr('fill', 'black')
            .attr('x', rScale(this.props.patientColumnData))
            .attr('y', th_height / 2)
            .attr('text-anchor', 'right')
            .style('font-size', '10px')
            .attr('dy', 8);

        }
        else if(this.props.category=='categorical'){
            svg.append("rect")
            .attr("class", "tableRect")
            .attr("x", 0)
            .attr("y", th_height / 4)
            .attr("width", 10)
            .attr("height", 10)
            .attr("fill", 'orange');//localColorScale(query_patient[column_names[col]])
        }
    }

    _setRef(componentNode){
        this._rootNode = componentNode;
    }

    render(){

        return(
            <td>
            <div className = 'cell' ref={this._setRef.bind(this)}>
               
            </div>
            </td>
        )

    }


}

export default Cell