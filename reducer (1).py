#!/usr/bin/env python3
import sys
from collections import defaultdict

summary = defaultdict(int)
for line in sys.stdin:
    country, qty = line.strip().split("\t")
    summary[country] += int(qty)

for country in summary:
    print(f"{country}\t{summary[country]}")
