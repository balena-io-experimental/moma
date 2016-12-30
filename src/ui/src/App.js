import React, { Component } from 'react';
import { fetch } from './api';
import Controls from './Controls';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {}
  }

  componentWillMount() {
    fetch({ endpoint: '/settings' }).then((res) => {
      console.log(res)
      this.setState({
        settings: res.data
      });
    }).catch((err) => {
      console.error(err);
    })
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Jbay hackfriday 30 December</h2>
        </div>
        <div className="App-intro">
          <Controls settings={this.state.settings} />
        </div>
      </div>
    );
  }
}

export default App;
