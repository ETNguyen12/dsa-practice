#!/usr/bin/env bash
# Compile and run the Java drill. Usage: ./run_java.sh
set -e
javac Drill.java Start.java
java Start
