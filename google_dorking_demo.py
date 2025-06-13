from googlesearch import search

query = 'intitle:"index of" "backup"'

print(f"Searching for: {query}\n")

for i, result in enumerate(search(query, stop=10), start=1):
    print(f"[{i}] {result}")

