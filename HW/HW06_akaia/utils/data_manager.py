"""
Google Sheet manager
"""
from urllib.parse import urlparse

import apiclient.discovery  # pylint: disable=import-error
import googleapiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class _SheetManager():
    """
    Google sheet manager.
    Can get data from the sheet, append data to the sheet and pretty print data.
    IMPORTANT:
    User must share google sheet with ngfg-account@ngfg-268019.iam.gserviceaccount.com
    Or give editing access url
    """
    credentials_file = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file,
        [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'])

    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    @staticmethod
    def get_data_with_range(spreadsheet_id, from_row, to_row):
        """
        Get data from google sheet by sheet id with range
        :param spreadsheet_id: str | google shit id, can be gotten from url
            E.G: https://docs.google.com/spreadsheets/d/1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE/edit#gid=0
            spreadsheet_id = '1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE'
        :param from_row: str | cell to begin with. E.G.: 'a', 'A1', 'b3'
        :param to_row: str | cell where search stop. E.G.: 'c', 'C5', 'c3'
        :return: list of lists or None
        """
        try:
            ranges = f'{from_row}:{to_row}'
            values = _SheetManager.service.spreadsheets().values().get(  # pylint: disable=no-member
                spreadsheetId=spreadsheet_id,
                range=ranges,
                majorDimension='ROWS'
            ).execute()

            data = values.get('values')

            if data is not None:
                data = _SheetManager.lists_to_list(data)

            return data

        except googleapiclient.errors.HttpError as error:
            return None

    @staticmethod
    def get_all_data(spreadsheet_id):
        """
        Get all data from google sheet by sheet id
        :param spreadsheet_id: str | google shit id, can be gotten from url
            E.G: https://docs.google.com/spreadsheets/d/1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE/edit#gid=0
            spreadsheet_id = '1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE
        :return: list of lists or None
        """
        try:
            values = _SheetManager.service.spreadsheets().values().get(  # pylint: disable=no-member
                spreadsheetId=spreadsheet_id,
                range='A:ZZZ',
                majorDimension='ROWS'
            ).execute()

            data = values.get('values')

            if data is not None:
                data = _SheetManager.lists_to_list(data)
            return data
        except googleapiclient.errors.HttpError as error:
            return None

    @staticmethod
    def append_data(spreadsheet_id, values: list):
        """
        Append data to google sheet by sheet id
        :param spreadsheet_id: str | google shit id, can be gotten from url
            E.G: https://docs.google.com/spreadsheets/d/1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE/edit#gid=0
            spreadsheet_id = '1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE
        :param values: List | data to append
        :return: True or None
        """
        try:
            if not isinstance(values, list):
                return None

            # check for multiple choice answer
            for index, answer in enumerate(values):
                if isinstance(answer, list):
                    values[index] = ';'.join(answer)

            data = [[element] for element in values]
            resource = {
                "majorDimension": "COLUMNS",
                "values": data
            }
            _SheetManager.service.spreadsheets().values().append(  # pylint: disable=no-member
                spreadsheetId=spreadsheet_id,
                range='A:A',
                body=resource,
                valueInputOption="USER_ENTERED"
            ).execute()

            return True

        except googleapiclient.errors.HttpError as error:
            return None

    @staticmethod
    def get_sheet_id_from_url(url: str):
        """
        Get google sheet id from sheet url
        urlparse = ParseResult(
        scheme='https',
        netloc='docs.google.com',
        path='/spreadsheets/d/1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUEaQgCjzuQmHaM/edit',
        params='',
        query='',
        fragment='gid=0')
        :param url: str | sheet url
        :return: None or str | sheet_id
        """
        try:
            sheet_id_number = 3

            link = urlparse(url)
            sheet_id = link.path.split('/')[sheet_id_number]
            return sheet_id

        except IndexError as error:
            return None

    @staticmethod
    def lists_to_list(data, values=None):
        """
        Gather data from many lists into one list
        :param data: user data
        :param values: list to return
        :return: list
        """
        if values is None:
            values = []

        if data is None:
            return None

        for item in data:
            if isinstance(item, list):
                _SheetManager.lists_to_list(item, values)
            else:
                values.append(item)

        return values

    @staticmethod
    def get_dict(spreadsheet_id):
        """
        Get all data from google sheet by sheet id
        :param spreadsheet_id: str | google shit id, can be gotten from url
            E.G: https://docs.google.com/spreadsheets/d/1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE/edit#gid=0
            spreadsheet_id = '1p0Q49GW9HUXBkd5LmKB9k7TRngc4fUE
        :return: dict
        """
        try:
            values = _SheetManager.service.spreadsheets().values().get(  # pylint: disable=no-member
                spreadsheetId=spreadsheet_id,
                range='A:ZZZ',
                majorDimension='ROWS'
            ).execute()

            data = values.get('values')
            result = {}
            if data is not None:
                for row in data:
                    result.setdefault(row[0], row[1])

            return result
        except googleapiclient.errors.HttpError as error:
            return {}


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Credentials(metaclass=Singleton):
    data = _SheetManager.get_dict("1rr1dzPSwa6qx6jarzbtXdWBSg5DsNsknmn2dWckmnvk")

    def __init__(self, spreadsheet_id):
        print("init Credentials")
        self.data = _SheetManager.get_dict(spreadsheet_id)

    def get_register_email(self):
        return self.data.get("register_login")

    def get_register_password(self):
        return self.data.get("register_password")

    def get_existing_email(self):
        return self.data.get("existing_login")

    def get_existing_password(self):
        return self.data.get("existing_password")
