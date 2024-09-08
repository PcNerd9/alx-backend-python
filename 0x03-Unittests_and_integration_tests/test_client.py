#!/usr/bin/env python3

"""
Test cases for the GithubOrgClient class
"""

import unittest
from parameterized import parameterized, parameterized_class
from typing import Mapping
from unittest.mock import Mock, patch, PropertyMock
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient
    """
    @parameterized.expand([
        "google",
        "abc"
        ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get: Mock) -> str:
        """
        test the org property
        """
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.return_value = {"payload": True}
        github = GithubOrgClient(org_name)
        self.assertEqual(github.org, {"payload": True})
        self.assertEqual(github.org, {"payload": True})
        mock_get.assert_called_once_with(url)

    def test_public_repos_url(self) -> str:
        """
        test the _public_repos_url attribute
        """

        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "some url"}
            github = GithubOrgClient("google")
            self.assertEqual(github._public_repos_url, "some url")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        test the public_repo
        """
        mock_get_json.return_value = [{"name": "truth"},
                                      {"name": "autoparse"},
                                      {"name": "Grapql"},
                                      {"name": "Apache"},
                                      {"name": "dagger"}]
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos_url:
            value = "https://api.github.com/orgs/google/repos"
            mock_repos_url.return_value = value
            github = GithubOrgClient("google")

            self.assertEqual(github.public_repos(), ["truth",
                                                     "autoparse",
                                                     "Grapql",
                                                     "Apache",
                                                     "dagger"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Mapping,
                         license_key: str, output: bool) -> None:
        """
        testing if has_license work perfectly
        """

        github = GithubOrgClient("google")
        self.assertEqual(github.has_license(repo, license_key), output)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
        }
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        create and start a patcher to the requests.get method
        and make sure the mock of requests.get(url).json()
        returns
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        cls.fixtures = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload
                }

        def get_side_effect(url: str) -> Mock:
            """
            return a mock object with a particular return value
            based on the input to the parent mock
            """
            mock_response = Mock()
            mock_response.json.return_value = cls.fixtures[url]

            return mock_response
        cls.mock_get.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """
        stop the patcher created when setting up
        the class
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        test if the public_repos method of the
        GithubOrgClient produce the expected output
        without input
        """

        github = GithubOrgClient("google")
        self.assertEqual(github.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        test if the public_repos method of the
        GithubOrgClient give the expected output with input
        """
        github = GithubOrgClient("google")
        self.assertEqual(github.public_repos(license="apache-2.0"),
                         self.apache2_repos)
