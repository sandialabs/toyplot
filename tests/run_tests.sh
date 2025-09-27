#!/usr/bin/env bash
set -euo pipefail

# run_tests.sh
# Run the Toyplot test suite.
# Requires: Python with unittest module (standard library)

echo "Running Toyplot test suite..."

# Change to the project root directory
cd "$(dirname "$0")/.."

# Run tests using unittest discovery
python -m unittest discover -s tests -p "test_*.py" -v

echo "All tests passed."