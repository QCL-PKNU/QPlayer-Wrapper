import unittest
from qiskit import QuantumCircuit
from qplayer import executeQASM

class GroverTest(unittest.TestCase):

    def test_grover(self):
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

        result = executeQASM(qc.qasm(), shots=1024)
        counts = result.get_counts()

        # check if counts is not empty
        self.assertTrue(counts)
