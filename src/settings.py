import os

def defaults():
    return({
    "POLL_INT": os.environ.get('POLL_INT'),
	"RELAYS": [ os.environ.get('RELAY1'), os.environ.get('RELAY2'), os.environ.get('RELAY3') ],
    "ANALOGS": [ os.environ.get('ANALOG1'), os.environ.get('ANALOG2'), os.environ.get('ANALOG3') ],
    "INPUTS": [ os.environ.get('INPUT1'), os.environ.get('INPUT2') , os.environ.get('INPUT3') ],
    "OUTPUTS": [ os.environ.get('OUPUT1'), os.environ.get('OUPUT2'), os.environ.get('OUPUT3') ]
	})
