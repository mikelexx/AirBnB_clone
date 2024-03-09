# **DESCRIPTION**
This project is the first step towards building  full web application: **the AirBnB clone**. 
It will be the basis of all other following projects:
_HTML/CSS templating
Database storage
API
front-end integration._
## Each task is linked helps to accomplish the following:

- put in place a parent class (called BaseModel) to take care of the initialization,
   serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
- A command interpreter is used in this project to manipulate data without a visual interface,
  as if one is working on a terminal/Shell (perfect for development and debugging)
---
How to start command interpreter
---
1. Interactive mode
- starting command interpreter of this project is as easy as running ./console script for interactive mode.
 -this will open up the command intepreter in interactive mode and one can enter commands
 -with realtime results.
 ```
$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
2. Non-interactive mode
- Otherwise,for non-interactive mode, one can just pipe a command from bash to the script,
- which case it will execute the command given alongside
- its parameters and exit immediately.
```
 $ echo "help" | ./console.py
 (hbnb)

 Documented commands (type help <topic>):
 ========================================
 EOF  help  quit
 (hbnb) 
 $
 $ cat test_help
 help
 $
 $ cat test_help | ./console.py
 (hbnb)

 Documented commands (type help <topic>):
 ========================================
 EOF  help  quit
 (hbnb) 
 $
```
---
Using command interpreter
---
###  The way it works is once you run it in interactive mode,
###  it prompts you to enter command, which you can provide with optional argument(s)
###  for commands that require so then hit enter to get your result.
###  After getting results you can continue to provide other commands to the prompt
### or just type "quit" to exit the interpreter.
---
### examples
---
## Following are some of the examples to illustrate this.
_to enter the console_
```
 adminpc@mike:~/AirBnB_clone$ ./console.py
 (hbnb)
```
_running no argument commands (create and user commands)_
```
 (hbnb) create BaseModel
 f35a1d39-7b4a-47cd-9740-d450169c1e64
 (hbnb) create User
 2584a587-55c8-4fae-b656-b9bbbfd9dbcd
 ```
_running commands that requires arguments_
```
 (hbnb) show User 2584a587-55c8-4fae-b656-b9bbbfd9dbcd
 [User] (2584a587-55c8-4fae-b656-b9bbbfd9dbcd) {'id': '2584a587-55c8-4fae-b656-b9bbbfd9dbcd', 'created_at': datetime.datetime(2024, 3, 7, 12, 19, 23, 242636), 'updated_at': datetime.datetime(2024, 3, 7, 12, 19, 23, 242680)}
 ```
- the above command created new User object, lets try to view all objects created to this instance  via all command
```
 (hbnb) all
 [BaseModel] (f35a1d39-7b4a-47cd-9740-d450169c1e64) {'id': 'f35a1d39-7b4a-47cd-9740-d450169c1e64', 'created_at': datetime.datetime(2024, 3, 7, 12, 19, 0, 332996), 'updated_at': datetime.datetime(2024, 3, 7, 12, 19, 0, 333051)}
[User] (2584a587-55c8-4fae-b656-b9bbbfd9dbcd) {'id': '2584a587-55c8-4fae-b656-b9bbbfd9dbcd', 'created_at': datetime.datetime(2024, 3, 7, 12, 19, 23, 242636), 'updated_at': datetime.datetime(2024, 3, 7, 12, 19, 23, 242680)}
```
_to see list of available commands for use_
```
 (hbnb) help

 Documented commands (type help <topic>):
 ========================================
 EOF  all  create  destroy  quit  show  update

 Undocumented commands:
 ======================
 help
 ```
_to see the documentation/usage  of a command_
```
(hbnb)
	(hbnb) help show

        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.
      Args:
           line: (str) line containing class name and id
               e.g Ex: $ show BaseModel 1234-1234-1234.


 (hbnb)
```
