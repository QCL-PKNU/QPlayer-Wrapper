cmake_minimum_required(VERSION 3.4...3.18)
project(qplayer)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(pybind11)
pybind11_add_module(qplayer QPlayer/qasm/main.cpp)


# Include directories for header files
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/core/include)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(qplayer
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
