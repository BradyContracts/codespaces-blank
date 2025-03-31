import numpy as np
from torchtext.data.utils import get_tokenizer

def tokenize_code(code_snippet):
    tokenizer = get_tokenizer('basic_english')
    tokens = tokenizer(code_snippet)
    return tokens

def preprocess_data(code_snippets):
    tokenized_snippets = [tokenize_code(snippet) for snippet in code_snippets]
    all_tokens = [token for snippet in tokenized_snippets for token in snippet]
    unique_tokens = list(set(all_tokens))
    token_to_idx = {token: idx for idx, token in enumerate(unique_tokens)}
    idx_to_token = {idx: token for token, idx in token_to_idx.items()}
    return tokenized_snippets, token_to_idx, idx_to_token