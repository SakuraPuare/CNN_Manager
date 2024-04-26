from torch import nn
from torch.nn import functional as F


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # convolutional layer
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 16, 3, padding=1)
        # max pooling layer
        self.pool = nn.MaxPool2d(2, 2)

        # Fully connected layer
        self.fc1 = nn.Linear(16 * 4 * 4, 10)

        # Dropout
        self.dropout = nn.Dropout(p=0.2)

        # Output layer
        self.out = nn.LogSoftmax(dim=1)

    def flatten(self, x):
        return x.view(x.size()[0], -1)

    def forward(self, x):
        # add sequence of convolutional and max pooling layers
        x = self.dropout(self.pool(F.relu(self.conv1(x))))
        x = self.dropout(self.pool(F.relu(self.conv2(x))))
        x = self.dropout(self.pool(F.relu(self.conv3(x))))
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.out(x)
        return x
