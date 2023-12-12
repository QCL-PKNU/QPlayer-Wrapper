from qiskit import *
from src import RunQPlayer
from qplayer_wra import *

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)
qc.y(0)
qc.cx(0, 1)
qc.measure_all()

qasm = qc.qasm()

result = executeQASM(qasm, 1080)
# result = RunQPlayer(qasm, 1080)
print(result)