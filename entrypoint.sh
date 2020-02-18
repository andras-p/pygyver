#!/bin/bash

# exit on error
set -e

# print command
set -ex

# colours
export TERM=xterm-256color

DATE=`/bin/date +%Y-%m-%d-%H:%M:%S`

# change to source code directory
cd src/

if [ "$1" == "pygyver-tests" ]; then
    echo "Starting "$2" tests"
    tests/entrypoint-tests.sh "$2"
    echo "Finished "$2" tests."
    exit $?
fi

if [ "$1" == "waxit-tests" ]; then
    echo "Starting "$2" tests"
    tests/entrypoint-tests.sh "$2"
    echo "Finished "$2" tests."
    exit $?
fi
