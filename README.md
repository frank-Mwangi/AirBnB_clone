# AirBnB Clone - The Console

HolbertonBnB is a web application, integrating a back-end Python Package, front-end console, and data storage in JSON file format.

## USAGE

Usage To use the console frontend, simply run the console.py file.
This will launch the console application, which will display a prompt for user input.
Users can input commands and the console will execute the corresponding action.

## Running the Console

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF all count create destroy help quit show update

(hbnb)
$
Alternatively, to use the HolbertonBnB console in interactive mode, run the file console.py by itself:

$ ./console.py
While running in interactive mode, the console displays a prompt for input:

$ ./console.py
(hbnb)
To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$
