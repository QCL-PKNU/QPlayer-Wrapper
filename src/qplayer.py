#######################################################################
#   QuantumCircuit
#   
#   Created: 2023. 12. 02
#   Last Modified: 2023. 12. 10
#
#   Authors:
#      Nagyeong Choi (choi2019@pukyong.ac.kr)
#
#   High Performance Computing Laboratory (hpcl.pknu.ac.kr)
#######################################################################

import tempfile
import os
import qplayer_wra
import json

current_dir = os.getcwd()

## RunQPlayer function executes QPlayer with the given QASM code.
# @param qasm_code: The QASM code to be executed.
# @param run: The number of runs for the QuantumCircuit.
# @param file_name: The base name for output(.res) and JSON files.
# @return: The JSON-formatted result of QPlayer execution.
def RunQPlayer(qasm_code:str = None, run:int = 1, file_name:str = 'QuantumCircuit'):
    try: 
        if(qasm_code is None):
            return
        
        file_path = mk_qasm_file(qasm_code)
        # test_input_path = "../QPlayer/release/bin/examples/test.qasm"
        output_path = f"{current_dir}/{file_name}.res"
        json_path = f"{current_dir}/{file_name}.json"
        shots = run

        qplayer_wra.main_wra(file_path,output_path,json_path,shots)

        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)

        result = json.dumps(json_data, indent=2)

        return result

    except Exception as ex:
        print(ex)

## Creates a temporary QASM file and writes the provided QASM code into it.
# @param _qasm_code: The QASM code to be written into the file.
# @return: The path of the created QASM file.
def mk_qasm_file(_qasm_code):
    tmp_dir = tempfile.mkdtemp(prefix='tmp_QuantumCircuit')
    qasm_file_path = os.path.join(tmp_dir, 'QuantumCircuit.qasm')
    
    with open(qasm_file_path, 'w') as qasm_file:
        qasm_file.write(_qasm_code)

    return qasm_file_path


import atexit

## Cleans up the temporary directory created during the execution.
# Runs on program exit.
@atexit.register
def cleanup_temp_dir():
    temp_dir = os.path.join(current_dir, 'tmp_QuantumCircuit')
    if os.path.isdir(temp_dir):
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            os.unlink(file_path)
        os.rmdir(temp_dir)