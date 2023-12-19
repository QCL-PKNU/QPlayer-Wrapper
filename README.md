# QPlayer Wrapper

QPlayer Wrapper is a Python interface that facilitates the utilization of the ETRI-provided QPlayer within a Python environment. This README provides a step-by-step guide on how to set up your environment to seamlessly integrate and use the QPlayer Wrapper.

---------------

## OS environment

- CenOS 7.x or higher
- Ubuntu 20.x or higher

## Depencencies

- gcc and g++ capable of C++11 standard
- make 3.x or higher
- pip 23.x or higher
- pybind11 2.x or higher
- scikit-build 0.17 or higher


## Installation

Follow the instructions below to set up your environment for using the QPlayer Wrapper.

### Clone QPlayer Repository
```bach
git clone https://github.com/eQuantumOS/QPlayer.git
```

### Clone pybind11 Repository
```bach
git clone https://github.com/pybind/pybind11.git
```

## Install (pip package-management system)
```bash
apt update & apt install pip
```

### Install QPlayer Wrapper
```bach
cd QPlayer-Wrapper
pip install -r requirements.txt
pip install .
```

## Usage

### Test
```python
python3 -m unittest
```

### Run main.py

```bash
python3 main.py
```

### Sample code (main.py)
```python
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qplayer import executeQASM

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.y(0)
qc.cx(0, 1)
qc.measure_all()

qasm = qc.qasm()

result = executeQASM(qasm, 1080)

figure = plot_histogram(result.get_counts())
figure.savefig('result.png')
```