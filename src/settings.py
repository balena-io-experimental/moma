def defaults():
    return({
    "POLL_INT": 3000,
    "RELAYS": [
      {
        "name": 'relay 1',
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
    "OUTPUTS": [
      {
        "name": 'output 1',
        "endpoint": '/output/1'
      },
      {
        "name": 'output 2',
        "endpoint": '/output/2'
      },
      {
        "name": 'output 3',
        "endpoint": '/output/3'
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
