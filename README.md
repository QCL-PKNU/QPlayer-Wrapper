# QPlayer Wrapper

This is a wrapper that makes the ETRI-provided QPlayer available in the Python environment.
The README describes how to set up your environment to use the QPlayer Wrapper.

---------------
## Setup

Follow the instructions below to set up your environment for using the QPlayer Wrapper

### Clone QPlayer Wrapper
```bach
git clone https://github.com/Sengthai/qplayer_wrapper.git
```
```bach
cd qplayer_wrapper
```

### Clone QPlayer Repository
```bach
git clone https://github.com/eQuantumOS/QPlayer.git
```

### Clone pybind11 Repository
```bach
git clone https://github.com/pybind/pybind11.git
```

### Install qplayer_wrapper
```bach
pip install .
```

## Usage
### Test code (main.py)
```python
from qiskit import *
from src import RunQPlayer

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cy(0, 1)
qc.rx(2, 0)
qc.measure(0,0)
qc.measure(1,1)

qasm = qc.qasm()

result = RunQPlayer(qasm, run=1080)
print(result)
```
### Result
```bach
{
  "circuit": {
    "used qubits": 2,
    "used gates": 5,
    "gate calls": {
      "U3": 2,
      "H": 1,
      "RX": 1,
      "CX": 1,
      "MEASURE": 3
    }
  },
  "runtime": {
    "total simulation time": 22053,
    "individual gate time": {
      "U3": [
        208,
        105,
        103,
        104
      ],
      "H": [
        8114,
        8114,
        8114,
        8114
      ],
      "RX": [
        60,
        60,
        60,
        60
      ],
      "CX": [
        7092,
        7092,
        7092,
        7092
      ],
      "MEASURE": [
        6579,
        6462,
        0,
        2193
      ]
    }
  },
  "simulation jobs": {
    "max states": 4,
    "final states": 1,
    "used memory": "114.5 MB"
  },
  "system": {
    "OS": {
      "name": "Ubuntu",
      "version": "22.04.3 LTS (Jammy Jellyfish)"
    },
    "CPU": {
      "model": "Intel(R) Xeon(R) Silver 4214R CPU @ 2.40GHz",
      "cores": 48,
      "herz": "3052.007"
    },
    "Memory": {
      "total": "251.5 GB",
      "avail": "239.5 GB"
    }
  }
}
```
