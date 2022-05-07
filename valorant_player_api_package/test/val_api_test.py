import unittest
from valorant_player_api import ValorantAPI

class TestsValorantAPI(unittest.TestCase):
    def test_get_account_data(self):
        user = "jaredthejelly"
        id = "69420"
        
        val = ValorantAPI()
        account_data = val.get_account_data(user, id)
        
        self.assertNotEqual(account_data, "There was an error processing your request!")
        
    def test_get_mmr_data(self):
        user = "jaredthejelly"
        id = "69420"
        
        val = ValorantAPI()
        mmr_data = val.get_mmr_data(user, id)
        
        self.assertNotEqual(mmr_data, "There was an error processing your request!")
    
    def test_get_mmr_history(self):
        user = "jaredthejelly"
        id = "69420"
        
        val = ValorantAPI()
        mmr_history = val.get_mmr_history(user, id)
        
        self.assertNotEqual(mmr_history, "There was an error processing your request!")
    
    def test_get_match_history(self):
        user = "jaredthejelly"
        id = "69420"
        
        val = ValorantAPI()
        match_history = val.get_match_history(user, id)
        
        self.assertNotEqual(match_history, "There was an error processing your request!")
        
    def test_bad_get_account_data(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        val = ValorantAPI()
        account_data = val.get_account_data(user, id)
        
        self.assertEqual(account_data, "There was an error processing your request!")
        
    def test_bad_get_mmr_data(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        val = ValorantAPI()
        mmr_data = val.get_mmr_data(user, id)
        
        self.assertEqual(mmr_data, "There was an error processing your request!")
    
    def test_bad_get_mmr_history(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        val = ValorantAPI()
        mmr_history = val.get_mmr_history(user, id)
        
        self.assertEqual(mmr_history, "There was an error processing your request!")
    
    def test_bad_get_match_history(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        val = ValorantAPI()
        match_history = val.get_match_history(user, id)
        
        self.assertEqual(match_history, "There was an error processing your request!")

if __name__ == '__main__':
    unittest.main()