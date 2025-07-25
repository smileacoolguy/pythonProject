*** Settings ***
Library    SeleniumLibrary

*** variables ***
${url}    https://robotframework.org/RobotDemo/

***Test Cases***
Open Google and Verify Title
    Learning first program
    Learning first program

*** keywords ***
Learning first program
    Open Browser   ${url}     chrome
    Title Should Be    Robot Framework Demo
    #[Timeout]    3 second
    Close Browser

