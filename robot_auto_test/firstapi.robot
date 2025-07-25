***Settings***
Library    RequestsLibrary
Library    JSONLibrary


***Variables***
${BASE_URL}    https://jsonplaceholder.typicode.com
${RESOURCE_USERS}    /todos

***Test Cases***
Get Users
    Create Session    session    ${BASE_URL}
    ${response}     Get On Session    session    ${RESOURCE_USERS}/1
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Status Should Be    200    ${response}
    ${json_data} =  Set Variable   ${response.json()}[userId]
    Log To Console      ${json_data}
    Should Be True    ${json_data} == 1
    # Add more assertions as needed