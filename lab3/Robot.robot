*** Settings ***
Library   OperatingSystem
Library    Process

*** Variables ***

${main}    /home/roman/qa-kp02-yakobchuk/lab3/main.py

*** Test Cases ***

#Directory
Dir create
    ${result} =    Run Process    python3   ${main}    post    directory    name\=root      maxElements\=100

Dir move
    ${result} =    Run Process    python3   ${main}    patch    directory    name\=name    parent\=root

Dir delete
    ${result} =    Run Process    python3   ${main}    delete    directory    name\=name

Dir read
    ${result} =    Run Process    python3   ${main}    get    directory    name\=name    parent\=root

#Binary
Bin create
    ${result} =    Run Process    python3   ${main}    post    binaryFile  name\=bin   parent\=root    information\=hello

Bin move
    ${result} =    Run Process    python3    ${main}    patch    binaryFile  name\=bin  parent\=root

Bin delete
    ${result} =    Run Process    python3   ${main}    delete    binaryFile  name\=bin

Bin read
    ${result} =    Run Process    python3    ${main}    get    binaryFile  name\=bin  parent\=root

#LogTextFile
Log create
    ${result} =    Run Process    python3   ${main}    post    logTextFile  name\=log   parent\=root    information\=hello

Log move
    ${result} =    Run Process    python3    ${main}    patch    logTextFile  name\=log  parent\=root

Log delete
    ${result} =    Run Process    python3   ${main}    delete    logTextFile  name\=log

Log read
    ${result} =    Run Process    python3    ${main}    get    logTextFile  name\=log  parent\=root

#Buffer
Buf create
    ${result} =    Run Process    python3   ${main}    post    bufferFile  name\=buf   parent\=root    information\=hello

Buf move
    ${result} =    Run Process    python3    ${main}    patch    bufferFile  name\=buf  parent\=root

Buf delete
    ${result} =    Run Process    python3   ${main}    delete    bufferFile  name\=buf

Buf read
    ${result} =    Run Process    python3    ${main}    get    bufferFile  name\=buf  parent\=root