import React, { Component } from 'react'


class Cell extends Component {

    constructor(props){
        super(props)
    
    }

    componentWillMount(){
        this.setState({rowID:this.props.rowID,
                       columnID:this.props.columnID})

    }



    render(){

        return(
            <td>
            <div className = 'cell'>
                {this.props.rowID+':'+this.props.columnID}
            </div>
            </td>
        )

    }


}

export default Cell