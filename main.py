import sys
from stats import report

if len(sys.argv) < 2:
    raise Exception("Usage: python3 main.py <path_to_book>")
else:
	report(sys.argv[1])