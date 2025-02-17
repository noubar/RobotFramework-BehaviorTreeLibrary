# BehaviorTreeLibrary

This project is a `proof of concept` implementation to integrate behavior trees in Robot Framework. The goal of this project is to test the feasibility of using behavior trees in automation testing and to evaluate whether it can improve test automation in Robot Framework. The results have been published in our 2023 ISSTA paper [`RobotBT: Behavior-Tree-Based Test-Case Specification for the Robot Framework`](https://doi.org/10.1145/3597926.3604924), which is available as open access publication.

```
@inproceedings{PAB2023,
  title = {RobotBT: Behavior-Tree-Based Test-Case Specification for the Robot Framework},
  author = {Sven Peldszus and Noubar Akopian and Thorsten Berger},  
  doi = {10.1145/3597926.3604924},
  year = {2023},
  booktitle = {Proceedings of the ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA)},
  pages = {1503–1506},
  note = {Open Access},
}
```

The [`BehaviorTreeLibrary`](https://github.com/noubar/RobotFramework-BehaviorTreeLibrary) is a Python-based library for the [Robot Framework](https://robotframework.org/) that provides behavior tree nodes as Robot Framework keywords to add the behavior tree functionalities into Robot Framework.
The library officially supports Python >= 3.7 and currently cannot be installed using pip.


## Overview

Behavior trees are a structured way to represent complex, decision-based workflows. By breaking down automation logic into smaller, manageable tasks and decision points, behavior trees can make automation code more maintainable and easier to understand.

This project will be used to evaluate the benefits and drawbacks of using behavior trees in Robot Framework. It includes a sample behavior tree library that can be used to define and execute behavior trees in Robot Framework, as well as sample test cases that use the behavior tree library.

## Requirements

- Python 3.x
- Robot Framework

## Installation

To install the library, run the following command:

```
./runner.bat install
```
or 
```
./runner.sh install
```

## Usage

After installing the library, you can import it into your Robot Framework test suite using the following line:

```
*** Settings ***
Library  BehaviorTreeLibrary
```

### Supported BT Nodes

The `BehaviorTreeLibrary` supports the following Behavior Tree (BT) nodes:

- Selector = Fallback = One Should Pass
- Sequence = All Should Pass

### Supported BT Decorators

The `BehaviorTreeLibrary` supports the following Behavior Tree (BT) decorators:

- Repeat Until All Branches Are Executed
- Repeat Until All Lines Are Executed
- Repeat Until All Branches Are Passed
- Repeat Until Branches Are Executed  \<min_percentage>
- Repeat Until Lines Are Executed  \<min_percentage>
- Repeat Until Branches Are Passed  \<min_percentage>
- Repeat Until Lines Are Passed  \<min_percentage>
- All Branches Should Be Executed
- All Lines Should Be Executed
- All Branches Should Be Passed
- Branches Should Be Executed  \<min_percentage>
- Lines Should Be Executed  \<min_percentage>
- Branches Should Be Passed  \<min_percentage>
- Lines Should Be Passed  \<min_percentage>

## License

The `BehaviorTreeLibrary` is released under the [MIT License](https://opensource.org/licenses/MIT).

## Conclusion

By implementing a behavior tree library integration in Robot Framework, this project demonstrates the potential benefits of using behavior trees in automation testing. By evaluating the performance and maintainability of this integration, you can determine whether behavior trees are a good fit for your test automation needs.

## Examples

- [BehaviorTreeLibrary-Tests](https://github.com/noubar/BehaviorTreeLibrary-Tests).
