import unittest
from src.utils.logging import setup_logging
from src.utils.saving_loading import save_model, load_model
import torch
import os

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.model = torch.nn.Linear(10, 2)  # Simple model for testing
        self.model_path = 'test_model.pth'

    def test_save_model(self):
        save_model(self.model, self.model_path)
        self.assertTrue(os.path.exists(self.model_path))

    def test_load_model(self):
        save_model(self.model, self.model_path)
        new_model = torch.nn.Linear(10, 2)
        load_model(new_model, self.model_path)
        self.assertEqual(list(new_model.parameters())[0].size(), list(self.model.parameters())[0].size())

    def tearDown(self):
        if os.path.exists(self.model_path):
            os.remove(self.model_path)

if __name__ == '__main__':
    unittest.main()