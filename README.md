# Coding Practice: Tournament Winner
This project is meant for me to practice coding interview questions with Python.
I am presented with the following task: Given an array of pairs representing 
teams that have competed against each other and an array containing the 
results of the competition, write a function that returns the winner of each 
tournament.

Important Background Information:
This exercise demonstrates an exercise of a competition that follows a 
round-robin elimination style (where only the winner advances). Each team is 
either designated as a home or away team. There are no ties and only one 
team can advance to the next round of competitions. Each winning score will 
increase by 3 points.

The arrays are noted as follows:
competitions = [homeTeam, awayTeam]
results = results[i], is defaulted to keep account of the homeTeam's wins (1 
if win and 0 if lost). A team will only advice if they win.

Sample output: 
competitions = [
["teamOne", "teamTwo",
"teamTwo", "teamThree",
"teamThree", "teamOne""]
]
results = [0,0,1]

It should be read as follows: 
1. teamTwo won against teamOne
2. teamThree won against teamTwo
3. teamThree won against teamOne


## Running The Project
**NOTE: Your IDE may configure the project implicitly as a module. BE SURE TO 
RUN STEP 4 BELOW BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to the [ProductSum.Mod1]() directory
3. Run the program as a module: `python -m Mod1 -h`. This will print the help 
   message.
4. Run the program as a module (with real inputs): `python -m Mod1`
   a. IE: `python -m Mod1`

The program's output will be displayed in the output.txt file.

### Mod1 Usage:

```commandline
usage: python -m Mod1 [-h] 

optional arguments:
  -h, --help  show a help message and exits the program
```

Usage statements are very formalized

| Symbol    | Meaning   |
| ---           | ---       |
| [var]         | variable var is optional. |
| var           | variable var is required. All positional arguments are required.|
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values |
| *             | This argument consumes 0 or more values |

### Project Layout

The following was my project's package layout:

* ProductSum.Mod1/: `The parent or "root" folder containing all of the 
  projecs files`
    * README.md:
      `The README files that describes my programs and the nuances needed 
      to run the program`
    * Mod1/: 
      `The module of my program (per requirement).`
      * __init__.py 
        `This python file details critical functions, variables, and 
        classes that are exposed when scripts import the Lab1 module.`
      * __main__.py 
        `The starting point when the program runs, it handles command line 
        arguments.`
      * *.py 
        `Holds the scripts that perform the code.`