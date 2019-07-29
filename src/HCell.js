import React, { Component } from 'react'
import * as d3 from "d3";
import { tsImportEqualsDeclaration } from '@babel/types';


class HCell extends Component {

    constructor(props){
        super(props)
    
    }
    static defaultProps = {
        columnsInfo: {},
        columnName:"",
        eachColunmData:[],
        columnsCate:{}    
      }


    componentDidMount(){
        const props = this.props
        this.setState({columnName:this.props.columnName,
                       columnID:this.props.columnID})
          
    //    console.log(this.props.columnName) 
       this.drawHead.bind(this)(props)   // 立即执行才会绘制
    }

    // componentWillReceiveProps(props) {
    //     //debugger
    //     this.drawHead.bind(this)(props)   // 立即执行才会绘制
    // }

    drawHead(props){

        if(props.category=='numerical'){
            var col_data = props.eachColunmData;
            var columnName = props.columnName
            var max_value = props.columnsCate['high'];
            var min_value = props.columnsCate["low"];
        
         
            var bin_num = 9;
            var bins = (max_value-min_value)/bin_num;
            var obj = {},k;
            for (var i = 0;i<bin_num+1;i++){
                obj[i]=0;
            }
            for (var i = 0, len = col_data.length; i < len; i++) {
                    // k = col_data[i];
                    // if (obj[k])
                    //     obj[k]++;
                    // else
                    //     obj[k] = 1;
                    obj[Math.floor((col_data[i]-min_value)/bins)]++;
                    //onsole.log(Math.floor((col_data-min_value)/bins));
        
                }
            obj[8]+=obj[9];
            delete obj[9];

            var max_number = 0;
            var obj_length = 0;
            for(var o in obj){
                obj_length++;
                if (obj[o]>max_number)
                    max_number = obj[o]
            }   
                
    
            var cate_count = 0 ;
            for (var j in obj){
                    //console.log(70/obj_length);
                d3.select(this._rootNode).append('div')
                        .style('height',((obj[j]/max_number)*90).toString()+"%")
                        .style('width',((78-2)/obj_length).toString()+'px')
                        .style('background-color','orange')//colorArr[attributeNumericalList.indexOf(columsName[col_num])]
                        .style('display','inline-block')
                        .style('border','1px solid')
                        .style('opacity',0.8)
                        .attr('transform',"translate(" + cate_count*((80-2)/obj_length) + "," + 20 + ")");
                cate_count++;
        
            }
            obj['min']=min_value;
            obj['max'] = max_value;
            //cross_cate.push(obj);
        }
        else if(props.category=='categorical'){
            const width = 80
            var color_categorical_2 = ["blue","orange"];
            var color_categorical_3=[ '#e5403c','#b286ff','#5684a2'];
            var color_categorical_8 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999'];
            var categoryNum = props.columnsCate["categoryNum"];
            var categorySet = props.columnsCate["categorySet"];
            var localColorSet = [];
            switch(categoryNum){
                case 2:
                    localColorSet = color_categorical_2;
                    break;
                case 3:
                    localColorSet = color_categorical_3;
                    break;
                default:
                    localColorSet = color_categorical_8;
            }
            var localColorScale = d3.scaleOrdinal().domain(categorySet).range(localColorSet);
    //        if(col_num==3){
    //            console.log(localColorScale(categorySet[0]),localColorScale(categorySet[2]));
    //        }
            var col_data = props.eachColunmData;
       
    
            var obj = {},k;
            for (var i = 0, len = col_data.length; i < len; i++) {
                k = col_data[i];
                if (obj[k])
                    obj[k]++;
                else
                    obj[k] = 1;
            }
            //console.log(obj);
            var max_number = 0;
            var obj_length = 0;
            for(var o in obj){
                obj_length++;
                if (obj[o]>max_number)
                    max_number = obj[o]
            }
            //console.log(max_number);
    
            var cate_count = 0 ;
            for (var j in obj){
                var bgc='#ffffff';
                if(j=='是'||j=='有'||j==1){
                    bgc = '#e41a1c';
                }
                else if (j=='无'||j=='否'||j==0){
                    bgc = '#377eb8';
                }
                else if(j=='NA'){
                    bgc = '#999999';
                }
                else if(j=='见现病史'){
                    bgc = '#4daf4a';
                }
                else if (j=='男'){
                    bgc='orange';
                }
                else if (j=='女'){
                    bgc = 'blue';
                }
                else {
                    bgc = color_categorical_8[cate_count];
                }
                //console.log(70/obj_length);
                d3.select(this._rootNode).append('div')
                    .style('height',((obj[j]/max_number)*90).toString()+"%")
                    .style('width',((78-2)/obj_length).toString()+'px')
                    .style('background-color',localColorScale(j))
                    .style('display','inline-block')
                    .style('border','1px solid')
                    .style('opacity',0.5)
                    .attr('title',j)
                    .attr('transform',"translate(" + cate_count*((width-2)/obj_length) + "," + 20 + ")");
                cate_count++;
            }
                 obj['min'] = -1000;
                 obj['max'] = -1000;
                 //cross_cate.push(obj);
        }
        
    }
 
    _setRef(componentNode){
        this._rootNode = componentNode;
    }



    render(){

        return(
            <th>
            <div>
                {this.props.columnName}
            </div>
            <div className = 'Hcell' ref={this._setRef.bind(this)} >
                {/* <div>
                this.props.columnName
                </div> */}
            </div>
            </th>
        )

    }


}

export default HCell