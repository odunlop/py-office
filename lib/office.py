from dataclasses import dataclass

class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.avaliablity = True
    
    def start(self):
        if self.avaliablity == False:
            return "This room is already in use!"
        else:
            self.avaliablity = False
    
    def end(self):
        self.avaliablity = True

class Office:
    def __init__(self):
        self._rooms = []
    
    def add(self, room):
        self._rooms.append(room)

    def list_rooms(self):
        return [room.name for room in self._rooms]
    
    def free_rooms(self):
        return [room.name for room in self._rooms if room.avaliability == True]

@dataclass
class Team:
    name: str