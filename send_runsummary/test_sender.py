import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from sender import Sender


class TestSenderGoogleSheetsConnection(unittest.TestCase):
    def setUp(self):
        """Set up common test fixtures"""
        self.dummy_args = ["send_runsummary.py"]
        self.mock_sheet = MagicMock()
        self.mock_gc = MagicMock()
        self.mock_gc.open.return_value.sheet1 = self.mock_sheet

    @patch("gspread.service_account")
    def test_init_worksheet_connection(self, mock_service_account):
        """Test Google Sheets connection initialization"""
        mock_service_account.return_value = self.mock_gc

        sender = Sender(self.dummy_args)

        # Verify service account setup
        json_path = str(
            next((Path(__file__).parent.parent / "send_runsummary/json").glob("*.json"))
        )
        mock_service_account.assert_called_once_with(filename=json_path)

        # Verify worksheet initialization
        mock_gc_open_args = sender._Sender__config["runsummary_config"]["sheetname"]
        self.mock_gc.open.assert_called_once_with(mock_gc_open_args)
        self.assertEqual(sender._Sender__worksheet, self.mock_sheet)

    @patch("gspread.service_account")
    def test_read_worksheet(self, mock_service_account):
        """Test worksheet read operations"""
        mock_service_account.return_value = self.mock_gc
        test_data = [{"column1": "value1", "column2": "value2"}]
        self.mock_sheet.get_all_records.return_value = test_data

        sender = Sender(self.dummy_args)
        records = sender._Sender__worksheet.get_all_records()

        self.assertEqual(records, test_data)
        self.mock_sheet.get_all_records.assert_called_once()

    @patch("gspread.service_account")
    def test_write_worksheet(self, mock_service_account):
        """Test worksheet write operations"""
        mock_service_account.return_value = self.mock_gc
        mock_cell = MagicMock()
        self.mock_sheet.range.return_value = [mock_cell]

        sender = Sender(self.dummy_args)
        test_data = {"runnumber": "1"}
        test_size = "10MB"

        sender._Sender__update_worksheet(test_data, test_size)

        self.mock_sheet.range.assert_called_once()
        self.mock_sheet.update_cells.assert_called_once()


if __name__ == "__main__":
    unittest.main()
