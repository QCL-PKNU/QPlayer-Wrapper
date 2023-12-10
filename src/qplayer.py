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

def RunQPlayer(_qasm_code:str, _shots:int = 1):
    # try:
    # file_path = mk_qasm_file(_qasm_code) 
    print(_qasm_code)
    input_path = "../QPlayer/release/bin/examples/test.qasm"
    output_path = "../simulation.res"
    json_path = "../task.json"
    # qplayer_wra.main_wra(file_path,output_path,json_path,_shots)
    # except Exception as ex:
        # print(ex)

def mk_qasm_file(_qasm_code):
    tmp_dir = tempfile.mkdtemp(prefix='project_tmp')
    qasm_file_path = os.path.join(tmp_dir, 'QuantumCircuit.qasm')
    
    with open(qasm_file_path, 'w') as qasm_file:
        qasm_file.write(_qasm_code)

    return qasm_file_path

#호출 예시
RunQPlayer()