import React, { Component } from 'react';

class Analog extends Component {

  render() {
    return (
      <a className="analog">
       { this.props.label || this.props.name }: <code>{ this.props.value }</code>
      </a>
    );
  }
}

export default Analog;
