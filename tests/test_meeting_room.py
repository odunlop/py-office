import unittest
from lib.office import MeetingRoom

class TestMeetingRoom(unittest.TestCase):
    def test_meeting_room_name(self):
        room = MeetingRoom("1A")
        self.assertEqual(room.name, "1A")