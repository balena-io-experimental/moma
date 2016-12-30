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

  update(endpoint, method) {
    fetch({ endpoint : endpoint, method: method })
    .then((res) => {
      if (res.status === 200) {
        console.log(this.props.endpoint, res.data);
        this.setState({
          isActive : res.data.value,
          date: new Date()
        });
      }
    }).catch((err) => {
      console.error(err);
    })
  }

  componentDidMount() {
    this.update(this.props.endpoint, 'GET');
    setInterval(() => {
      this.update(this.props.endpoint, 'GET');
    }, this.props.interval || 3000);
  }

  render() {
    return (
      <p>
        <button className={`button ${this.state.isActive ? 'active' : 'inActive'}`}
        onClick={(e) => {
          this.update(`${this.props.endpoint}`, 'PUT');
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
