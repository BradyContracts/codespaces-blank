import torch
import torch.optim as optim
import logging
from torch.utils.data import DataLoader
from src.model.architecture import DiffusionModel
from src.data.preprocessing import preprocess_data
from src.data.augmentation import augment_data
from src.utils.saving_loading import save_model

def train_model(train_loader, val_loader, vocab_size, num_epochs=10, learning_rate=0.001):
    embedding_dim = 256
    hidden_dim = 512

    model = DiffusionModel(vocab_size, embedding_dim, hidden_dim)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs.view(-1, vocab_size), targets.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        scheduler.step()
        avg_loss = total_loss / len(train_loader)
        logging.info(f'Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss}')

    return model

def main():
    # Placeholder for loading data and preparing DataLoader
    # train_loader, val_loader, vocab_size = load_data()
    
    # Example usage
    # model = train_model(train_loader, val_loader, vocab_size)
    # save_model(model, 'diffusion_model.pth')

if __name__ == "__main__":
    main()