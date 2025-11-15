# Quick Start Guide

Get started with the Nude Content Detector in 5 minutes!

## 1. Install

```bash
# Run the setup script
./setup.sh

# Or install manually
pip install -r requirements.txt
```

## 2. Basic Usage

### Scan a Single Image

```bash
python detector.py your_image.jpg
```

### Scan a Folder

```bash
python detector.py /path/to/images/
```

### Recursive Scan

```bash
python detector.py /path/to/images/ -r
```

## 3. Understanding Results

The detector will classify images into three categories:

- **SAFE** (Low Risk) - No explicit content detected
- **PARTIAL_NUDITY** (Medium Risk) - Some covered/partial nudity detected
- **EXPLICIT_CONTENT** (High Risk) - Explicit nudity detected

## 4. Sample Output

```
============================================================
NUDE/PORN CONTENT DETECTION REPORT
============================================================

Total Images Scanned: 3
Explicit Content:     1 (33.3%)
Partial Nudity:       0 (0.0%)
Safe Content:         2 (66.7%)

============================================================
DETAILED RESULTS:
============================================================

1. image1.jpg
   Classification: SAFE
   Risk Level: LOW
   Explicit Detections: 0
   Max Confidence: 0.0

2. image2.jpg
   Classification: EXPLICIT_CONTENT
   Risk Level: HIGH
   Explicit Detections: 2
   Max Confidence: 0.95
   Detected Parts:
     - FEMALE_BREAST_EXPOSED: 95.2%
     - BUTTOCKS_EXPOSED: 87.3%
```

## 5. Advanced Options

### Save Report to File

```bash
python detector.py images/ -o report.txt
```

### Export as JSON

```bash
python detector.py images/ -j results.json
```

### Adjust Sensitivity

```bash
# Lower threshold = more sensitive (0.0-1.0)
python detector.py image.jpg -t 0.5
```

## 6. Using in Python Code

```python
from detector import NudeContentDetector

# Initialize
detector = NudeContentDetector()

# Check single image
result = detector.detect_file('image.jpg')

if result['is_explicit']:
    print("⚠️ Explicit content detected!")
else:
    print("✓ Image is safe")
```

## 7. Common Use Cases

### Content Moderation API
```python
def moderate_user_upload(image_path):
    detector = NudeContentDetector()
    result = detector.detect_file(image_path)

    if result['is_explicit']:
        return {'allowed': False, 'reason': 'Explicit content'}
    return {'allowed': True}
```

### Batch Processing
```python
detector = NudeContentDetector()
results = detector.detect_directory('./uploads/', recursive=True)

# Get all flagged images
flagged = [r for r in results if r['is_explicit']]
print(f"Found {len(flagged)} explicit images")
```

## Troubleshooting

### Error: "NudeNet is not installed"
```bash
pip install nudenet
```

### First run is slow
The model (~50MB) is downloaded on first use. Subsequent runs are much faster.

### Memory issues
Process images in batches or reduce image resolution before detection.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [example.py](example.py) for more code examples
- Adjust `nsfw_threshold` for your specific use case

## Support

For issues, check the README.md or create an issue in the repository.
