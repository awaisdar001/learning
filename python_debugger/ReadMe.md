# What is a debugger?
A tool that helps you look at your program while it’s running.

| ✔ What You Can do? 	| ✘ What You Can't Do? 	|
|--------------------	|----------------------	|
| Freeze frame       	| Find bugs for you :( 	|
| Look around        	|                      	|
| Step line by line  	|                      	|

## What is pdb?

* The standard **P**ython **d**e**b**ugger.
* A module in Python (no installation!)
* A command line tool

## Usage
* Option 1:  Run the whole program under pdb.

```
python -m pdb jeopardy.py
```
 
* Option 2:  Stop at a specific (break)point. 

```
# For python < 3.7 
import pdb;pdb.set_trace()

# For python > 3.7
breakpoint()
```

## Commands

### Look around
| Command              	| What it does?      	                            |
|--------------------	|----------------------	                            |
| L (List)             	| Print source code 	                            |
| P or PP (Pretty Print)|Print variables p or pp (print or pretty print)    |


### Navigation
| Command       	| What It does?                         	|
|---------------	|---------------------------------------	|
| n (next)      	| Advance line by line                  	|
| c (continue)  	| Keep going until the next stop point  	|
| w (here)      	| Where am I?                           	|
| q (uit)       	| Exit debugger                         	|
| s (step into) 	| Dive into a function                  	|
| r (return)    	| Fast forward to the end of a function 	|
