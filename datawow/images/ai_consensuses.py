from datawow.connector import Connector


class AIConsensus():

    def __init__(self, token):
        self.token = token

    def create(self, params=None):
        """Create consensus

        Args:
            data (str): URL of image
            postback_url (str): URL for answer callback once image has been checked
            postback_method (str): Configuration HTTP method GET POST PUT PATCH
            custom_id (str): Custom ID that used for search

        Returns:
            dict: The value containt in Response class as dict.

        """

        return Connector(self.token, model_type="consensus", path="jobs/ai/consensuses/").send(
            method='POST',
            data=params)

    def list(self, params=None):
        """Retrieve list of image closed questions

        Args:
            page (int): Page of data
            per_page (int): Limit of date per page

        Returns:
            dict: The value containt in Response class as dict

         """

        return Connector(self.token, model_type="consensus", path="jobs/ai/consensuses/").send(
            method='GET',
            data=params)

    def find_id(self, image_id=None):
        """Retrieve image by ID or custom ID

        Args:
            image_id (int): Image's ID or custom ID which is you were assigned

        Returns:
            dict: The value containt in Response class as dict

        """

        return Connector(self.token, model_type="consensus", path="jobs/ai/consensuses/").send(
            method='GET',
            doc_id=image_id)
