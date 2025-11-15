#!/bin/bash
# Setup script for Nude Content Detector

echo "=========================================="
echo "Nude Content Detector - Setup"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Create virtual environment (optional but recommended)
echo ""
read -p "Create virtual environment? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To use the detector:"
echo "  1. If you created a virtual environment: source venv/bin/activate"
echo "  2. Run: python detector.py <image_or_directory>"
echo ""
echo "Examples:"
echo "  python detector.py image.jpg"
echo "  python detector.py /path/to/images/ -r"
echo "  python detector.py image.jpg -o report.txt"
echo ""
echo "For more information, see README.md"
