"""
Integration tests for API (clientside)
"""
import unittest
from api import tests
from database import tests




class TestAPI(unittest.TestCase):
    """
    Testing API works
    """
    def test_add_note(self):
        pass

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)