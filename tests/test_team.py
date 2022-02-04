import unittest
from lib.office import Team
from connection import DatabaseConnection

database = DatabaseConnection()
connection = database.create_connection(
    "office_teams", "orladunlop", "", "127.0.0.1", "5432"
)

class TestTeam(unittest.TestCase):
    def test_team_has_name(self):
        team = Team("Bethesda")
        self.assertEqual(team.name, "Bethesda")
    
    def test_team_entered_into_db_upon_creation(self):
        database.execute_read_query(connection, "TRUNCATE teams;")

        team = Team("SpaceX")
        result = database.execute_read_query(connection, "SELECT * FROM teams WHERE name = 'SpaceX'")
        self.assertEqual(result[0][1], team.name)

