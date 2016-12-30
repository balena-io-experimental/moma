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

  componentDidMount() {
    setInterval(() => {
      fetch({
        endpoint : `${this.props.endpoint}`
      })
      .then((res) => {
        if (res.status === 200) {
          this.setState({
            reading : res.data.reading,
            date: new Date()
          });
        }
      }).catch((err) => {
        console.error(err)
      })
    }, this.props.interval || 1000);

  }

  render() {
    return (
        <a>
         { this.props.text } : { this.state.reading }
         <LastUpdated date={this.state.date} />
        </a>
    );
  }
}

export default Analog;
