import unittest
from qplayer.run_qplayer import executeQASM

class RunQPlayerTest(unittest.TestCase):

    def test_executeQASM(self):
        # Test case 1: Valid QASM code and shots
        qasm_code = """
            OPENQASM 2.0;
            include "qelib1.inc";

            qreg q[1];
            creg c[1];

            h q;

            measure q -> c;
        """
        shots = 1080
        result = executeQASM(qasm_code, shots)
        self.assertIsNotNone(result)
        self.assertEqual(result.simulation_results.total_shots, shots)