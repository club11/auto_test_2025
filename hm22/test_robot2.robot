*** Settings ***
Library    ../homework_12.py    WITH NAME    BankLibrary


*** Test Cases ***
Test Reader Class
    [Documentation]    Проверка Reader
    ${reader}=    Create Reader    Vasya
    ${name}=    Get Reader Name    ${reader}
    Should Be Equal    ${name}    Vasya

Test Book Class
    [Documentation]    Проверка Book
    ${book}=    Create Book    Hobbit   Tolkien     400     0006754023
    ${name}=    Get Book Name    ${book}
    ${author}=    Get Book Author    ${book}
    ${num_pages}=    Get Book Num Pages    ${book}
    ${isbn}=    Get Book ISBN    ${book}
    Should Be Equal    ${name}    Hobbit
    Should Be Equal    ${author}    Tolkien
    Should Be Equal    ${num_pages}    400
    Should Be Equal    ${isbn}    0006754023

Test Reserve Book
    [Documentation]    Проверка манипуляций с книгой
    ${book}=    Create Book    Hobbit   Tolkien     400     0006754023
    ${reader}=    Create Reader    Vasya

    Reserve Book    ${reader}    ${book}
    ${reserved}=    Get Book Reserve Status    ${book}
    Should Be True    ${reserved} == True
    Cancel Reserve Book    ${reader}    ${book}
    ${reserved}=    Get Book Reserve Status    ${book}
    Should Be True    ${reserved} == False       # ?
    Reserve Book    ${reader}    ${book}
    Get Book    ${reader}    ${book}
    ${is_taken}=    Get Book Taken Status    ${book}
    Should Be True    ${is_taken} == True
    Return Book    ${reader}    ${book}
    ${is_taken}=    Get Book Taken Status    ${book}
    Should Be True    ${is_taken} == False


*** Keywords ***
Create Reader
    [Arguments]    ${name}
    ${result}=    Evaluate    homework_12.Reader(reader_name="${name}")    homework_12
    RETURN    ${result}

Get Reader Name
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.reader_name
    [Return]    ${result}

Create Book
    [Arguments]    ${name}     ${author}    ${num_pages}    ${isbn}
    ${result}=    Evaluate    homework_12.Book(book_name="${name}", author="${author}", num_pages="${num_pages}", isbn="${isbn}")    homework_12
    RETURN    ${result}

Get Book Name
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.book_name
    [Return]    ${result}

Get Book Author
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.author
    [Return]    ${result}

Get Book Num Pages
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.num_pages
    [Return]    ${result}

Get Book ISBN
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.isbn
    [Return]    ${result}

Reserve Book
    [Arguments]    ${object}    ${object_book}
    ${result}=    Call Method    ${object}    reserve_book    a_book=${object_book}
    [Return]    ${result}

Cancel Reserve Book
    [Arguments]    ${object}    ${object_book}
    ${result}=    Call Method    ${object}    cancel_reserve    a_book=${object_book}
    [Return]    ${result}

Get Book
    [Arguments]    ${object}    ${object_book}
    ${result}=    Call Method    ${object}    get_book    a_book=${object_book}
    [Return]    ${result}

Return Book
    [Arguments]    ${object}    ${object_book}
    ${result}=    Call Method    ${object}    return_book    a_book=${object_book}
    [Return]    ${result}


Get Book Reserve Status
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.book_is_reserved
    [Return]    ${result}

Get Book Taken Status
    [Arguments]    ${object}
    ${result}=    Evaluate    $object.book_is_taken
    [Return]    ${result}

