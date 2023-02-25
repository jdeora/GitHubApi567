import unittest
from main1 import get_repo_commits

class TestGitHubAPI(unittest.TestCase):
    def test_get_repo_commits(self):
        get_repo_commits("jdeora")
    def test_get_repo_commits(self):
        get_repo_commits("john145")
    def test_get_repo_commits(self):
        get_repo_commits("nouser")


if __name__ == '__main__':
    unittest.main()


