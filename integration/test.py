from mock import patch

from django.test import TestCase

from .client import BinditException
from .task import create_account_and_task


class CreateAcountAndTaskTestCase(TestCase):
    """Unittests for integration.task.create_account_and_task."""

    @patch('integration.client.BinditClient.create_account')
    @patch('integration.client.BinditClient.create_transfer')
    def test_expected(self, mock_create_account, mock_create_transfer):
        """
        Test the happy case, no expected behaviour.
        """
        mock_create_account.return_value = {'id': 45, 'name': 'gerbil'}
        mock_create_transfer.return_value = {'id': 67, 'amount': 12, 'account': 45}

        create_account_and_task('gerbil', 12)

    @patch('integration.client.BinditClient.create_account')
    @patch('integration.client.BinditClient.create_transfer')
    def test_account_call_fails(self, mock_create_account, mock_create_transfer):
        """
        Test the case when creating the account in Bindit fails.
        """
        mock_create_account.side_effect = BinditException()
        mock_create_transfer.return_value = {'id': 67, 'amount': 12, 'account': 45}

        create_account_and_task('gerbil', 12)

    @patch('integration.client.BinditClient.create_account')
    @patch('integration.client.BinditClient.create_transfer')
    def test_transfer_call_fails(self, mock_create_account, mock_create_transfer):
        """
        Test the case when creating the transfer in Bindit fails.
        """
        mock_create_account.return_value = {'id': 45, 'name': 'gerbil'}
        mock_create_transfer.side_effect = BinditException()

        create_account_and_task('gerbil', 12)

    @patch('integration.client.BinditClient.create_account')
    @patch('integration.client.BinditClient.create_transfer')
    def test_account_transfer_call_fails(self, mock_create_account, mock_create_transfer):
        """
        Test the case when creating both the account and transfer in Bindit fails.
        """
        mock_create_account.side_effect = BinditException()
        mock_create_transfer.side_effect = BinditException()

        create_account_and_task('gerbil', 12)


