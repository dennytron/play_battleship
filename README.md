***Play Battleship!***

Provide the application a list of commands in a commands text file.

*Requires Python 3.10 or Python3.11*

**Running the Application with Python**
```
python3.11 main.py [optional commands file]
```
If no command file is provided as the first argument, the application will look
for `commands.txt`

*The Commands File Composition*

Valid commands are PLACE_SHIP and FIRE.

To place your ships, supply a PLACE_SHIP command followed by 
- A ship type (Carrier, Battleship, Cruiser, Submarine, Destroyer)
- A direction (right or down)
- A location on the 10x10 grid (A1 through J10, where A=down and 10=across)

For example:
```
PLACE_SHIP Destroyer right A1
PLACE_SHIP Carrier down B2
```

To make fire commands, supply a FIRE followed by
- A location on the 10x10 grid (A1 through J10, where A=down and 10=across)

For example:
```
FIRE A1
FIRE B2
```

**Running the Application in Docker**

Supply commands using the provided `commands.txt` and run the application:
```
chmod +x docker-run.sh
./docker-run.sh
```

*The application will show you:*
A list of actions performed.
A map of the battlefield at the end.