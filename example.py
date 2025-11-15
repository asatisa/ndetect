#!/usr/bin/env python3
"""
Example usage of the Nude Content Detector
"""

from detector import NudeContentDetector


def example_single_image():
    """Example: Detect content in a single image"""
    print("=" * 60)
    print("Example 1: Single Image Detection")
    print("=" * 60)

    detector = NudeContentDetector()

    # Replace with your image path
    image_path = "test_image.jpg"

    result = detector.detect_file(image_path)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"File: {result['file_path']}")
        print(f"Classification: {result['classification']}")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Is Explicit: {result['is_explicit']}")
        print(f"Explicit Detections: {result['explicit_detections']}")
        print(f"Max Confidence: {result['max_confidence']}")

        if result['detected_parts']:
            print("\nDetected Parts:")
            for part in result['detected_parts']:
                print(f"  - {part['label']}: {part['confidence']*100:.1f}%")


def example_directory_scan():
    """Example: Scan all images in a directory"""
    print("\n" + "=" * 60)
    print("Example 2: Directory Scan")
    print("=" * 60)

    detector = NudeContentDetector()

    # Replace with your directory path
    directory_path = "./test_images"

    results = detector.detect_directory(directory_path, recursive=True)

    # Generate report
    report = detector.generate_report(results)
    print(report)


def example_custom_threshold():
    """Example: Use custom detection threshold"""
    print("\n" + "=" * 60)
    print("Example 3: Custom Threshold")
    print("=" * 60)

    detector = NudeContentDetector()

    # Set a stricter threshold (less sensitive)
    detector.nsfw_threshold = 0.8

    image_path = "test_image.jpg"
    result = detector.detect_file(image_path)

    print(f"With 0.8 threshold: {result.get('classification', 'N/A')}")


def example_batch_processing_with_filtering():
    """Example: Process multiple images and filter results"""
    print("\n" + "=" * 60)
    print("Example 4: Batch Processing with Filtering")
    print("=" * 60)

    detector = NudeContentDetector()

    directory_path = "./test_images"
    results = detector.detect_directory(directory_path)

    # Filter only explicit content
    explicit_images = [
        r for r in results
        if r.get('is_explicit', False)
    ]

    print(f"\nTotal images scanned: {len(results)}")
    print(f"Explicit content found: {len(explicit_images)}")

    if explicit_images:
        print("\nExplicit images:")
        for img in explicit_images:
            print(f"  - {img['file_path']}")
            print(f"    Risk: {img['risk_level']}, Confidence: {img['max_confidence']}")


def example_export_json():
    """Example: Export results to JSON"""
    print("\n" + "=" * 60)
    print("Example 5: Export to JSON")
    print("=" * 60)

    import json

    detector = NudeContentDetector()

    directory_path = "./test_images"
    results = detector.detect_directory(directory_path)

    # Save to JSON
    output_file = "detection_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results exported to: {output_file}")


def example_api_integration():
    """Example: How to integrate into an API or application"""
    print("\n" + "=" * 60)
    print("Example 6: API Integration Pattern")
    print("=" * 60)

    def check_image_safety(image_path: str) -> dict:
        """
        Check if an image is safe for display.
        Returns decision and reason.
        """
        detector = NudeContentDetector()
        result = detector.detect_file(image_path)

        if result.get('is_explicit'):
            return {
                'safe': False,
                'action': 'BLOCK',
                'reason': f"Explicit content detected (confidence: {result['max_confidence']})",
                'risk_level': result['risk_level']
            }
        elif result.get('is_partial_nudity'):
            return {
                'safe': False,
                'action': 'WARN',
                'reason': "Partial nudity detected - manual review recommended",
                'risk_level': result['risk_level']
            }
        else:
            return {
                'safe': True,
                'action': 'ALLOW',
                'reason': "No explicit content detected",
                'risk_level': result['risk_level']
            }

    # Test the function
    image_path = "test_image.jpg"
    decision = check_image_safety(image_path)

    print(f"Safety Check Result:")
    print(f"  Safe: {decision['safe']}")
    print(f"  Action: {decision['action']}")
    print(f"  Reason: {decision['reason']}")
    print(f"  Risk Level: {decision['risk_level']}")


def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print(" NUDE CONTENT DETECTOR - EXAMPLES")
    print("=" * 70)

    try:
        # Run examples (uncomment the ones you want to try)

        # Note: You'll need to provide actual image paths
        # example_single_image()
        # example_directory_scan()
        # example_custom_threshold()
        # example_batch_processing_with_filtering()
        # example_export_json()
        example_api_integration()

        print("\n" + "=" * 70)
        print("Examples completed!")
        print("=" * 70)

    except Exception as e:
        print(f"\nError running examples: {e}")
        print("\nMake sure to:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Provide valid image paths in the examples")


if __name__ == '__main__':
    main()
