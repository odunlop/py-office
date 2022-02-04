from connection import DatabaseConnection
from dataclasses import dataclass

database = DatabaseConnection()
connection = database.create_connection(
    "office_teams", "orladunlop", "", "127.0.0.1", "5432"
)

class Office:
    def __init__(self):
        self._rooms = []
    
    def add(self, room):
        self._rooms.append(room)

    def list_rooms(self):
        return [room.name for room in self._rooms]
    
    def free_rooms(self):
        return [room.name for room in self._rooms if room.avaliable == True]
    
    def occupied_rooms(self):
        return [
            f"{room.name}: {room.team}"
            for room
            in self._rooms
            if room.avaliable == False
        ]

class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.avaliable = True
        self.team = None
    
    def start(self, team):
        if self.avaliable == False:
            return "This room is already in use!"
        else:
            self.avaliable = False
            self.team = team
    
    def end(self):
        self.avaliable = True

@dataclass
class Team:
    name: str

    def __post_init__(self):
        insert_query = (
            f"INSERT INTO teams (name) VALUES ('{self.name}');"
        )
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(insert_query)