import React, {Component} from 'react'
import AttrTable from './AttrTable'
import PatientsTable from './PatientsTable'
import StarChart from './StarChart'
import Histograms from './Histograms'
import Navigation from './Navigation'
import { directive } from '@babel/types';

class ReactPatientsApp extends Component {
    render(){
        return(
            <div>
            <div className='col-md-2'>
                <AttrTable/>
                <StarChart/>
            </div>
            <div className='col-md-10'>
                <Navigation/>
                <PatientsTable/>
                <Histograms/>
            </div>
            </div>
        )
    }



}

export default ReactPatientsApp