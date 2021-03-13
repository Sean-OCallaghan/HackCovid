import React, {Component} from 'react';
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import './Header.css';
export default class Header extends Component{
  
  render(){ 
  return (
    <div class="header"> 
    <Jumbotron fluid>
    <div class="Container">
  <Container >
    <h1>Yes</h1>
    <p>
      Do you have a waitlist you would like to optimize for your community?
    </p>
  </Container> 
  </div>
</Jumbotron>
</div>
  );
  }
}

