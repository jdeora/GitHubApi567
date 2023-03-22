import unittest
from unittest.mock import patch, Mock
from main import get_repo_commits


class TestGitHubAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_repo_commits(self, mock_get):
        mock_response = Mock()
        mock_response.text = '[{"name": "repo1"}, {"name": "repo2"}]'
        mock_get.return_value = mock_response

        mock_commit_responses = [
            Mock(),  #for repo1
            Mock()   #for repo2
        ]
        mock_commit_responses[0].text = '[{"commit": {"message": "message 1"}}]'
        mock_commit_responses[1].text = '[{"commit": {"message": "message 2"}}]'

        mock_get.side_effect = [
            mock_response,           #for repo list
            mock_commit_responses[0], #for repo1 commits
            mock_commit_responses[1]  #repo2 commits
        ]

        get_repo_commits("jdeora")


        mock_get.assert_has_calls([

            unittest.mock.call('https://api.github.com/users/jdeora/repos'),
            unittest.mock.call('https://api.github.com/repos/jdeora/repo1/commits'),
            unittest.mock.call('https://api.github.com/repos/jdeora/repo2/commits')
        ])

    @patch('requests.get')
    def test_invalid_user_id(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 1
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_repo_commits("invalid_user_id")

        mock_get.assert_called_once_with('https://api.github.com/users/invalid_user_id/repos')

    @patch('requests.get')
    def test_private_repos(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 2
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_repo_commits("user_with_private_repos")

        mock_get.assert_called_once_with('https://api.github.com/users/user_with_private_repos/repos')

    @patch('requests.get')
    def test_empty_repo(self, mock_get):
        mock_response = Mock()
        mock_response.text = '[]'
        mock_get.return_value = mock_response

        get_repo_commits("user_with_empty_repo")

        mock_get.assert_called_once_with('https://api.github.com/users/user_with_empty_repo/repos')


if __name__ == '__main__':
    unittest.main()
