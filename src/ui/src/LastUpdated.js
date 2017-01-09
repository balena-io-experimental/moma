import React, { Component } from 'react';
import moment from 'moment';

class LastUpdated extends Component {
  render() {
    return(
      <span className="date">
        Last updated: { moment(this.props.date).format('h:mm:ss a') }
      </span>
    )
  }
}

export default LastUpdated
