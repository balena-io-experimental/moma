import React, { Component } from 'react';
import { fetch } from './api';
import LastUpdated from './LastUpdated';
import Button from './Button.js';
import Analog from './Analog.js';
import _ from 'lodash';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      settings: {},
      editing: false
    }
  }

  componentWillMount() {
    this.getSettings()
    .then(() => {
      return this.getData();
    })
    .then(() => {
      setInterval(() => {
        this.getData();
      }, this.state.settings.POLL_INT || 1000);
    }).catch((err) => {
      console.error(err)
    });
  }

  getData() {
    return fetch({ endpoint: '/state' }).then((res) => {
      this.setState({
        data: res.data,
        lastUpdate: new Date()
      });
    })
  }

  getSettings() {
    return fetch({ endpoint: '/settings' }).then((res) => {
      this.setState({
        settings: res.data,
      });
    })
  }

  loadData(data, settings) {
    const { editing } = this.state

    return(
      <div>
        <h2>Relays</h2>
        {
          data.RELAYS.map((o, i) => {
            return (
              <div key={o.name}>
                <Button name={o.name} label={settings.RELAYS[i]}  value={o.value} attrs={{ disabled: !editing }}/>
              </div>
            )
          })
        }
        <h2>Analogs</h2>
        {
          data.ANALOGS.map((o, i) => {
            return (
              <div key={o.name}>
                <Analog name={o.name} label={settings.ANALOGS[i]} value={o.value} attrs={{ disabled: !editing }}/>
              </div>
            )
          })
        }
        <h2>Inputs</h2>
        {
          data.INPUTS.map((o,i) => {
            return (
              <div key={o.name}>
                <Button name={o.name} label={settings.INPUTS[i]} value={o.value} attrs={ { disabled : true } } />
              </div>
            )
          })
        }
        <h2>Outputs</h2>
        {
          data.OUTPUTS.map((o, i) => {
            return (
              <div key={o.name}>
                <Button name={o.name} label={settings.OUTPUTS[i]} value={o.value} id={o.name} attrs={{ disabled: !editing }}/>
              </div>
            )
          })
        }
      </div>
    )
  }


  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Moma</h2>
          <LastUpdated date={this.state.lastUpdate} />
          <div>  
            <button className={`button ${ !this.state.editing ? 'active': 'inActive'}`} onClick={() => { this.setState((prevState) => ({ editing: !prevState.editing })) }}>{ this.state.editing ? 'Stop' : 'Start' } editing</button>
          </div>
        </div>
        <div className="App-intro">
        { _.isEmpty(this.state.data) ?  <div>Loading...</div> : this.loadData(this.state.data, this.state.settings)}
        </div>
      </div>
    );
  }
}

export default App;
