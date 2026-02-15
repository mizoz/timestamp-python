# Timestamp Python

[![PyPI Version](https://img.shields.io/pypi/v/timestamp-python?style=flat-square)](https://pypi.org/project/timestamp-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/timestamp-python?style=flat-square)](https://pypi.org/project/timestamp-python/)
[![License](https://img.shields.io/pypi/l/timestamp-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/timestamp-python?style=flat-square)](https://pypi.org/project/timestamp-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/timestamp-python?style=flat-square)](https://github.com/mizoz/timestamp-python)

> A Python CLI tool for working with timestamps and date/time conversions.

## Features

- Convert timestamps to human-readable dates
- Convert dates to timestamps
- Get current timestamp
- Multiple format support
- Timezone conversions
- Python API for integration

## Installation

### From PyPI

```bash
pip install timestamp-python
```

### From Source

```bash
git clone https://github.com/mizoz/timestamp-python.git
cd timestamp-python
pip install -e .
```

## Usage

### Command Line

```bash
# Get current timestamp
timestamp now

# Convert timestamp to date
timestamp to-date 1704067200

# Convert date to timestamp
timestamp to-timestamp "2024-01-01"

# Format output
timestamp now --format iso
```

### Python API

```python
from timestamp_tool import TimestampTool

tool = TimestampTool()

# Get current timestamp
now = tool.now()
print(now)

# Convert to date
date = tool.to_date(1704067200)
print(date)
```

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
