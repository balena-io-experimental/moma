import React, { Component } from 'react';
import moment from 'moment';

class LastUpdated extends Component {
  render() {
    return(
      <span className="date">
        lastupdated: { moment(this.props.date).calendar() }
      </span>
    )
  }
}

export default LastUpdated
