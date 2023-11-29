cmake_minimum_required(VERSION 3.4...3.18)
project(qplayer_wrapper)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(pybind11)
pybind11_add_module(qplayer_wrapper core/qplayer_wrapper.cpp
                                    QPlayer/core/src/dump.cpp 
                                    QPlayer/core/src/experimental.cpp
                                    QPlayer/core/src/gate.cpp 
                                    QPlayer/core/src/misc.cpp
                                    QPlayer/core/src/register.cpp 
                                    QPlayer/core/src/state.cpp
                                    QPlayer/core/src/timer.cpp)

##헤더 찾기
# Include directories for header files
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/QPlayer/core/include)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(qplayer_wrapper
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})

                           # OpenMP 찾기
find_package(OpenMP)

# OpenMP를 찾았다면 사용하도록 설정
if(OpenMP_FOUND)
    # OpenMP 플래그를 컴파일러에 추가
    target_compile_options(qplayer_wrapper PUBLIC ${OpenMP_CXX_FLAGS})

    # OpenMP 라이브러리를 링크
    target_link_libraries(qplayer_wrapper PUBLIC OpenMP::OpenMP_CXX)
else()
    message(WARNING "OpenMP not found. Compiling without OpenMP support.")
endif()
