import requests

# Simple script to fetch existing release notes from Github

# to fetch the next page use: https://api.github.com/repos/demisto/content/releases?page=2
releases = requests.get('https://api.github.com/repos/demisto/content/releases', verify=False).json()

for r in releases:
    print(f'processing: {r["tag_name"]}')
    with open(f'{r["tag_name"]}.md', 'w') as f:
        f.write(r['body'])
