#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Activating virtual environment..."

# Activate the virtual environment
source venv/Scripts/activate

echo "Running test suite..."

# Run pytest
pytest

# Capture the exit code
STATUS=$?

if [ $STATUS -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
