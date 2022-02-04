import unittest
from lib.office import Office

class TestOffice(unittest.TestCase):
    def test_add_meeting_room(self):
        office = Office()
        mock_room = MockMeetingRoom("1B", True, None )
        office.add(mock_room)
        self.assertEqual(office.list_rooms(), ["1B"])
    
    def test_list_free_rooms(self):
        office = Office()
        mock_room = MockMeetingRoom("1A", True, None )
        mock_room2 = MockMeetingRoom("2B", False, None)
        office.add(mock_room)
        office.add(mock_room2)
        self.assertEqual(
            office.free_rooms(),
            ["1A"]
        )
    
    def test_list_occupied_rooms_with_teams(self):
        office = Office()
        mock_room = MockMeetingRoom("1A", True, "Bethesda" )
        mock_room2 = MockMeetingRoom("2B", False, "Concerned Ape")
        mock_room3 = MockMeetingRoom("3C", False, "Blizzard")
        office.add(mock_room)
        office.add(mock_room2)
        office.add(mock_room3)
        self.assertEqual(
            office.occupied_rooms(),
            ["2B: Concerned Ape", "3C: Blizzard"]
        )

class MockMeetingRoom:
    def __init__(self, name, avaliable, team):
        self.name = name
        self.avaliable = avaliable
        self.team = team