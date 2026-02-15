# Timestamp Python

A Python library and CLI tool for working with timestamps and date/time conversions.

## Features

- Convert timestamps to human-readable dates
- Convert dates to timestamps
- Multiple format support (ISO, Unix, custom)
- Current timestamp display
- Timezone conversions
- Relative time calculations
- Python API for integration

## Installation

```bash
pip install timestamp-python
```

Or clone and install:

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
timestamp convert 1699900000

# Convert date to timestamp
timestamp convert "2024-01-01"

# Unix timestamp to date
timestamp unix 1699900000

# Relative time
timestamp relative "2024-01-01"
```

### Python API

```python
from timestamp import Timestamp

ts = Timestamp()

# Get current timestamp
now = ts.now()
print(now)

# Convert timestamp to date
date = ts.from_timestamp(1699900000)
print(date)

# Convert date to timestamp
ts_value = ts.to_timestamp("2024-01-01")
print(ts_value)

# Relative time
relative = ts.relative("2024-01-01")
print(relative)
```

## Options

- `now` - Get current timestamp
- `convert <value>` - Convert between formats
- `unix <timestamp>` - Convert Unix timestamp
- `relative <date>` - Show relative time

## License

MIT License

## Author

mizoz
