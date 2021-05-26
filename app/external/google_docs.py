import os
from abc import ABC, abstractmethod


class GoogleDocsAPI(ABC):
    """Abstract class for Google Docs API"""

    @abstractmethod
    def download_template(self, folder_path: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def delete_template(self, folder_path: str) -> None:
        raise NotImplementedError


class GoogleDocsAPIMock(GoogleDocsAPI):
    """
    Mock class for testing, implements methods of GoogleDocsAPI abstract class.
    """

    def download_template(self, folder_path: str) -> str:
        """Simulates downloading and saving template file."""

        file_path = f'{folder_path}/test.txt'
        template_text = """
                Contract
                {name} from one side and
                {company} from another
                """

        with open(file_path, "w+") as f:
            f.write(template_text)

        return file_path

    def delete_template(self, folder_path: str) -> None:
        """Deletes template file."""

        file_path = f'{folder_path}/test.txt'

        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass


class GoogleDocsAPIImpl(GoogleDocsAPI):
    """
    Class implements methods of GoogleDocsAPI abstract class.
    In real application this class should call methods google-api-python-client
    google-auth-httplib2, google-auth-oauthlib libraries for downloading file
    from Google docs.
    """

    def download_template(self, folder_path: str) -> str:
        """Simulates downloading and saving template file."""

        file_path = f'{folder_path}/template.txt'
        template_text = """
        Contract
        {name} from one side and
        {company} from another
        """

        with open(file_path, "w+") as f:
            f.write(template_text)

        return file_path

    def delete_template(self, folder_path: str) -> None:
        """Deletes template file."""

        file_path = f'{folder_path}/template.txt'

        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
