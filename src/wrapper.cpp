#include <pybind11/pybind11.h>
#include "main.cpp"

namespace py = pybind11;

PYBIND11_MODULE(qplayer, m) {
    m.def("main", []&main , "");
}