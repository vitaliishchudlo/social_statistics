# Social Network Statistics
___
<!--
Download sources
----
- **Windows** - the most current version is [here](https://github.com/vitaliishchudlo/steam_name_changer/releases)
-->
NEED TO INSTALL microdot(asyncio)

Prerequisites
-------------
This project consists of two parts: 
  - Web server
  - LCD output

#### Web server
      Will be developed in Flask using Python 3.8+
      The API shall be able to return data from the user's social networks in JSON format.

#### LCD Output:
      The display system shall be developed in the MicroPayton language.
      The ESP32/ESP8266 microcontroller will be used.
      The output of information will be performed on LCD 1602/2004
Future features in the folded version
-------------
  - Power change button (batteries / USB)
  - System restart button
  - Colored box lighting that can be changed
___


<!--
Getting Started
-------------
run bootstrap.sh: ./bootstrap.sh
start service: docker compose up

Testing
-------------
To test the application:

app$ scripts/test_app.sh

Linting
-------------
To lint the shell scripts:

$ docker compose run shell-linter
shell-linter$ scripts/lint_app.sh

or

$ docker compose run shell-linter scripts/lint_app.sh
Documenting
To document the application:

app$ scripts/document_app.sh

Notes
-------------
-->
