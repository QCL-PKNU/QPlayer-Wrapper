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
```bach

```
