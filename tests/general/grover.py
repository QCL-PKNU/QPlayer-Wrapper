from qiskit import *
from src import RunQPlayer

def grover():
    qc = QuantumCircuit(5, 5)
    qc.h(0)
    qc.h(1)
    qc.s(0)
    qc.s(1)
    qc.h(0)
    qc.cx(0, 1)
    qc.h(1)
    qc.s(0)
    qc.s(1)
    qc.h(0)
    qc.h(1)
    qc.x(0)
    qc.x(1)
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.h(1)
    qc.measure(0,0)
    qc.measure(1,1)

    qasm = qc.qasm()

    result = RunQPlayer(qasm, run=1080)

# run
grover()