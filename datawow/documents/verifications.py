from datawow.connector import Connector


class Verification():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create image choices

        Args:
            data (str): URL of image
            postback_url (str): URL for answer callback once image has been checked
            postback_method (str): Configuration HTTP method GET POST PUT PATCH

        Returns:
            dict: The value containt in Response class as dict

        """
        return Connector(self.token, model_type="docs",
                         path="images/document_verifications/",
                         headers={'Content-Type': 'application/json'}).send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of image

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="docs", path="images/document_verifications/").send(
            method='GET',
            data=params)

    def find_id(self, doc_id=None):
        """Retrieve image by ID or custom ID

        Args:
            image_id (int): Image's ID or custom ID which is you were assigned

        Returns:

        """

        return Connector(self.token, model_type="docs", path="images/document_verifications/").send(
            method='GET',
            doc_id=doc_id)
