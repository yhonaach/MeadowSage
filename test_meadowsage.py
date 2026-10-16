# test_meadowsage.py
"""
Tests for MeadowSage module.
"""

import unittest
from meadowsage import MeadowSage

class TestMeadowSage(unittest.TestCase):
    """Test cases for MeadowSage class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MeadowSage()
        self.assertIsInstance(instance, MeadowSage)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MeadowSage()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
