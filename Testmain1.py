import unittest

class TestGitHubAPI(unittest.TestCase):
    def test_get_repo_commits(self):
        get_repo_commits("jdeora")


if __name__ == '__main__':
    unittest.main()


