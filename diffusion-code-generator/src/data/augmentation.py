import numpy as np

def augment_data(tokenized_snippets, token_to_idx):
    augmented_snippets = []
    for snippet in tokenized_snippets:
        # Random Insertion
        if np.random.rand() < 0.1:
            insertion_index = np.random.randint(0, len(snippet) + 1)
            inserted_token = np.random.choice(list(token_to_idx.keys()))
            snippet.insert(insertion_index, inserted_token)
        # Random Deletion
        if np.random.rand() < 0.1 and len(snippet) > 1:
            deletion_index = np.random.randint(0, len(snippet))
            del snippet[deletion_index]
        # Random Swap
        if np.random.rand() < 0.1 and len(snippet) > 1:
            swap_index1, swap_index2 = np.random.choice(len(snippet), 2, replace=False)
            snippet[swap_index1], snippet[swap_index2] = snippet[swap_index2], snippet[swap_index1]
        augmented_snippets.append(snippet)
    return augmented_snippets