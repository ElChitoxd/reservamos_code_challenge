# reservamos_code_challenge
 Repository that allow the solution to the reservamos code challenge

## Requirements
    Python should be installed in a version 3.9 or higer
    Selenium should be installed in a version 4 or higer
        pip install selenium


 ## Instructions On how to execute the script
The script could be executed by running the next command

python reservamos_code_challenge.py

The script will execute in a headfull way by default and will use chromedriver as its default driver

## Approach
The approach that i took to solve this problem was in the next steps:

    1. Make a manual testing to see the functionality and how the page works
    2. Make another manual run to take the xpath that i will need to do the test, see if there is any frames or iframes or new windows
    3. Start the coding in a simple way
    4. Make the code modular

### Problems that i found on the way

    1. The checkbox could not be clickable on the input tag, i investigate and took the decition to use the span
    2. On headless mode some buttons works in a different way, like the search button
    3. Due this the script is not working in headless mode
    4. Due this i comment the block of lines that could configure the script, and the user can select if it runs in full, or edge driver
    5. The IDE has a lot of troubles, and some extensions too, it reduce my time, as same the weekend i could't work on the project.

# Thanks a lot for give the oportunity to take this assesment!