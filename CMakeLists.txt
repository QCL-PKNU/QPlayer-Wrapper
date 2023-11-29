cmake_minimum_required(VERSION 3.4...3.18)
project(qplayer_wrapper)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(pybind11)
# pybind11_add_module(qplayer_wrapper QPlayer/core/sre/timer.cpp)
pybind11_add_module(dump QPlayer/core/sre/dump.cpp)
pybind11_add_module(experimental QPlayer/core/sre/experimental.cpp)
pybind11_add_module(gate QPlayer/core/sre/gate.cpp)
pybind11_add_module(misc QPlayer/core/sre/misc.cpp)
pybind11_add_module(precision QPlayer/core/sre/precision.cpp)
pybind11_add_module(register QPlayer/core/sre/register.cpp)
pybind11_add_module(state QPlayer/core/sre/state.cpp)
pybind11_add_module(timer QPlayer/core/sre/timer.cpp)

##헤더 찾기
# Include directories for header files
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(qplayer_wrapper
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
