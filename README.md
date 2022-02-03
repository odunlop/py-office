# Learning Python: Office Management Challenge
As part of my first week learning Python, this repo was created to attempt an old challenge I have already completed in Ruby but in Python instead :snake:

## General Info
* Developed using...
    - Python 3.9
    - unittest
* Designed so employees can check if a meeting room is busy or occupied
* Test-driven with dependency injection in mind

## Functionality
### MeetingRoom class
- Has a name which can be accessed :white_check_mark:
- Check avaliability (True or False) :white_check_mark:
- Start meeting, making the room unavaliable :white_check_mark:
    - Blocks you try to start a meeting in an occupied room :white_check_mark:
- End meeting, making the room free :white_check_mark:
- Will be assigned to a team when a meeting starts :white_check_mark:

### Office class
- Add meeting rooms to an office :white_check_mark:
- List all the meeting rooms in an office :white_check_mark:
- List of all avaliable offices :white_check_mark:
- Lists occupied rooms with which teams are using them :construction:

### Team class (*Data Class*)
- Has a name which can be accessed :white_check_mark: