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
    [Documentation]  This keyword works as a bomb it fails if called.
    ${f0}   Set Variable  ${${f0}+1}
    Set Test Variable    ${f0}
    Fail  f0 has failed


*** Test Cases ***
# Tree functionality test
Test All Branches Are Executed
    # Execution
    All Branches Should Be Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${3}
    Should Be Equal As Integers    ${f0}    ${2}
    
Test All Branches Are Executed Failour
    # Execution
    Run Keyword And Expect Error    Not all branches are executed.    All Branches Should Be Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test All Lines Are Executed
    # Execution
   All Lines Should Be Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test All Lines Are Executed Failour
    # Execution
   Run Keyword And Expect Error    Not all lines are executed.    All Lines Should Be Executed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  f0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test All Branches Are Passed
    # Execution
    All Branches Should Be Passed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test All Branches Are Passed Failour
    # Execution
    Run Keyword And Expect Error    Not all branches are passed.    All Branches Should Be Passed
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  All Should Pass
    ...  -  -  K0
    ...  -  -  K0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}


# Test All Lines Are Passed
#     # Execution
#     All Lines Should Be Passed
#     ...  One Should Pass
#     ...  -  f0
#     ...  -  All Should Pass
#     ...  -  -  K0
#     ...  -  -  K0
#     # Validation
#     Should Be Equal As Integers    ${k0}    ${2}
#     Should Be Equal As Integers    ${f0}    ${1}

# Test All Lines Are Passed Failour
#     # Execution
#     Run Keyword And Expect Error    Not all lines are passed.    All Lines Should Be Passed
#     ...  One Should Pass
#     ...  -  f0
#     ...  -  All Should Pass
#     ...  -  -  K0
#     ...  -  -  K0
#     ...  -  All Should Pass
#     ...  -  -  K0
#     ...  -  -  K0
#     ...  -  K0
#     # Validation
#     Should Be Equal As Integers    ${k0}    ${2}
#     Should Be Equal As Integers    ${f0}    ${1}


Test Certain Percentage Lines Are Passed
    # Execution
    Lines Should Be Passed  (2/6)*100
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test Certain Percentage Lines Are Passed Failour
    # Execution
    Run Keyword And Expect Error    50% of lines could not be passed.    Lines Should Be Passed  50
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  K0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test Certain Percentage Lines Are Executed
    Lines Should Be Executed  50
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f0
    ...  -  One Should Pass
    ...  -  -  f0
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${3}

Test Certain Percentage Lines Are Executed Failour
    Run Keyword And Expect Error    50% of lines could not be executed.    Lines Should Be Executed  50
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  One Should Pass
    ...  -  -  f0
    ...  -  -  k0
    ...  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test Certain Percentage Branches Are Executed
    Branches Should Be Executed  50
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f0
    ...  -  f0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${3}

Test Certain Percentage Branches Are Executed Failour
    Run Keyword And Expect Error    75% of branches could not be executed.     Branches Should Be Executed  75
    ...  One Should Pass
    ...  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f0
    ...  -  -  k0
    ...  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${1}

Test Certain Percentage Branches Are Passed
    Branches Should Be Passed  50
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  f0
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  -  One Should Pass
    ...  -  -  -  k0
    ...  -  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${4}
    Should Be Equal As Integers    ${f0}    ${1}

Test Certain Percentage Branches Are Passed Failour
    Run Keyword And Expect Error    75% of branches could not be passed.     Branches Should Be Passed  75
    ...  One Should Pass
    ...  -  All Should Pass
    ...  -  -  k0
    ...  -  -  k0
    ...  -  All Should Pass
    ...  -  -  f0
    ...  -  -  k0
    # Validation
    Should Be Equal As Integers    ${k0}    ${2}
    Should Be Equal As Integers    ${f0}    ${0}

