cmake_minimum_required(VERSION 2.8.9)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
project (sqlogd)
add_executable(sqlogd sqlogd.cpp)
