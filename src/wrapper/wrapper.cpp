#include <pybind11/pybind11.h>
#include "main.h"

namespace py = pybind11;

PYBIND11_MODULE(qplayer, m){
    m.def("main", &main, "");
}