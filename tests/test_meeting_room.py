import unittest
from unittest.mock import Mock
from lib.office import MeetingRoom

class TestMeetingRoom(unittest.TestCase):
    def test_meeting_room_name(self):
        room = MeetingRoom("1A")
        self.assertEqual(room.name, "1A")
    
    def test_meeting_room_avaliable_by_default(self):
        room = MeetingRoom("2B")
        self.assertEqual(room.avaliable, True)
    
    def test_starting_meeting_makes_room_unavaliable(self):
        room = MeetingRoom("3C")
        mock_team = Mock()
        room.start(mock_team)
        self.assertEqual(room.avaliable, False)
    
    def test_ending_meeting_makes_room_avaliable(self):
        room = MeetingRoom("4D")
        mock_team = Mock()
        room.start(mock_team)
        room.end()
        self.assertEqual(room.avaliable, True)
    
    def test_cannot_start_meeting_in_occupied_room(self):
        room = MeetingRoom("5E")
        mock_team = Mock()
        room.start(mock_team)
        self.assertEqual(
            room.start(mock_team),
            "This room is already in use!"
        )

    def test_starting_meeting_assigns_team(self):
        room = MeetingRoom("6F")
        mock_team = Mock()
        room.start(mock_team)
        self.assertEqual(room.team, mock_team)
