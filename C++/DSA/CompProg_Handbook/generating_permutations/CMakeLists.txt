cmake_minimum_required(VERSION 3.10)
project(MyProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include_directories(include)

# file(GLOB SOURCES "src/*.cpp")

add_executable(next_perm src/next_perm.cpp)
add_executable(recursion src/recursion.cpp)
