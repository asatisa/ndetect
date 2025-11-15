# Nude and Porn Picture Detection System

A Python-based content moderation tool that uses deep learning to detect nude and pornographic content in images. Built with NudeNet for accurate detection and classification.

## Features

- **Automatic Detection**: Identifies explicit content in images using state-of-the-art deep learning
- **Classification Levels**:
  - EXPLICIT_CONTENT (High Risk)
  - PARTIAL_NUDITY (Medium Risk)
  - SAFE (Low Risk)
- **Batch Processing**: Scan single images or entire directories
- **Detailed Reports**: Generate comprehensive reports with confidence scores
- **Multiple Export Formats**: Text reports and JSON output
- **Configurable Thresholds**: Adjust sensitivity based on your needs

## Use Cases

- Content moderation for platforms
- Parental control systems
- Workplace content filtering
- Social media safety tools
- Educational purposes

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependency is NudeNet, which will automatically download the pre-trained model on first use.

## Usage

### Command Line Interface

#### Scan a Single Image

```bash
python detector.py image.jpg
```

#### Scan a Directory

```bash
python detector.py /path/to/images/
```

#### Recursive Directory Scan

```bash
python detector.py /path/to/images/ -r
```

#### Save Report to File

```bash
python detector.py image.jpg -o report.txt
```

#### Export Results as JSON

```bash
python detector.py /path/to/images/ -j results.json
```

#### Adjust Detection Threshold

```bash
python detector.py image.jpg -t 0.7
```

### Python API

```python
from detector import NudeContentDetector

# Initialize detector
detector = NudeContentDetector()

# Detect single image
result = detector.detect_file('image.jpg')

print(f"Classification: {result['classification']}")
print(f"Risk Level: {result['risk_level']}")
print(f"Is Explicit: {result['is_explicit']}")

# Scan directory
results = detector.detect_directory('/path/to/images/', recursive=True)

# Generate report
report = detector.generate_report(results, output_file='report.txt')
print(report)
```

## Detection Results

Each detection returns:

- `is_explicit`: Boolean indicating explicit content
- `is_partial_nudity`: Boolean indicating partial nudity
- `classification`: Overall classification (EXPLICIT_CONTENT, PARTIAL_NUDITY, SAFE)
- `risk_level`: Risk assessment (HIGH, MEDIUM, LOW)
- `explicit_detections`: Count of explicit elements detected
- `max_confidence`: Highest confidence score
- `detected_parts`: List of detected body parts with confidence scores

## Exit Codes

When running from command line:

- `0`: All images are safe
- `1`: Partial nudity detected
- `2`: Explicit content detected

## Model Information

This tool uses NudeNet, a deep learning model specifically trained for nude content detection. The model can detect:

- Exposed and covered body parts
- Male and female anatomy
- Various levels of nudity

## Configuration

You can adjust the detection sensitivity by modifying the `nsfw_threshold` parameter:

```python
detector = NudeContentDetector()
detector.nsfw_threshold = 0.7  # Higher = stricter (less sensitive)
```

Default threshold is 0.6 (60% confidence).

## Performance

- First run will download the model (~50MB)
- Subsequent runs use cached model
- Processing time: ~0.5-2 seconds per image (depends on hardware)

## Limitations

- Requires good quality images for best accuracy
- May have false positives/negatives in edge cases
- Performance depends on GPU availability (faster with GPU)

## Privacy and Ethics

This tool is designed for:
- ✅ Content moderation and safety
- ✅ Parental controls
- ✅ Workplace compliance
- ✅ Educational purposes
- ✅ Research with proper consent

Please use responsibly and in compliance with applicable laws and regulations.

## License

This project uses NudeNet which is available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

## Technical Details

### Detected Labels

**Explicit Content:**
- FEMALE_GENITALIA_EXPOSED
- MALE_GENITALIA_EXPOSED
- FEMALE_BREAST_EXPOSED
- BUTTOCKS_EXPOSED
- ANUS_EXPOSED

**Partial Nudity:**
- FEMALE_BREAST_COVERED
- BUTTOCKS_COVERED
- FEMALE_GENITALIA_COVERED
- MALE_GENITALIA_COVERED

## Example Output

```
============================================================
NUDE/PORN CONTENT DETECTION REPORT
============================================================

Total Images Scanned: 5
Explicit Content:     1 (20.0%)
Partial Nudity:       1 (20.0%)
Safe Content:         3 (60.0%)

============================================================
DETAILED RESULTS:
============================================================

1. /path/to/image1.jpg
   Classification: EXPLICIT_CONTENT
   Risk Level: HIGH
   Explicit Detections: 2
   Max Confidence: 0.95
   Detected Parts:
     - FEMALE_BREAST_EXPOSED: 95.2%
     - BUTTOCKS_EXPOSED: 87.3%
```

## Acknowledgments

Built with [NudeNet](https://github.com/notAI-tech/NudeNet) - a state-of-the-art neural network for nude detection.
