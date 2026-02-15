#!/usr/bin/env python3
"""Convert timestamps to human-readable format."""
import sys, datetime

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: timestamp.py <timestamp> [--to-ts]")
        sys.exit(1)
    v = sys.argv[1]
    if '--to-ts' in sys.argv:
        print(int(datetime.datetime.fromisoformat(v).timestamp()))
    else:
        print(datetime.datetime.fromtimestamp(int(v)).isoformat())
