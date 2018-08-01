import grep
import re

def test_grep(result):
	for line in result[0]:
		assert(result[1].search(line))

test_grep(grep.grep())