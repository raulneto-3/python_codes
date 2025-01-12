import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision.transforms as transforms

# Definir a arquitetura do modelo
class DigitRecognitionModel(nn.Module):
    def __init__(self):
        super(DigitRecognitionModel, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten the input
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Instanciar o modelo e carregar os pesos
model = DigitRecognitionModel()
model.load_state_dict(torch.load('neural networks/handwritten digit recognition/digit_recognition.pth'))
model.eval()

# Carregar e processar a imagem
img = cv2.imread('neural networks/handwritten digit recognition/1.png', cv2.IMREAD_GRAYSCALE)
img = np.invert(img)
img = img.astype(np.float32) / 255.0
img = torch.tensor(img).unsqueeze(0).unsqueeze(0)  # Adicionar dimensões de batch e canal

# Fazer a previsão
with torch.no_grad():
    img = img.view(-1, 28*28)  # Flatten the input
    prediction = model(img)
    predicted_class = torch.argmax(prediction, dim=1).item()

print(f'The result is probably: {predicted_class}')
plt.imshow(img.view(28, 28), cmap='gray')
plt.show()