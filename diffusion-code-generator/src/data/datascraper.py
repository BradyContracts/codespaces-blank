from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fetch_python_snippets(url):
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()  # Use Chrome instead of Safari
    
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to load

    python_snippets = []
    
    # Find all code blocks
    code_blocks = driver.find_elements(By.CSS_SELECTOR, "div.file-box")
    
    for block in code_blocks:
        try:
            # Find language tag
            language = block.find_element(By.CSS_SELECTOR, "span.file-type").text
            if "Python" in language:
                # Find code snippet
                code = block.find_element(By.TAG_NAME, "code").text
                python_snippets.append(code.strip())
        except:
            continue

    driver.quit()
    return python_snippets

repo_url = "https://gist.github.com/discover"
snippets = fetch_python_snippets(repo_url)

for snippet in snippets:
    print(snippet)
