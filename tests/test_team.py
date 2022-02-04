import unittest
from lib.office import Team

class TestTeam(unittest.TestCase):
    def test_team_has_name(self):
        team = Team("Bethesda")
        self.assertEqual(team.name, "Bethesda")
    
    # def test_team_entered_into_db_upon_creation(self):
        # team = Team("Test")
        
        # Need to truncate at some point