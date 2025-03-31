import torch

def evaluate_model(model, val_loader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in val_loader:
            outputs = model(inputs)
            loss = criterion(outputs.view(-1, model.fc.out_features), targets.view(-1))
            total_loss += loss.item()
    
    avg_loss = total_loss / len(val_loader)
    return avg_loss

def log_validation_loss(epoch, val_loss):
    print(f'Epoch [{epoch}], Validation Loss: {val_loss}')