import React, { Component } from 'react';
import { fetch, createURL } from './api';

class Button extends Component {

  constructor(props) {
    super(props);
    this.state = {
      value: this.props.value
    };
  }

  update(endpoint, method) {
    fetch({ endpoint : endpoint, method: method })
    .then((res) => {
      if (res.status === 200) {
        this.setState({
          value : res.data.value
        });
      }
    }).catch((err) => {
      console.error(err);
    })
  }

  render() {
    return (
      <p>
        <button className={`button ${this.state.value ? 'active' : 'inActive'}`}
        onClick={(e) => {
          this.update(`${createURL(this.props.name)}`, 'PUT');
        }}
        {...this.props.attrs}>
        { this.props.label || this.props.name }
        </button>
      </p>
    );
  }
}

export default Button;
