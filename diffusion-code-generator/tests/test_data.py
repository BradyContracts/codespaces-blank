import pytest
from src.data.collection import fetch_code_snippets
from src.data.preprocessing import tokenize_code, preprocess_data
from src.data.augmentation import augment_data

def test_fetch_code_snippets():
    repo_url = 'https://github.com/example/repo'
    snippets = fetch_code_snippets(repo_url)
    assert isinstance(snippets, list)
    assert all(isinstance(snippet, str) for snippet in snippets)

def test_tokenize_code():
    code_snippet = 'def hello_world():'
    tokens = tokenize_code(code_snippet)
    assert isinstance(tokens, list)
    assert 'def' in tokens
    assert 'hello_world' in tokens

def test_preprocess_data():
    code_snippets = ['def hello_world():', 'print("Hello, World!")']
    tokenized_snippets, token_to_idx, idx_to_token = preprocess_data(code_snippets)
    assert len(tokenized_snippets) == len(code_snippets)
    assert len(token_to_idx) > 0

def test_augment_data():
    tokenized_snippets = [['def', 'hello_world', '():'], ['print', '("Hello, World!")']]
    token_to_idx = {token: idx for idx, token in enumerate(set(token for snippet in tokenized_snippets for token in snippet))}
    augmented_snippets = augment_data(tokenized_snippets, token_to_idx)
    assert len(augmented_snippets) == len(tokenized_snippets)
    assert all(isinstance(snippet, list) for snippet in augmented_snippets)