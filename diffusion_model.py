import torch
import torch.nn as nn
import torch.optim as optim

class DiffusionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super(DiffusionModel, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers)
        self.fc = nn.Linear(hidden_dim, input_dim)
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.fc(lstm_out)
        return output

def forward_diffusion(x, timesteps, noise_schedule):
    """Add noise progressively over time using Gaussian noise with variance."""
    for t in range(timesteps):
        noise = torch.randn_like(x) * noise_schedule[t]
        x = x + noise
    return x


def reverse_diffusion(model, noisy_data, timesteps, noise_schedule):
    """Reverse the noise to reconstruct the original code using learned denoising."""
    for t in reversed(range(timesteps)):
        noisy_data = model(noisy_data)  # Denoise using model
    return noisy_data

# Hyperparameters
input_dim = 512  # Adjust based on your tokenized input
hidden_dim = 512
num_layers = 2
timesteps = 1000
noise_schedule = torch.linspace(0, 1, timesteps)  # Linear schedule of noise

# Initialize model and optimizer
model = DiffusionModel(input_dim, hidden_dim, num_layers)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.MSELoss()  # Using MSE loss for denoising task

# Save Checkpoint
def save_checkpoint(model, optimizer, epoch, loss, path="diffusion_checkpoint.pth"):
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss
    }, path)
    print(f"Checkpoint saved at epoch {epoch}")

# Load Checkpoint
def load_checkpoint(model, optimizer, path="diffusion_checkpoint.pth"):
    if torch.cuda.is_available():
        checkpoint = torch.load(path)
    else:
        checkpoint = torch.load(path, map_location=torch.device('cpu'))
    
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']
    print(f"Checkpoint loaded: Epoch {epoch}, Loss: {loss}")
    return epoch, loss

def train_diffusion_model(model, optimizer, criterion, num_epochs=10, checkpoint_interval=5):
    start_epoch = 0
    try:
        start_epoch, _ = load_checkpoint(model, optimizer)
    except FileNotFoundError:
        print("No checkpoint found, starting from scratch.")
    
    for epoch in range(start_epoch, num_epochs):
        inputs = torch.randn(32, input_dim)  # Example random input; replace with actual data
        noisy_inputs = forward_diffusion(inputs, timesteps, noise_schedule)
        
        optimizer.zero_grad()
        
        # Reverse diffusion process
        denoised_outputs = reverse_diffusion(model, noisy_inputs, timesteps, noise_schedule)
        
        # Loss calculation
        loss = criterion(denoised_outputs.view(-1, input_dim), inputs.view(-1, input_dim))
        loss.backward()
        optimizer.step()
        
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
        
        # Save checkpoint at specified interval
        if (epoch + 1) % checkpoint_interval == 0:
            save_checkpoint(model, optimizer, epoch+1, loss.item())

train_diffusion_model(model, optimizer, criterion)
