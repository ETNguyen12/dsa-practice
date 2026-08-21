#!/usr/bin/env bash
# Compile and run the C++ drill. Usage: ./run_cpp.sh
set -e
g++ -std=c++17 -O2 drill.cpp -o drill
./drill
