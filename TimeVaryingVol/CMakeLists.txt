cmake_minimum_required(VERSION 3.10)
project(HistoricalVol)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

set(NUMCPP_DIR "../../")
set(SOURCE_FILE HistoricalVol.cpp)
set(EXECUTABLE_NAME historical_vol)

add_executable(${EXECUTABLE_NAME} ${SOURCE_FILE})
target_include_directories(${EXECUTABLE_NAME} PRIVATE ${NUMCPP_DIR})

