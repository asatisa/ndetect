#!/usr/bin/env python3
"""
Create simple test images for demonstration purposes
This creates basic geometric shapes to test the detector functionality
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_test_images():
    """Create safe test images for demonstration"""

    # Create test directory
    os.makedirs('test_images', exist_ok=True)

    # Test Image 1: Simple safe image with text
    img1 = Image.new('RGB', (800, 600), color='lightblue')
    draw1 = ImageDraw.Draw(img1)
    draw1.rectangle([100, 100, 700, 500], fill='white', outline='black', width=3)
    draw1.text((300, 250), "SAFE IMAGE", fill='black')
    draw1.text((250, 300), "For Testing Only", fill='gray')
    img1.save('test_images/safe_image_1.jpg')
    print("✓ Created: test_images/safe_image_1.jpg")

    # Test Image 2: Colorful shapes
    img2 = Image.new('RGB', (800, 600), color='white')
    draw2 = ImageDraw.Draw(img2)
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for i in range(6):
        x = (i % 3) * 250 + 50
        y = (i // 3) * 250 + 50
        draw2.ellipse([x, y, x+200, y+200], fill=colors[i], outline='black')
    draw2.text((300, 550), "TEST IMAGE 2", fill='black')
    img2.save('test_images/safe_image_2.jpg')
    print("✓ Created: test_images/safe_image_2.jpg")

    # Test Image 3: Gradient background
    img3 = Image.new('RGB', (800, 600))
    for y in range(600):
        color = int((y / 600) * 255)
        for x in range(800):
            img3.putpixel((x, y), (color, 100, 255 - color))
    draw3 = ImageDraw.Draw(img3)
    draw3.text((250, 280), "DEMO IMAGE", fill='white')
    img3.save('test_images/safe_image_3.jpg')
    print("✓ Created: test_images/safe_image_3.jpg")

    # Test Image 4: Nature-like pattern
    img4 = Image.new('RGB', (800, 600), color='skyblue')
    draw4 = ImageDraw.Draw(img4)
    # Draw "ground"
    draw4.rectangle([0, 400, 800, 600], fill='green')
    # Draw "sun"
    draw4.ellipse([600, 50, 750, 200], fill='yellow')
    # Draw "clouds"
    for i in range(3):
        x = i * 300 + 50
        draw4.ellipse([x, 100, x+150, 180], fill='white')
    draw4.text((250, 500), "LANDSCAPE TEST", fill='white')
    img4.save('test_images/safe_image_4.jpg')
    print("✓ Created: test_images/safe_image_4.jpg")

    print(f"\n✓ Created 4 test images in test_images/ directory")
    print("These are safe geometric images for testing the detector.")

if __name__ == '__main__':
    create_test_images()
