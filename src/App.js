import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './Components/Header';
import FileUpload from './Components/fileUpload'

class App extends Component{
  render(){ 
  return (
    <div className="App">
      <Header />
      <FileUpload/>
    </div>
  );
  }
}

export default App;
