#include <pybind11/pybind11.h>
#include <filesystem>
#include <cstdlib>

#include "QASMparser.h"
#include "main.cpp"

const char* homeDir = getenv("HOME");

void set_value(char _f_in[], char _f_out[], char _j_out[]){
    strcpy(f_in,_f_in);
    strcpy(f_out,_f_out);
    strcpy(j_out,_j_out);

    is_json = 1;
}

void _convertQASM(void){
    FILE *in = NULL;
	FILE *out = NULL;

	in = fopen(f_in, "rt");
	out = fopen(f_qasm, "wt");

    if (homeDir == nullptr) {
        std::cout << "Missing Home path" << std::endl;
    }

    char line[1024] = "";
    char tmp[] = "include \"qelib1.inc\";\n";
    char fath_qelib[1024];
    snprintf(fath_qelib, sizeof(fath_qelib), "include \"%s/qplayer_wrapper/QPlayer/qasm/qelib1.inc\";", homeDir);
    
	cout << "\"" <<homeDir << "\"" << "// [] " << fath_qelib << endl;
    
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

namespace py = pybind11;

PYBIND11_MODULE(qplayer_wra, m) {
    m.def("set_value",&set_value,"");
    m.def("_convertQASM",&_convertQASM,"");
    m.def("runQASM",&runQASM,"");
    m.def("genStatJson",&genStatJson,"",py::arg("*stat"));
}
