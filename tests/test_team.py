import unittest
from lib.office import Team

class TestTeam(unittest.TestCase):
    def test_team_has_name(self):
        team = Team("Bethesda")
        self.assertEqual(team.name, "Bethesda")