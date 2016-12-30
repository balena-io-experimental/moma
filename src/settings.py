def defaults():
    return({
    "POLL_INT": 3000,
    "RELAYS": [
      {
        "name": 'Pump outside house',
        "endpoint": '/relay/1'
      },
      {
        "name": 'relay 2',
        "endpoint": '/relay/2'
      },
      {
        "name": 'relay 3',
        "endpoint": '/relay/3'
      }
    ],
    "ANALOGS": [
      {
        "name": 'analog 1',
        "endpoint": '/analog/1'
      },
      {
        "name": 'analog 2',
        "endpoint": '/analog/2'
      },
      {
        "name": 'analog 3',
        "endpoint": '/analog/3'
      }
    ],
    "INPUTS": [
      {
        "name": 'input 1',
        "endpoint": '/input/1'
      },
      {
        "name": 'input 2',
        "endpoint": '/input/2'
      },
      {
        "name": 'input 3',
        "endpoint": '/input/3'
      }
    ]
    })