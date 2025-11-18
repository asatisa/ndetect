#!/usr/bin/env python3
"""
Demo script to test the detector without installing heavy dependencies
This simulates the detector behavior for demonstration
"""

import os
from pathlib import Path

def demo_detection():
    """Demonstrate how the detector would work"""

    print("=" * 70)
    print("NUDE/PORN CONTENT DETECTOR - DEMO MODE")
    print("=" * 70)
    print()
    print("NOTE: This is a demo simulation.")
    print("To use real detection, install: pip install -r requirements.txt")
    print()
    print("=" * 70)

    # Check test images
    test_dir = Path('test_images')
    if not test_dir.exists():
        print("Error: test_images directory not found")
        return

    image_files = list(test_dir.glob('*.jpg'))

    if not image_files:
        print("No test images found")
        return

    print(f"Found {len(image_files)} test image(s)")
    print("=" * 70)
    print()

    # Simulate detection results
    for idx, img_path in enumerate(image_files, 1):
        print(f"{idx}. {img_path.name}")
        print(f"   Classification: SAFE")
        print(f"   Risk Level: LOW")
        print(f"   Explicit Detections: 0")
        print(f"   Max Confidence: 0.0")
        print(f"   Status: ✓ Image is safe")
        print()

    print("=" * 70)
    print("SUMMARY:")
    print("=" * 70)
    print(f"Total Images: {len(image_files)}")
    print(f"Safe: {len(image_files)} (100%)")
    print(f"Explicit: 0 (0%)")
    print(f"Partial Nudity: 0 (0%)")
    print()
    print("=" * 70)
    print("HOW TO USE REAL DETECTION:")
    print("=" * 70)
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print()
    print("2. Run detector:")
    print("   python detector.py test_images/")
    print()
    print("3. Or use Python API:")
    print("   from detector import NudeContentDetector")
    print("   detector = NudeContentDetector()")
    print("   result = detector.detect_file('image.jpg')")
    print()

if __name__ == '__main__':
    demo_detection()
