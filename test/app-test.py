import unittest
from ailola import get_relevant

class TestAilola(unittest.TestCase):
    def test_get_relevant(self):
        # Test create_terraform
        prompt = get_relevant('create_terraform', 'Generate a Terraform template')
        self.assertEqual(prompt[0]['role'], 'system')
        self.assertIn('You are a file name generator', prompt[0]['content'])
        self.assertIn('only generate valid names for Terraform templates', prompt[0]['content'])
        self.assertEqual(prompt[1]['role'], 'user')
        self.assertEqual(prompt[1]['content'], 'Generate a Terraform template')

        # Test validate_terraform
        prompt = get_relevant('validate_terraform', 'Validate a Terraform template')
        self.assertEqual(prompt[0]['role'], 'system')
        self.assertIn('You are a Terraform HCL validator', prompt[0]['content'])
        self.assertIn('only validate valid Terraform HCL templates', prompt[0]['content'])
        self.assertEqual(prompt[1]['role'], 'user')
        self.assertEqual(prompt[1]['content'], 'Validate a Terraform template')

        # Test create_k8s
        prompt = get_relevant('create_k8s', 'Generate a k8s template')
        self.assertEqual(prompt[0]['role'], 'system')
        self.assertIn('You are a k8s template generator', prompt[0]['content'])
        self.assertIn('only generate valid k8s templates', prompt[0]['content'])
        self.assertEqual(prompt[1]['role'], 'user')
        self.assertEqual(prompt[1]['content'], 'Generate a k8s template')

        # Test debug
        prompt = get_relevant('debug', 'Validate Jenkins console log')
        self.assertEqual(prompt[0]['role'], 'system')
        self.assertIn('You are a validator for jenkins', prompt[0]['content'])
        self.assertIn('only validate jenkins console log', prompt[0]['content'])
        self.assertEqual(prompt[1]['role'], 'user')
        self.assertEqual(prompt[1]['content'], 'Validate Jenkins console log')

if __name__ == '__main__':
    unittest.main()