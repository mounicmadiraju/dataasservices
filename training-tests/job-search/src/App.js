import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import JobForm from './components/job-form'
import {Motion, spring, StaggeredMotion} from 'react-motion';
import Test from './components/test';

import 'bootstrap/dist/css/bootstrap.css';
import { InputGroup, InputGroupAddon, Input, Container, Button, Row, Col } from 'reactstrap';

const Search = (props) => {
  return (
    <div>
      <Container>
        
      

        <div className="home" >
          <Test/>
          <img src="http://jobsharks.net/wp-content/uploads/2017/08/jobshark-white-1.png" />
          <div className="search-wrap">
            
            <form>
              
              <Row>
                <Col xs="6" md="6">
                  <Input placeholder="Job Title, keywords etc" />
                </Col>
                <Col xs="6" md="3">
                  <Input placeholder="City or Zip" />
                </Col>
                <Col sm="12" md="3" >
                  <Button block color="primary">Submit</Button>

                  <StaggeredMotion
  defaultStyles={[{h: 0}, {h: 0}, {h: 0}]}
  styles={prevInterpolatedStyles => prevInterpolatedStyles.map((_, i) => {
    return i === 0
      ? {h: spring(100)}
      : {h: spring(prevInterpolatedStyles[i - 1].h)}
  })}>
  {interpolatingStyles =>
    <div>
      {interpolatingStyles.map((style, i) =>
        <div key={i} style={{border: '1px solid', height: style.h}} />)
      }
    </div>
  }
</StaggeredMotion>
                </Col>
              </Row>
            </form>
          </div>
      </div>
      
      </Container>
    </div>
  );
};

export default Search;