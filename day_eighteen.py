import re

txt = "I love to teach python"

match = re.match("I love to teach", txt, re.I)
print(match)

if match:
    span = match.span()
    print(span)

    start, end = span
    print(start, end)

    substring = txt[start:end]
    print(substring)
