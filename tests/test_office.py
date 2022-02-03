import unittest
from unittest.mock import Mock
from lib.office import Office

class TestOffice(unittest.TestCase):
    def test_add_meeting_room(self):
        office = Office()
        mock_room = Mock(name = "1B")
        office.add(mock_room)
        self.assertEqual(office.list_rooms(), [mock_room.name])
        

