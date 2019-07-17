import React, {Component} from 'react'
import AttrTable from './AttrTable'
import PatientsTable from './PatientsTable'
import StarChart from './StarChart'
import Histograms from './Histograms'
import Navigation from './Navigation'
import axios from  'axios'

axios.defaults.withCredentials = false;
axios.defaults.headers.post['Content-Type'] = 'application/json';
const server = 'http://127.0.0.1:8000'

class ReactPatientsApp extends Component {
    constructor(){
        super()
    }


    componentDidMount(){

        axios({
            method: 'post',
            url:`${server}/database/`,
            data: {
                shownumber: 50,
                id:20
            }
        })
              .then((response)=>{
                // 在这儿实现 setState
                console.log(response)
                this.setState({
                    patientsData:response[0]
                })
            })
            .catch(function(error){
                // 处理请求出错的情况
                console.log(error)
            })
          
    }



    render(){
        return(
            <div>
            <div className='col-md-2'>
                <AttrTable/>
                <StarChart/>
            </div>
            <div className='col-md-10'>
                <Navigation/>
                <PatientsTable className = 'mainTable'/>
                <Histograms/>
            </div>
            </div>
        )
    }



}

export default ReactPatientsApp