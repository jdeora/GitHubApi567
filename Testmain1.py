import unittest
from main1 import get_repo_commits

class TestGitHubAPI(unittest.TestCase):
    def test_get_repo_commits(self):
        get_repo_commits("jdeora")
    def test_invalid_user_id():
    with pytest.raises(Exception):
        get_repo_commits("invalid_user_id")
    def test_private_repos():
        get_repo_commits("user_with_private_repos")
    # Assert that no output for private repositories
    def test_empty_repo():
        get_repo_commits("user_with_empty_repo")
    # Assert that "Number of commits: 0" for empty repositories


if __name__ == '__main__':
    unittest.main()


