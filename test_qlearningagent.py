# test_qlearningagent.py
"""
Tests for Q-LearningAgent module.
"""

import unittest
from qlearningagent import Q-LearningAgent

class TestQ-LearningAgent(unittest.TestCase):
    """Test cases for Q-LearningAgent class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Q-LearningAgent()
        self.assertIsInstance(instance, Q-LearningAgent)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Q-LearningAgent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
