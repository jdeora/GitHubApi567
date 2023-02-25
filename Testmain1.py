import unittest
from main1 import get_repo_commits

class TestGitHubAPI(unittest.TestCase):
    def test_get_repo_commits(self):
        get_repo_commits("jdeora")


if __name__ == '__main__':
    unittest.main()


