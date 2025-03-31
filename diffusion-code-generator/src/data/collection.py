import requests
from bs4 import BeautifulSoup

def fetch_python_snippets(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        python_snippets = []
        
        for code_block in soup.find_all('div', class_='file-box'):
            language_tag = code_block.find('span', class_='file-type')
            if language_tag and 'Python' in language_tag.get_text():
                code_tag = code_block.find('code')
                if code_tag:
                    python_snippets.append(code_tag.get_text().strip())
        
        return python_snippets
    else:
        raise Exception(f'Failed to fetch code snippets from {repo_url}')

repo_url = "https://gist.github.com/discover"
python_snippets = fetch_python_snippets(repo_url)
for snippet in python_snippets:
    print(snippet)
