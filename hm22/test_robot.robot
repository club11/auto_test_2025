*** Settings ***
Library    ../homework_12.py    WITH NAME    BankLibrary

*** Test Cases ***
Test Client Registration
    ${bank}=    Create Bank Instance
    Register Client      ${bank}    0000001    Siarhei
    ${name}=    Get Client Name    ${bank}
    Should Be Equal    ${name}    Siarhei

Test Open Deposit Account
    ${bank}=    Create Bank Instance
    Register Client    ${bank}    0000001    Siarhei
    Open Deposit Account    ${bank}    0000001    100000    1
    ${balance}=    Get Start Balance    ${bank}
    Should Be Equal As Numbers    ${balance}    100000

Test Calculate Interest Rate
    ${bank}=    Create Bank Instance
    Register Client    ${bank}    0000001    Siarhei
    Open Deposit Account    ${bank}    0000001    100000    1
    ${interest}=    Calculate Interest Rate    ${bank}    0000001
    Should Be True    ${interest} > 100000

Test Close Deposit
    ${bank}=    Create Bank Instance
    Register Client    ${bank}    0000001    Siarhei
    Open Deposit Account    ${bank}    0000001    100000    1
    Close Deposit    ${bank}    0000001
    ${balance}=    Get Start Balance    ${bank}
    Should Be Equal As Numbers    ${balance}    0

*** Keywords ***
Create Bank Instance
    ${bank}=    Evaluate    homework_12.Bank()    homework_12
    RETURN    ${bank}

Register Client
    [Arguments]    ${object}    ${client_id}    ${name}
    ${result}=    Call Method    ${object}    register_client    client_id=${client_id}    name=${name}
    [Return]    ${result}

Get Client Name
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.name
    [Return]    ${result}

Open Deposit Account
    [Arguments]    ${object}     ${client_id}    ${start_balance}    ${years}
    ${result}=    Call Method    ${object}    open_deposit_account    client_id=${client_id}    start_balance=${start_balance}    years=${years}

Get Start Balance
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.start_balance
    RETURN    ${result}

Calculate Interest Rate
    [Arguments]    ${object}    ${client_id}
    ${result}=    Call Method    ${object}    calc_interest_rate    client_id=${client_id}
    RETURN    ${result}

Close Deposit
    [Arguments]    ${object}    ${client_id}
    ${result}=    Call Method    ${object}    close_deposit    client_id=${client_id}
