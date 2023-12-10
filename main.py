from qiskit import *
from src import RunQPlayer

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure(0,0)
qc.measure(1,1)

qasm = qc.qasm()

print(type(qasm))