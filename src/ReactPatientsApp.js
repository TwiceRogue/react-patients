import React, {Component} from 'react'
import AttrTable from './AttrTable'
import PatientsTable from './PatientsTable'
import StarChart from './StarChart'
import Histograms from './Histograms'
import Navigation from './Navigation'
import axios from  'axios'
import  "./index.css";

axios.defaults.withCredentials = false;
axios.defaults.headers.post['Content-Type'] = 'application/json';
const server = 'http://127.0.0.1:8000'

class ReactPatientsApp extends Component {
    constructor(){
        var data = [['0','1'],['0','1']]
        super()
        this.state={
            allPatientsData:data
        }
    }


    componentDidMount(){
        console.log('componentDidMount~')
        axios({
            method: 'post',
            url:`${server}/database/`,
            data: {
                shownumber: 50
            }
        })
              .then((response)=>{
                // 在这儿实现 setState
                console.log(response)
                console.log(response['data'][0])
                this.setState({
                    allPatientsData:response['data'][4],
                    columnsInfo:response['data'][3],
                    columnsCate:response['data'][6]
                }) // 你拿到数据之后，又刷新了一次，所以就有两次了呀。。
                  // 那我应该怎么写 will mount 的时候直接渲染数据么
            })
            .catch((error)=>{
                // 处理请求出错的情况
                console.log(error)
            })
          
    }



    render(){
        return(
            <div>
            <div className='col-md-2'>
                <AttrTable className = 'attrTable panel' 
                           columnsNumber = {Object.keys(this.state.allPatientsData[0]).length} 
                           columnsInfo = {this.state.columnsInfo} 
                           columnsCate={this.state.columnsCate}/>
                <StarChart/>
            </div>
            <div className='col-md-10'>
                <Navigation/>
                <PatientsTable className = 'mainTable' allPatientsData = {this.state.allPatientsData} columnsNumber = {Object.keys(this.state.allPatientsData[0]).length} 
                                columnsInfo = {this.state.columnsInfo} columnsCate={this.state.columnsCate}/>
                <Histograms/>
            </div>
            </div>
        )
    }



}





export default ReactPatientsApp