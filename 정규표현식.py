import re

text = "Hello, my email is john@example.com"
match = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
if match:
    email = match.group()
    print(email)  # 출력: john@example.com
