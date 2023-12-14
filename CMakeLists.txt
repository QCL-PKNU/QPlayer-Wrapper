cmake_minimum_required(VERSION 3.4...3.18)
project(qplayer)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(OpenMP REQUIRED)

# Add the path to pybind11
add_subdirectory(pybind11)

# Add a new executable target for initializing Token::KindNames
# add_executable(TokenInitializer src/TokenInitializer.cpp QPlayer/qasm/src/QASMtoken.cpp)
# target_link_libraries(TokenInitializer PRIVATE QASMtoken)
set(QPLAYER_SOURCES
    qplayer/core.cpp
    qplayer/qelib1.inc
    QPlayer/qasm/src/QASMparser.cpp
    QPlayer/qasm/src/QASMscanner.cpp
    QPlayer/qasm/src/QASMtoken.cpp
    QPlayer/core/src/gate.cpp
    QPlayer/core/src/register.cpp
    QPlayer/core/src/timer.cpp
    QPlayer/core/src/misc.cpp
    QPlayer/core/src/dump.cpp
    QPlayer/core/src/experimental.cpp
    QPlayer/core/src/state.cpp
)
pybind11_add_module(qplayer_wra ${QPLAYER_SOURCES})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/qasm
                    ${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/qasm/include
                    ${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/release/include
                    ${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/core/include
)
# Add the following line to disable the warning about converting string literals to char*
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-write-strings -lstdc++fs -std=c++17")

# target_include_directories(qplayer_wra PRIVATE
#     /pybind11/include/pybind11  # pybind11 헤더 파일이 있는 경로
# )
# Create a library from the source files
# add_library(qplayer MODULE src/wrapper.cpp QPlayer/qasm/main.cpp)

# target_include_directories(qplayer_wra PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src2)
# target_link_libraries(qplayer_wra PRIVATE pybind11::module)

# Link the Python library
target_link_libraries(qplayer_wra PRIVATE Python3::Python)
target_link_libraries(qplayer_wra PRIVATE OpenMP::OpenMP_CXX)