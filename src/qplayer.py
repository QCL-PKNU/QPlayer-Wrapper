#######################################################################
#   QuantumCircuit
#   
#   Created: 2023. 12. 02
#   Last Modified: 2023. 12. 02
#
#   Authors:
#      Nagyeong Choi (choi2019@pukyong.ac.kr)
#
#   High Performance Computing Laboratory (hpcl.pknu.ac.kr)
#######################################################################
import qplayer_wra

def RunQPlayer(run:int = None):
    return "hi"
    try:
        output_path = "../QPlayer/release/bin/examples/test.qasm"
        input_path = "./simulation.res"
        json_path = "./task.json"
        qplayer_wra.set_value(output_path,input_path,json_path)
    # qplayer_wra._convertQASM()
    # qplayer_wra._runQASM()
    # # test = "-i examples/test.qasm -o ./log/simulation.res"
    # # qasm_path = 
    except Exception as ex:
        print(ex)

#호출 예시
RunQPlayer()