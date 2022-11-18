*** Settings ***
Library  Collections
Library  BehaviorTreeLibrary

*** Variables ***
${v0}   ${-1}
${v1}   ${-1}
${v2}   ${-1}


*** Keywords ***
k0
    # Log To Console  I am the k0 on execution
    [Return]  ${0}

k1
    [Arguments]  ${dummy1}
    # Log To Console  I am the k1 on execution and my dummy argument is ${dummy1}
    [Return]  ${1}


k2
    [Arguments]  ${dummy1}  ${dummy2}
    # Log To Console  I am the k2 on execution and my dummy arguments are ${dummy1}, ${dummy2}
    [Return]  ${2}

All Should Equal 0
    Should Be Equal As Integers    ${v0}    ${0}
    Should Be Equal As Integers    ${v1}    ${0}
    Should Be Equal As Integers    ${v2}    ${0}


*** Test Cases ***
# Tree functionality test
Test Global Assigner Keyword
    # Execution
    All Should Pass
    ...  -  Assign Return As Global Variable   $v0   k0
    ...  -  Assign Return As Global Variable   $v1   k1  dummy1
    ...  -  Assign Return As Global Variable   $v2   k2  dummy1  dummy2
    # Validation
    Should Be Equal As Integers    ${v0}    ${0}
    Should Be Equal As Integers    ${v1}    ${1}
    Should Be Equal As Integers    ${v2}    ${2}

Test Suite Assigner Keywords
    Should Be Equal As Integers    ${v0}    ${0}
    Should Be Equal As Integers    ${v1}    ${1}
    Should Be Equal As Integers    ${v2}    ${2}
    # Execution
    All Should Pass
    ...  -  Assign Return As Suite Variable   $v0   k0
    ...  -  Assign Return As Suite Variable   $v1   k0
    ...  -  Assign Return As Suite Variable   $v2   k0
    # Validation
    All Should Equal 0

Test Test Assigner Keywords
    All Should Equal 0
    # Execution
    All Should Pass
    ...  -  Assign Return As Test Variable   $v0   k0
    ...  -  Assign Return As Test Variable   $v1   k1  dummy1
    ...  -  Assign Return As Test Variable   $v2   k2  dummy1  dummy2
    # Validation
    Should Be Equal As Integers    ${v0}    ${0}
    Should Be Equal As Integers    ${v1}    ${1}
    Should Be Equal As Integers    ${v2}    ${2}

Test Scope Assigner Keywords
    Should Be Equal As Integers    ${v0}    ${0}
    Should Be Equal As Integers    ${v1}    ${0}
    Should Be Equal As Integers    ${v2}    ${0}
    # Execution
    All Should Pass
    ...  -  Assign Return As Scope Variable   $v0   k0
    ...  -  Assign Return As Scope Variable   $v1   k1  dummy1
    ...  -  Assign Return As Scope Variable   $v2   k2  dummy1  dummy2
    ...  -  Should Be Equal As Integers    \${v0}    \${0}
    ...  -  Should Be Equal As Integers    \${v1}    \${1}
    ...  -  Should Be Equal As Integers    \${v2}    \${2}
    All Should Equal 0