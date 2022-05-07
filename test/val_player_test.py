import unittest
from src.stats import Player

class TestsPlayer(unittest.TestCase):
    def test_account_data(self):
        user = "jaredthejelly"
        id = "69420"
        
        player = Player(user, id)
        account_data = player.account_data()
        
        self.assertNotEqual(account_data, "There was an error processing your request!")
        
    def test_mmr_data(self):
        user = "jaredthejelly"
        id = "69420"
        
        player = Player(user, id)
        mmr_data = player.mmr_data()
        
        self.assertNotEqual(mmr_data, "There was an error processing your request!")
    
    def test_mmr_history(self):
        user = "jaredthejelly"
        id = "69420"
        
        player = Player(user, id)
        mmr_history = player.mmr_history()
        
        self.assertNotEqual(mmr_history, "There was an error processing your request!")
    
    def test_match_history(self):
        user = "jaredthejelly"
        id = "69420"
        
        player = Player(user, id)
        match_history = player.match_history()
        
        self.assertNotEqual(match_history, "There was an error processing your request!")
        
    def test_bad_account_data(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        player = Player(user, id)
        account_data = player.account_data()
        
        self.assertEqual(account_data, "There was an error processing your request!")
        
    def test_bad_mmr_data(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        player = Player(user, id)
        mmr_data = player.mmr_data()
        
        self.assertEqual(mmr_data, "There was an error processing your request!")
    
    def test_bad_mmr_history(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        player = Player(user, id)
        mmr_history = player.mmr_history()
        
        self.assertEqual(mmr_history, "There was an error processing your request!")
    
    def test_bad_match_history(self):
        user = "jaredthejelly_bad_for_test"
        id = "69420"
        
        player = Player(user, id)
        match_history = player.match_history()
        
        self.assertEqual(match_history, "There was an error processing your request!")

if __name__ == '__main__':
    unittest.main()