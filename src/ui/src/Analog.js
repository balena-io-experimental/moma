import React, { Component } from 'react';
import { fetch } from './api';
import LastUpdated from './LastUpdated'

class Analog extends Component {

  constructor(props) {
    super(props);
    this.state = {
      date: new Date()
    };
  }

  update(endpoint) {
    fetch({
      endpoint : endpoint
    })
    .then((res) => {
      if (res.status === 200) {
        this.setState({
          value : res.data.value,
          date: new Date()
        });
      }
    }).catch((err) => {
      console.error(err)
    })
  }

  componentDidMount() {
    this.update(this.props.endpoint)
    setInterval(() => {
      this.update(this.props.endpoint)
    }, this.props.interval || 1000);

  }

  render() {
    return (
        <a className="analog">
         { this.props.text }: <code>{ this.state.value }</code>
         <LastUpdated date={this.state.date} />
        </a>
    );
  }
}

export default Analog;
