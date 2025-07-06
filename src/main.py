#!/usr/bin/env python3
"""
Main application file for Claude GitHub Integration Test

This demonstrates a complete Python project setup via GitHub MCP.
"""

import sys
from utils import validate_input, process_data


def main():
    """Main application entry point."""
    print("🚀 Claude GitHub Integration Test")
    print("=" * 35)
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_data>")
        sys.exit(1)
    
    input_data = sys.argv[1]
    
    if not validate_input(input_data):
        print("❌ Invalid input data")
        sys.exit(1)
    
    result = process_data(input_data)
    print(f"✅ Result: {result}")


if __name__ == "__main__":
    main()
