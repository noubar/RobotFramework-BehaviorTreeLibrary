*** Settings ***
Library  Collections
Library  BehaviorTreeLibrary

*** Variables ***
${k0}   ${0}
${f0}   ${0}
${f1}   ${0}
${f2}   ${0}
${MIN}  ${2}

*** Keywords ***
k0
    [Documentation]  This keyword works as counter by increasing the value of test variable k0 by one.
    ${k0}   Set Variable  ${${k0}+1}
    Set Test Variable    ${k0}

f0
    [Documentation]  This keyword works as a revers time bomb it fails until it reaches the max times of failure.
    ...  max_fail_time = ${MIN}
    ${f0}   Set Variable  ${${f0}+1}
    Set Test Variable    ${f0}
    IF    ${f0} <= ${MIN}
        Fail  f0 has failed
    END

f1
    [Documentation]  This keyword works as a revers time bomb it fails until it reaches the max times of failure.
    ...  max_fail_time = ${MIN}+${10}
    ${f1}   Set Variable  ${${f1}+1}
    Set Test Variable    ${f1}
    IF    ${f1} <= ${${MIN}+${10}}
        Fail  f1 has failed
    END

f2
    [Documentation]  This keyword works as a revers time bomb it fails until it reaches the max times of failure.
    ...  max_fail_time = ${MIN}+${20}
    ${f2}   Set Variable  ${${f2}+1}
    Set Test Variable    ${f2}
    IF    ${f2} <= ${${MIN}+${20}}
        Fail  f2 has failed
    END


*** Test Cases ***
# Tree functionality test
Test Repeat Until All Branches Are Executed
    # Execution
    Repeat Until All Branches Are Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${1}
    Should Be Equal As Integers    ${f0}    ${1}

Test Repeat Until All Lines Are Executed
    # Execution
    Repeat Until All Lines Are Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${1}
    Should Be Equal As Integers    ${f0}    ${1}

Test Repeat Until All Branches Are Passed
    # Execution
    Repeat Until All Branches Are Passed
    ...  One Should Pass
    ...  -  f0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${1}
    Should Be Equal As Integers    ${f0}    ${1}

Test Repeat Until All Lines Are Passed
    # Execution
    Repeat Until All Lines Are Passed
    ...  One Should Pass
    ...  -  f0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${3}

Test Repeat Until All Lines Are Passed Depth 2
    Repeat Until All Lines Are Passed
    ...  One Should Pass
    ...  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  One Should Pass
    ...  -  -  f0
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${24}
    Should Be Equal As Integers    ${f0}    ${12}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${23}

Test Repeat Until All Lines Are Executed Depth 2
    Repeat Until All Lines Are Executed
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  -  One Should Pass
    ...  -  -  -  f0
    ...  -  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${39}
    Should Be Equal As Integers    ${f0}    ${1}
    Should Be Equal As Integers    ${f1}    ${13}
    Should Be Equal As Integers    ${f2}    ${13}

Test Repeat Until All Branches Are Passed Depth 2
    Repeat Until All Branches Are Passed
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  One Should Pass
    ...  -  -  f1
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${35}
    Should Be Equal As Integers    ${f0}    ${0}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${23}

Test Repeat Until All Branches Are Executed Depth 2
    Repeat Until All Branches Are Executed
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  f2
    ...  -  -  One Should Pass
    ...  -  -  -  f2
    ...  -  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f1
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f0
    ...  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${22}
    Should Be Equal As Integers    ${f0}    ${12}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${24}

Test Repeat Until Lines Are Passed Full Iteration
    Repeat Until Lines Are Passed  100
    ...  One Should Pass
    ...  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  One Should Pass
    ...  -  -  f0
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${24}
    Should Be Equal As Integers    ${f0}    ${12}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${23}

Test Repeat Until Lines Are Executed Full Iteration
    Repeat Until Lines Are Executed  100
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  -  One Should Pass
    ...  -  -  -  f0
    ...  -  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${39}
    Should Be Equal As Integers    ${f0}    ${1}
    Should Be Equal As Integers    ${f1}    ${13}
    Should Be Equal As Integers    ${f2}    ${13}

Test Repeat Until Branches Are Passed Full Iteration
    Repeat Until Branches Are Passed  100
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  One Should Pass
    ...  -  -  f1
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${35}
    Should Be Equal As Integers    ${f0}    ${0}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${23}

Test Repeat Until Branches Are Executed Full Iteration
    Repeat Until Branches Are Executed  100
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  f2
    ...  -  -  One Should Pass
    ...  -  -  -  f2
    ...  -  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f1
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f0
    ...  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${22}
    Should Be Equal As Integers    ${f0}    ${12}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${24}

Test Repeat Until Lines Are Passed Less Iteration
    Repeat Until Lines Are Passed  75
    ...  One Should Pass
    ...  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  One Should Pass
    ...  -  -  f0
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${15}
    Should Be Equal As Integers    ${f0}    ${12}
    Should Be Equal As Integers    ${f1}    ${13}
    Should Be Equal As Integers    ${f2}    ${13}

Test Repeat Until Lines Are Executed Less Iteration
    Repeat Until Lines Are Executed  75
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f1
    ...  -  -  One Should Pass
    ...  -  -  -  f0
    ...  -  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${39}
    Should Be Equal As Integers    ${f0}    ${1}
    Should Be Equal As Integers    ${f1}    ${13}
    Should Be Equal As Integers    ${f2}    ${13}

Test Repeat Until Branches Are Passed Less Iteration
    Repeat Until Branches Are Passed  75
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f2
    ...  -  One Should Pass
    ...  -  -  f1
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${35}
    Should Be Equal As Integers    ${f0}    ${0}
    Should Be Equal As Integers    ${f1}    ${22}
    Should Be Equal As Integers    ${f2}    ${23}

Test Repeat Until Branches Are Executed Less Iteration
    Repeat Until Branches Are Executed  75
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  f2
    ...  -  -  One Should Pass
    ...  -  -  -  f2
    ...  -  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f1
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f0
    ...  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${2}
    Should Be Equal As Integers    ${f1}    ${2}
    Should Be Equal As Integers    ${f2}    ${2}
