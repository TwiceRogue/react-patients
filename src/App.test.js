import React from 'react';
import ReactDOM from 'react-dom';
import ReactPatientsApp from './ReactPatientsApp';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ReactPatientsApp />, div);
  ReactDOM.unmountComponentAtNode(div);
});
