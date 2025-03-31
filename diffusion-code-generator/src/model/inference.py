def generate_code(model, prompt, max_length=100):
    model.eval()
    input_seq = [token_to_idx[token] for token in tokenize_code(prompt)]
    input_seq = torch.tensor(input_seq).unsqueeze(0)
    generated_code = []
    with torch.no_grad():
        for _ in range(max_length):
            outputs = model(input_seq)
            _, predicted = torch.max(outputs[:, -1, :], 1)
            generated_code.append(idx_to_token[predicted.item()])
            input_seq = torch.cat([input_seq, predicted.unsqueeze(0)], dim=1)
    return ' '.join(generated_code)