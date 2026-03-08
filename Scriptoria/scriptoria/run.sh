#!/bin/bash

echo "========================================"
echo "  Scriptoria - AI Film Studio"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "WARNING: .env file not found!"
    echo "Please copy .env.example to .env and add your API key."
    echo ""
    exit 1
fi

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
echo ""

# Run the application
echo "Starting Scriptoria..."
echo ""
streamlit run app.py
