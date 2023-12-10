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