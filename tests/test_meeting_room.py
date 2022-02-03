import unittest
from lib.office import MeetingRoom

class TestMeetingRoom(unittest.TestCase):
    def test_meeting_room_name(self):
        room = MeetingRoom("1A")
        self.assertEqual(room.name, "1A")
    
    def test_meeting_room_avaliable_by_default(self):
        room = MeetingRoom("2B")
        self.assertEqual(room.avaliablity, True)
    
    def test_starting_meeting_makes_room_unavaliable(self):
        room = MeetingRoom("3C")
        room.start()
        self.assertEqual(room.avaliablity, False)