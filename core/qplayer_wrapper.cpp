#include <pybind11/pybind11.h>
#include "dump.h"
#include "experimental.h"
#include "gate.h"
#include "misc.h"
#include "register.h"
#include "state.h"
#include "timer.h"

namespace py = pybind11;

PYBIND11_MODULE(qplayer_wrapper, m) {
    // py::class_<QubitDelimiter>(m, "QubitDelimiter")
    py::class_<QRegister>(m, "QRegister");
    m.def("dump", &dump, "Dump function",
        py::arg("QReg"),
        py::arg("msg") = py::str(""),
        py::arg("begin") = 0,
        py::arg("end") = 0,
        py::arg("qubits") = py::list()
    );
    m.def("experimental", &experimental, "experimental");
    m.def("gate", &gate, "gate");
    m.def("misc", &misc, "misc");
    m.def("register", &register, "register");
    m.def("state", &state, "state");
    m.def("timer", &timer, "timer");

}