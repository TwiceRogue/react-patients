import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';
import ReactPatientsApp from './ReactPatientsApp'
import * as serviceWorker from './serviceWorker';
import 'bootstrap/dist/css/bootstrap.css'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import reducer from './reducer/reducer'

const store = createStore(reducer);

ReactDOM.render(
<Provider store={store}><ReactPatientsApp/></Provider>, 
document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
