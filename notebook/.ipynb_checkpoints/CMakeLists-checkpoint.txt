cmake_minimum_required(VERSION 3.0.0)
project(notebook_mpi VERSION 0.1.0)

include(CTest)
enable_testing()

find_package(MPI REQUIRED)
include_directories(${MPI_CXX_INCLUDE_PATH})

add_executable(mpi main.cpp)
target_link_libraries(mpi ${MPI_CXX_LIBRARIES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
