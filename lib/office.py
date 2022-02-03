from dataclasses import dataclass

class Office:
    def __init__(self):
        self._rooms = []
    
    def add(self, room):
        self._rooms.append(room)

    def list_rooms(self):
        return [room.name for room in self._rooms]
    
    def free_rooms(self):
        return [room.name for room in self._rooms if room.avaliability == True]

class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.avaliablity = True
        self.team = None
    
    def start(self, team):
        if self.avaliablity == False:
            return "This room is already in use!"
        else:
            self.avaliablity = False
            self.team = team
    
    def end(self):
        self.avaliablity = True

@dataclass
class Team:
    name: str