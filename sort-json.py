#!/usr/bin/env python3

import sys
import json
import fileinput


content = ""
for line in fileinput.input():
    content += line

print(json.dumps(json.loads(content), sort_keys=True, indent=4, separators=(',', ': ')))
