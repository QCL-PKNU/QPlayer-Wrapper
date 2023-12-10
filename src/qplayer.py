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

current_dir = os.getcwd()

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

        print(json.dumps(json_data, indent=2))

    except Exception as ex:
        print(ex)

def mk_qasm_file(_qasm_code):
    tmp_dir = tempfile.mkdtemp(prefix='tmp_QuantumCircuit')
    qasm_file_path = os.path.join(tmp_dir, 'QuantumCircuit.qasm')
    
    with open(qasm_file_path, 'w') as qasm_file:
        qasm_file.write(_qasm_code)

    return qasm_file_path


import atexit

@atexit.register
def cleanup_temp_dir():
    temp_dir = os.path.join(current_dir, 'tmp_QuantumCircuit')
    if os.path.isdir(temp_dir):
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            os.unlink(file_path)
        os.rmdir(temp_dir)