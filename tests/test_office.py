import unittest
from unittest.mock import Mock
from lib.office import Office

class TestOffice(unittest.TestCase):
    def test_add_meeting_room(self):
        office = Office()
        mock_room = MockMeetingRoom("1B", True)
        office.add(mock_room)
        self.assertEqual(office.list_rooms(), ["1B"])
    
    def test_list_free_rooms(self):
        office = Office()
        mock_room = MockMeetingRoom("1B", True )
        mock_room2 = MockMeetingRoom("1B", False )
        office.add(mock_room)
        office.add(mock_room2)
        self.assertEqual(
            office.free_rooms(),
            ["1B"]
        )

class MockMeetingRoom:
    def __init__(self, name, avaliability):
        self.name = name
        self.avaliability = avaliability

