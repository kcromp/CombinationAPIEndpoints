# CombinationAPIEndpoints

## Description

API endpoints that display possible combinations depending on task. The root endpoint '/' will give light detail on what to expect in the other endpoints. 
The endpoint '/coins' returns the count and combinations of the number of ways pennies, nickels, dimes, and quarters can be combined to sum exactly $1. 
The '/demo' endpoint uses input from the denomination_values.txt file to parse and return the count and combinations for an arbitrary set of currency names 
and denominations for an arbitrary total sum. 


## Requirements 

```
Python v3.9 (To download: https://www.python.org/downloads/). This application was built and tested using Python version 3.9 
Install Flask. Command Prompt: pip install Flask. Additional information on Flask and installation procedures can be found https://pypi.org/project/Flask/
``` 

## How to Start the Application

Download files and store locally. 
Using Command Prompt, navigate to inside the recently downloaded CombinationAPIEndpoints folder (on the same level as the app.py file) and run Flask: 

```
$ flask run
```

Open a browser to the address and port listed. The default location from within the application will be http://127.0.0.1:5000/. (Press CTRL + C to quit) 

Navigate to http://127.0.0.1:5000/coins to view the the count and combinations of the number of ways pennies, nickels, dimes, and quaters can be combined
to sum exactly $1. 

Navigate to http://127.0.0.1:5000/demo to view the count and combinations of an arbitrary set of currency names and denominations for a total sum. 
The currency names and denominations for this endpoint are configurable from within the denomination_values.txt file. 


## Changing Values

To change the count and combination for the '/demo' endpoint, open the denomination_values.txt file and add custom data. The data should be edited or inserted 
using the format 'name' (string) and 'quantity required to reach the desired sum' (int) on alternating lines. 

For example: 

``` 
coins
1.5 
arrowhead
3
buttons
150
``` 

Note that the application may need to be restarted from the Command Prompt or Terminal to see the updated results after a change. 


## Testing

Test cases and documenation have been added to this project. 

