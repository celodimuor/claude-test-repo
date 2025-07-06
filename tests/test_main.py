#!/usr/bin/env python3
"""
Unit tests for Claude GitHub Integration Test

Comprehensive test suite for the main application.
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import validate_input, process_data, calculate_hash


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_validate_input_valid(self):
        """Test validation with valid inputs."""
        self.assertTrue(validate_input("hello world"))
        self.assertTrue(validate_input("test-123"))
        self.assertTrue(validate_input("Valid_Input_123"))
    
    def test_validate_input_invalid(self):
        """Test validation with invalid inputs."""
        self.assertFalse(validate_input(""))
        self.assertFalse(validate_input("   "))
        self.assertFalse(validate_input("invalid@email.com"))
        self.assertFalse(validate_input("special!chars"))
    
    def test_process_data_success(self):
        """Test successful data processing."""
        result = process_data("test input")
        self.assertIsNotNone(result)
        self.assertIn("TEST INPUT", result)
        self.assertIn("[", result)  # Should contain timestamp
    
    def test_calculate_hash(self):
        """Test hash calculation."""
        hash1 = calculate_hash("test")
        hash2 = calculate_hash("test")
        hash3 = calculate_hash("different")
        
        self.assertEqual(hash1, hash2)  # Same input, same hash
        self.assertNotEqual(hash1, hash3)  # Different input, different hash
        self.assertEqual(len(hash1), 32)  # MD5 hash length


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete application."""
    
    def test_full_workflow(self):
        """Test the complete data processing workflow."""
        test_input = "integration test"
        
        # Validate
        self.assertTrue(validate_input(test_input))
        
        # Process
        result = process_data(test_input)
        self.assertIsNotNone(result)
        
        # Hash
        hash_result = calculate_hash(test_input)
        self.assertIsInstance(hash_result, str)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
