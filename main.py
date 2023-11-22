from qiskit import QuantumCircuit
from qplayer import RunQPlayer, RunQiskitOnQPlayer

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure(0,0)
qc.measure(1,1)

qasm = qc.qasm()

# result is dictionary = json
result = RunQPlayer(qasm, run=1080)
# or
result = RunQiskitOnQPlayer(qc, run=1080)