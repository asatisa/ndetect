#!/usr/bin/env python3
"""
Nude and Porn Picture Detection System
Using NudeNet for content moderation and safety
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import json

try:
    from nudenet import NudeDetector
except ImportError:
    print("Error: NudeNet is not installed. Please run: pip install nudenet")
    sys.exit(1)


class NudeContentDetector:
    """
    Detector for nude and pornographic content in images.
    Uses deep learning models to classify and detect explicit content.
    """

    def __init__(self, model_path: str = None):
        """
        Initialize the detector.

        Args:
            model_path: Optional path to custom model. If None, uses default NudeNet model.
        """
        print("Initializing NudeNet Detector...")
        self.detector = NudeDetector(model_path) if model_path else NudeDetector()

        # Classification thresholds
        self.nsfw_threshold = 0.6

        # Define labels that indicate explicit content
        self.explicit_labels = {
            'FEMALE_GENITALIA_EXPOSED',
            'MALE_GENITALIA_EXPOSED',
            'FEMALE_BREAST_EXPOSED',
            'BUTTOCKS_EXPOSED',
            'ANUS_EXPOSED',
            'MALE_BREAST_EXPOSED'
        }

        # Define labels that may indicate partial nudity
        self.partial_nudity_labels = {
            'FEMALE_BREAST_COVERED',
            'BUTTOCKS_COVERED',
            'FEMALE_GENITALIA_COVERED',
            'MALE_GENITALIA_COVERED'
        }

    def detect_file(self, image_path: str) -> Dict:
        """
        Detect nude/porn content in a single image file.

        Args:
            image_path: Path to the image file

        Returns:
            Dictionary with detection results
        """
        if not os.path.exists(image_path):
            return {
                'error': f'File not found: {image_path}',
                'is_explicit': False
            }

        try:
            # Run detection
            detections = self.detector.detect(image_path)

            # Analyze results
            analysis = self._analyze_detections(detections)
            analysis['file_path'] = image_path

            return analysis

        except Exception as e:
            return {
                'error': f'Detection failed: {str(e)}',
                'file_path': image_path,
                'is_explicit': False
            }

    def detect_directory(self, directory_path: str, recursive: bool = False) -> List[Dict]:
        """
        Detect nude/porn content in all images in a directory.

        Args:
            directory_path: Path to the directory
            recursive: Whether to search subdirectories

        Returns:
            List of detection results for each image
        """
        results = []

        # Supported image extensions
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'}

        path = Path(directory_path)
        if not path.exists():
            return [{'error': f'Directory not found: {directory_path}'}]

        # Get image files
        if recursive:
            image_files = [
                f for f in path.rglob('*')
                if f.is_file() and f.suffix.lower() in image_extensions
            ]
        else:
            image_files = [
                f for f in path.glob('*')
                if f.is_file() and f.suffix.lower() in image_extensions
            ]

        print(f"Found {len(image_files)} image(s) to process...")

        for idx, image_file in enumerate(image_files, 1):
            print(f"Processing {idx}/{len(image_files)}: {image_file.name}")
            result = self.detect_file(str(image_file))
            results.append(result)

        return results

    def _analyze_detections(self, detections: List[Dict]) -> Dict:
        """
        Analyze detection results to determine if content is explicit.

        Args:
            detections: List of detections from NudeNet

        Returns:
            Analysis results
        """
        explicit_count = 0
        partial_nudity_count = 0
        max_confidence = 0.0
        detected_parts = []

        for detection in detections:
            label = detection['class']
            score = detection['score']

            if score > max_confidence:
                max_confidence = score

            if label in self.explicit_labels and score > self.nsfw_threshold:
                explicit_count += 1
                detected_parts.append({
                    'label': label,
                    'confidence': round(score, 3),
                    'box': detection['box']
                })
            elif label in self.partial_nudity_labels and score > self.nsfw_threshold:
                partial_nudity_count += 1
                detected_parts.append({
                    'label': label,
                    'confidence': round(score, 3),
                    'box': detection['box']
                })

        # Determine classification
        is_explicit = explicit_count > 0
        is_partial_nudity = partial_nudity_count > 0 and not is_explicit

        # Risk level
        if is_explicit:
            risk_level = 'HIGH'
            classification = 'EXPLICIT_CONTENT'
        elif is_partial_nudity:
            risk_level = 'MEDIUM'
            classification = 'PARTIAL_NUDITY'
        else:
            risk_level = 'LOW'
            classification = 'SAFE'

        return {
            'is_explicit': is_explicit,
            'is_partial_nudity': is_partial_nudity,
            'classification': classification,
            'risk_level': risk_level,
            'explicit_detections': explicit_count,
            'partial_nudity_detections': partial_nudity_count,
            'max_confidence': round(max_confidence, 3),
            'detected_parts': detected_parts,
            'total_detections': len(detections)
        }

    def generate_report(self, results: List[Dict], output_file: str = None) -> str:
        """
        Generate a summary report of detection results.

        Args:
            results: List of detection results
            output_file: Optional file to save the report

        Returns:
            Report as a string
        """
        total = len(results)
        explicit = sum(1 for r in results if r.get('is_explicit', False))
        partial = sum(1 for r in results if r.get('is_partial_nudity', False))
        safe = total - explicit - partial

        report = f"""
{'='*60}
NUDE/PORN CONTENT DETECTION REPORT
{'='*60}

Total Images Scanned: {total}
Explicit Content:     {explicit} ({100*explicit/total if total > 0 else 0:.1f}%)
Partial Nudity:       {partial} ({100*partial/total if total > 0 else 0:.1f}%)
Safe Content:         {safe} ({100*safe/total if total > 0 else 0:.1f}%)

{'='*60}
DETAILED RESULTS:
{'='*60}
"""

        for idx, result in enumerate(results, 1):
            if 'error' in result:
                report += f"\n{idx}. {result.get('file_path', 'Unknown')}\n"
                report += f"   ERROR: {result['error']}\n"
            else:
                report += f"\n{idx}. {result.get('file_path', 'Unknown')}\n"
                report += f"   Classification: {result.get('classification', 'N/A')}\n"
                report += f"   Risk Level: {result.get('risk_level', 'N/A')}\n"
                report += f"   Explicit Detections: {result.get('explicit_detections', 0)}\n"
                report += f"   Max Confidence: {result.get('max_confidence', 0)}\n"

                if result.get('detected_parts'):
                    report += f"   Detected Parts:\n"
                    for part in result['detected_parts']:
                        report += f"     - {part['label']}: {part['confidence']*100:.1f}%\n"

        report += f"\n{'='*60}\n"

        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved to: {output_file}")

        return report


def main():
    """Main function for CLI usage"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Detect nude and pornographic content in images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s image.jpg                    # Detect single image
  %(prog)s /path/to/images/             # Detect all images in directory
  %(prog)s /path/to/images/ -r          # Recursive scan
  %(prog)s image.jpg -o report.txt      # Save report to file
  %(prog)s /path/to/images/ -j results.json  # Export as JSON
        """
    )

    parser.add_argument(
        'input',
        help='Path to image file or directory'
    )

    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Recursively scan subdirectories'
    )

    parser.add_argument(
        '-o', '--output',
        help='Save report to text file'
    )

    parser.add_argument(
        '-j', '--json',
        help='Export results as JSON file'
    )

    parser.add_argument(
        '-t', '--threshold',
        type=float,
        default=0.6,
        help='Detection confidence threshold (0.0-1.0, default: 0.6)'
    )

    args = parser.parse_args()

    # Initialize detector
    detector = NudeContentDetector()
    detector.nsfw_threshold = args.threshold

    # Process input
    input_path = Path(args.input)

    if input_path.is_file():
        print(f"Detecting content in: {input_path}")
        results = [detector.detect_file(str(input_path))]
    elif input_path.is_dir():
        print(f"Scanning directory: {input_path}")
        results = detector.detect_directory(str(input_path), args.recursive)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)

    # Generate and display report
    report = detector.generate_report(results, args.output)
    print(report)

    # Export JSON if requested
    if args.json:
        with open(args.json, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"JSON results saved to: {args.json}")

    # Exit with status code based on results
    if any(r.get('is_explicit', False) for r in results):
        sys.exit(2)  # Explicit content found
    elif any(r.get('is_partial_nudity', False) for r in results):
        sys.exit(1)  # Partial nudity found
    else:
        sys.exit(0)  # All safe


if __name__ == '__main__':
    main()
