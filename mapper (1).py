#!/usr/bin/env python3
import sys
for line in sys.stdin:
    fields = line.strip().split(",")
    if len(fields) > 7 and fields[7] != "Country":
        print(f"{fields[7]}\t{fields[3]}")  # Country \t Quantity
