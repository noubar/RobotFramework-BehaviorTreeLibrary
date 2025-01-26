#!/bin/bash

cleanup() {
    rm -rf build
    rm -rf dist
    rm -rf keywords
    rm -rf src/robotframework_BehaviorTreeLibrary.egg-info
}

dependency() {
    python3 -m pip install --upgrade pip setuptools wheel
    pip3 install -r requirements-dev.txt
}

build() {
    cleanup
    dependency
    python3 setup.py sdist bdist_wheel
    python3 libdoc.py
}

install() {
    build
    pip install .
}

test_unit() {
    cd atests
    python3 Treenator_unit_test.py
    cd ..
}

test_robot() {
    cd atests
    robot --outputdir ../result/ .
    cd ..
}

test() {
    install
    test_unit
    result=$?
    mkdir -p result
    test_robot
    if [ $result -eq 0 ]; then
        result=$?
    fi
    rebot --name ATests --outputdir result -x rebot_xunit.xml result/output.xml
}

if [ ! -z "$1" ]; then
  $1
fi
