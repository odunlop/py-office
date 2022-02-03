class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.avaliablity = True
    
    def start(self):
        self.avaliablity = False

class Office:
    def __init__(self):
        self._rooms = []
    
    def add(self, room):
        self._rooms.append(room)

    def list_rooms(self):
        return self.print_rooms(self._rooms)
    
    def print_rooms(self, rooms):
        return [room.name for room in self._rooms]