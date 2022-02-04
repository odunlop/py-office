# Learning Python: Office Management Challenge
As part of my first week learning Python, this repo was created to attempt an old challenge I have already completed in Ruby but in Python instead :snake:

## General Info
* Developed using...
    - Python 3.9
    - unittest
    - psycopg2 (pip must be fully up to date to ensure it works properly)
* Designed so employees can check if a meeting room is busy or occupied
* Test-driven with dependency injection in mind
* Database is truncated after during tests :construction:

### Database Setup
*It is probably not necessary to have a database for this project but I thought it would be a good one to try setting up a database with Python for the first time*

Connect to psql and create the office_teams database:
* Enter the command `CREATE DATABASE office_teams;`
* To set up appropriate tables, connect to the databse in psql and run the SQL scripts in the 'db/migrations' folder.

## Functionality
### MeetingRoom class
- Has a name which can be accessed :white_check_mark:
- Check avaliability (*True* or *False*) :white_check_mark:
- Start meeting, making the room unavaliable :white_check_mark:
    - Blocks you try to start a meeting in an occupied room :white_check_mark:
- End meeting, making the room free :white_check_mark:
- Will be assigned to a team when a meeting starts :white_check_mark:

### Office class
- Add meeting rooms to an office :white_check_mark:
- List all the meeting rooms in an office :white_check_mark:
- List of all avaliable offices :white_check_mark:
- Lists occupied rooms with which teams are using them :white_check_mark:

### Team class (*Data Class*)
- Has a name which can be accessed :white_check_mark:
- Store new teams in a database? :white_check_mark: