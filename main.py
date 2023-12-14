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
