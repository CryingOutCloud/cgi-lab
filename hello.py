#!/usr/bin/env python3

import os
import json

print("Content-Type: text/plain")
print()
# print(os.environ) Q1

#Q2: QUERY_STRING

# print(json.dumps(dict(os.environ), indent=2))


#Q3: just print your key
print(f"'<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")