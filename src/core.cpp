#include <pybind11/pybind11.h>
#include <filesystem>
#include <unistd.h>
#include <cstdlib>

#include "QASMparser.h"
#include "main.cpp"

void _set_value(char _f_in[], char _f_out[], char _j_out[], int _shots){
    strcpy(f_in,_f_in);
    strcpy(f_out,_f_out);
    strcpy(j_out,_j_out);
    shots = int(_shots);

    is_json = 1;
}

void _convertQASM(void){
    FILE *in = NULL;
	FILE *out = NULL;

	in = fopen(f_in, "rt");
	out = fopen(f_qasm, "wt");

    // if (homeDir == nullptr) {
    //     std::cout << "Missing Home path" << std::endl;
    // }

    char line[1024] = "";
    char tmp[] = "include \"qelib1.inc\";\n";
    char fath_qelib[1024];

    // Combination of qelib1.inc file paths
    std::filesystem::path executablePath = __FILE__;
    executablePath = executablePath.parent_path();
    std::string parentDirectory = executablePath.parent_path().parent_path().string();

    snprintf(fath_qelib, sizeof(fath_qelib), "include \"%s/qplayer_wrapper/QPlayer/qasm/qelib1.inc\";", parentDirectory.c_str());
    
	while(!feof(in)) {
		fgets(line, sizeof(line), in);

        if(strcmp(line, tmp) == 0){
            fprintf(out, "%s\n", fath_qelib);
        }else{
            fprintf(out, "%s\n", line);
        }
	}
	fprintf(out, "\n");

	fclose(in);
	fclose(out);
}

/**
 * @brief Wrapper function for main QPlayer operations.
 *
 * This function calls _set_value, _convertQASM, and runQASM(in main.cpp) functions.
 * It catches exceptions and sets a Python runtime error if an exception occurs.
 *
 * @param _f_in Input QASM file path.
 * @param _f_out Output result file path.
 * @param _j_out Output JSON file path.
 * @param _shots Number of shots for QPlayer.
 */
void main_wra(char _f_in[], char _f_out[], char _j_out[], int _soths){
    try {
        _set_value(_f_in,_f_out,_j_out,_soths);
        _convertQASM();
        runQASM();
    } catch (const std::exception& e) {
        PyErr_SetString(PyExc_RuntimeError, e.what());
    }
}
namespace py = pybind11;

PYBIND11_MODULE(qplayer_wra, m) {
    m.def("main_wra", &main_wra, "Description of main_wra function",
      py::arg("_f_in"), py::arg("_f_out"), py::arg("_j_out"), py::arg("_soths"));
}
