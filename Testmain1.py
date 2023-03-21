import unittest
import pytest
from main1 import get_repo_commits

class TestGitHubAPI(unittest.TestCase):
    def test_get_repo_commits(self):
        get_repo_commits("jdeora")
    
    def test_invalid_user_id(self):
        with self.assertRaises(Exception):
            get_repo_commits("invalid_user_id")
    
    def test_private_repos(self):
        with self.assertRaises(Exception):
            get_repo_commits("user_with_private_repos")
    
    def test_empty_repo(self):
        with self.assertRaises(Exception):
            get_repo_commits("user_with_empty_repo")

if __name__ == '__main__':
    unittest.main()


