import React, { Component } from 'react';
import { fetch } from './api';
import LastUpdated from './LastUpdated';

class Button extends Component {

  constructor(props) {
    super(props);
    this.state = {
      date: new Date()
    };
  }

  componentDidMount() {
    fetch({ endpoint : `${this.props.endpoint}` })
    .then((res) => {
      if (res.status === 200) {
        this.setState({
          isActive : res.data.active,
          date: new Date()
        });
      }
    }).catch((err) => {
      console.error(err);
    })
  }

  render() {
    return (
      <p>
        <button className={`button ${this.state.isActive ? 'active' : 'inActive'}`}
        onClick={(e) => {
          fetch({
            endpoint: `${this.props.endpoint}`,
            method: 'PUT'
          }).then((data) => {
            this.setState({
              isActive : !this.state.isActive,
              date: new Date()
            });
          }).catch((err) => {
            console.error(err)
          })
        }}
        {...this.props.attrs}>
        { this.props.text }
        </button>
        <LastUpdated date={this.state.date}/>
      </p>
    );
  }
}

export default Button;
