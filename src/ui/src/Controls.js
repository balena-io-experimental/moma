import React, { Component } from 'react';
import Button from './Button.js';
import Analog from './Analog.js';

class Controls extends Component {
  render() {
    if (!this.props.settings) {
      return (<div>Loading Settings</div>)
    } else {
      return (
        <div>
          <h2>Relays</h2>
          {
            this.props.settings.RELAYS.map((o) => {
              return (
                <div key={o.endpoint}>
                  <Button endpoint={o.endpoint} text={o.name} />
                </div>
              )
            })
          }
          <h2>Analogs</h2>
          {
            this.props.settings.ANALOGS.map((o) => {
              return (
                <div key={o.endpoint}>
                  <Analog endpoint={o.endpoint} text={o.name} interval={ this.props.settings.POLL_INT }/>
                </div>
              )
            })
          }
          <h2>Inputs</h2>
          {
            this.props.settings.INPUTS.map((o) => {
              return (
                <div key={o.endpoint}>
                  <Button endpoint={o.endpoint} text={o.name} attrs={ { disabled : true } } />
                </div>
              )
            })
          }
        </div>
      )
    }
  }
}

export default Controls;
