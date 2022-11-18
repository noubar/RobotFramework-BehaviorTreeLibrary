*** Settings ***
Library  Collections
Library  BehaviorTreeLibrary

*** Variables ***
${k0}   ${0}
${k1}   ${0}
${k2}   ${0}
${f0}   ${0}
${f1}   ${0}
${f2}   ${0}
${dummyArg1}  dummy1
${dummyArg2}  dummy2

*** Keywords ***
k0
    # Log To Console  I am the k0 on execution
    ${k0}   Set Variable  ${${k0}+1}
    Set Test Variable    ${k0}

k1
    [Arguments]  ${dummy1}
    # Log To Console  I am the k1 on execution and my dummy argument is ${dummy1}
    ${k1}   Set Variable  ${${k1}+1}
    Set Test Variable    ${k1}
    ${dummyArg1}  Set Variable  ${dummy1}
    Set Test Variable    ${dummyArg1}

k2
    [Arguments]  ${dummy1}  ${dummy2}
    # Log To Console  I am the k2 on execution and my dummy arguments are ${dummy1}, ${dummy2}
    ${k2}   Set Variable  ${${k2}+1}
    Set Test Variable    ${k2}
    ${dummyArg1}  Set Variable  ${dummy1}
    ${dummyArg2}  Set Variable  ${dummy2}
    Set Test Variable    ${dummyArg1}
    Set Test Variable    ${dummyArg2}

f0
    # Log To Console  I am the f0 and i am going to fail
    ${f0}   Set Variable  ${${f0}+1}
    Set Test Variable    ${f0}
    Fail  f0 has failed

f1
    [Arguments]  ${dummy1}
    # Log To Console  I am the f1 my dummy argument is ${dummy1} and i am going to fail
    ${f1}   Set Variable  ${${f1}+1}
    Set Test Variable    ${f1}
    ${dummyArg1}  Set Variable  ${dummy1}
    Set Test Variable    ${dummyArg1}
    Fail  f1 has failed

f2
    [Arguments]  ${dummy1}  ${dummy2}
    # Log To Console  I am the f2 my dummy arguments are ${dummy1},${dummy2} and i am going to fail
    ${f2}   Set Variable  ${${f2}+1}
    Set Test Variable    ${f2}
    ${dummyArg1}  Set Variable  ${dummy1}
    ${dummyArg2}  Set Variable  ${dummy2}
    Set Test Variable    ${dummyArg1}
    Set Test Variable    ${dummyArg2}
    Fail  f2 has failed

*** Test Cases ***
# Tree functionality test
Test Depth 1 With Args
    # Execution
    One Should Pass
    ...  -  f0
    ...  -  f1  1
    ...  -  K1  2
    ...  -  f1  3
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${f0}    ${1}
    Should Be Equal As Integers    ${f1}    ${1}
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  2

Test Depth 1 With Args Fail Expected
    Run Keyword And Expect Error  The tree has failed.
    ...  All Should Pass
    ...  -  f0
    ...  -  f1  1
    ...  -  K1  2
    # Validation
    Should Be Equal As Integers    ${f0}    ${1}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Integers    ${k1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  dummy1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

Test Depth 1 With Args Keyword Not Found Expected
    Run Keyword And Expect Error  No keyword with name 'false keyword' found.
    ...  One Should Pass
    ...  -  False Keyword  1
    ...  -  f1  2
    ...  -  K1  3
    # Validation
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Integers    ${k1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  dummy1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

Test Depth 2 Without Args
    One Should Pass
    ...  -  All Should Pass
    ...  -  -  k1  1
    ...  -  -  k2  2  3
    ...  -  One Should Pass
    ...  -  -  f1  4
    ...  -  -  k2  5  6
    ...  -  f1  7
    # Validation
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k2}    ${1}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  2
    Should Be Equal As Strings     ${dummyArg2}  3

Test Depth 2 With And Without Args
    One Should Pass
    ...  -  K1  1
    ...  -  k2  2  3
    ...  -  k0
    ...  -  k0
    ...  -  All Should Pass
    ...  -  -  f1  4
    ...  -  -  K1  5
    ...  -  -  Fail  fail2
    ...  -  f1  6
    # Validation
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k2}    ${0}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

Test Depth 3 Mix Args
    All Should Pass
    ...  -  k2  1  2
    ...  -  K1  3
    ...  -  k0
    ...  -  k0
    ...  -  One Should Pass
    ...  -  -  All Should Pass
    ...  -  -  -  K1  4
    ...  -  -  -  k2  5  6
    ...  -  -  f1  7
    ...  -  K1  8
    # Validation
    Should Be Equal As Integers    ${k2}    ${2}
    Should Be Equal As Integers    ${k1}    ${3}
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  8
    Should Be Equal As Strings     ${dummyArg2}  6

Test Depth 4 Mix Args
    One Should Pass
    ...  -  K1  1
    ...  -  k2  2  3
    ...  -  All Should Pass
    ...  -  -  One Should Pass
    ...  -  -  -  f1  4
    ...  -  -  -  K1  5
    ...  -  -  -  All Should Pass
    ...  -  -  -  -  f1  6
    ...  -  -  -  -  k2  7  8
    ...  -  -  Fail  fail2
    ...  -  f1  9
    # Validation
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k2}    ${0}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

Test Depth 4 Gets Only Deeper
    One Should Pass
    ...  -  k2  1  2
    ...  -  k0
    ...  -  All Should Pass
    ...  -  -  One Should Pass
    ...  -  -  -  f1  3
    ...  -  -  -  K1  4
    ...  -  -  -  All Should Pass
    ...  -  -  -  -  f1  5
    ...  -  -  -  -  k2  6  7
    # Validation
    Should Be Equal As Integers    ${k2}    ${1}
    Should Be Equal As Integers    ${k1}    ${0}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  1
    Should Be Equal As Strings     ${dummyArg2}  2

Test Depth 5 Mix Args
    All Should Pass
    ...  -  One Should Pass
    ...  -  -  f1  1
    ...  -  -  f2  2  3
    ...  -  -  All Should Pass
    ...  -  -  -  One Should Pass
    ...  -  -  -  -  f1  4
    ...  -  -  -  -  K1  5
    ...  -  -  -  -  All Should Pass
    ...  -  -  -  -  -  k1  6
    ...  -  -  -  -  -  k2  7  8
    ...  -  -  -  Log  i am a dummy log
    ...  -  -  f1  9
    ...  -  One Should Pass
    ...  -  -  K1  10
    ...  -  -  K1  11

    # Validation
    Should Be Equal As Integers    ${k1}    ${2}
    Should Be Equal As Integers    ${k2}    ${0}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Integers    ${f1}    ${2}
    Should Be Equal As Strings     ${dummyArg1}  10
    Should Be Equal As Strings     ${dummyArg2}  3

Mix BT With Robot Keywrods
    # Log To Console  I am executed before bt
    k0
    One Should Pass
    ...  -  K1  1
    ...  -  k2  2  3
    # Log To Console  I am executed after bt
    k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k2}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

# Test Depth 1 And 2 And 1 Mix Args reducible
#     One Should Pass
#     ...  -  a  arg1  arg2
#     ...  -  b  arg1
#     ...  -  c
#     ...  -  d
#     ...  -  One Should Pass
#     ...  -  -  f1
#     ...  -  -  k3
#     ...  -  -  Fail  fail2
#     ...  -  f1

Syntax Error Extra Dashes Ignored
    One Should Pass
    ...  -  K1  1
    ...  -  k2  2  3
    ...  -  One Should Pass
    ...  -  -  f1  4
    ...  -  -  K1  5
    ...  -  -  Fail  fail2
    ...  -  f1  6
    ...  -  -  -  
    # Validation
    Should Be Equal As Integers    ${k1}    ${1}
    Should Be Equal As Integers    ${k2}    ${0}
    Should Be Equal As Integers    ${k0}    ${0}
    Should Be Equal As Integers    ${f1}    ${0}
    Should Be Equal As Strings     ${dummyArg1}  1
    Should Be Equal As Strings     ${dummyArg2}  dummy2

# Syntax Error Tests
Syntax Error Middle With Arg
    Run Keyword And Expect Error  SyntaxError: Between k2 first_argument_k2 second_argument_k2 One Should Pass and f1 first_argument_f1.
    ...  One Should Pass
    ...  -  k2  first_argument_k2  second_argument_k2
    ...  -  K1  first_argument_k1
    ...  -  K1  first_argument_k1
    ...  -  k2  first_argument_k2  second_argument_k2
    ...     One Should Pass
    ...  -  -  f1  first_argument_f1
    ...  -  -  f1  first_argument_f1
    ...  -  -  Fail  fail2
    ...  -  f1  first_argument_f1

Syntax Error Middle Without Arg
    Run Keyword And Expect Error  SyntaxError: Between k2 first_argument_k2 second_argument_k2 One Should Pass and f0.
    ...  One Should Pass
    ...  -  k2  first_argument_k2  second_argument_k2
    ...  -  K1  first_argument_k1
    ...  -  K1  first_argument_k1
    ...  -  k2  first_argument_k2  second_argument_k2
    ...     One Should Pass
    ...  -  -  f0
    ...  -  -  K1  first_argument_k1
    ...  -  -  Fail  fail2
    ...  -  f1  first_argument_f1

Syntax Error Begining With Arg
    Run Keyword And Expect Error  SyntaxError: Between selector and k2 first_argument_k2 second_argument_k2.
    ...  One Should Pass
    ...  -  -  k2  first_argument_k2  second_argument_k2
    ...  -  k2  first_argument
    ...  -  k0
    ...  -  One Should Pass
    ...  -  -  f1  first_argument_f1
    ...  -  -  K1  first_argument_k1
    ...  -  -  Fail  fail2
    ...  -  f1  first_argument_f1

Syntax Error Begining Without Arg
    Run Keyword And Expect Error  SyntaxError: Between selector and k0.
    ...  One Should Pass
    ...  -  -  k0
    ...  -  k2  first_argument
    ...  -  k0
    ...  -  One Should Pass
    ...  -  -  f1  first_argument_f1
    ...  -  -  K1  first_argument_k1
    ...  -  -  Fail  fail2
    ...  -  f1  first_argument_f1


Syntax Error Ending With Arg
    Run Keyword And Expect Error  SyntaxError: Between Fail fail2 and f1 first_argument_f1.
    ...  One Should Pass
    ...  -  k2  first_argument  second_argument
    ...  -  K1  first_argument_k1
    ...  -  K1  first_argument_k1
    ...  -  k2  first_argument
    ...  -  One Should Pass
    ...  -  -  f1  first_argument_f1
    ...  -  -  K1  first_argument_k1
    ...  -  -  Fail  fail2
    ...  -  -  -  f1  first_argument_f1

Syntax Error Ending Without Arg
    Run Keyword And Expect Error  SyntaxError: Between Fail fail2 and f0.
    ...  One Should Pass
    ...  -  k2  first_argument_k2  second_argument_k2
    ...  -  K1  first_argument_k1
    ...  -  K1  first_argument_k1
    ...  -  k2  first_argument
    ...  -  One Should Pass
    ...  -  -  f1  first_argument_f1
    ...  -  -  K1  first_argument_k1
    ...  -  -  Fail  fail2
    ...  -  -  -  f0
