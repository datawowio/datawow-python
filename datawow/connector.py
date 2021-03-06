import os

from requests import Request, Session

from datawow import errors
from datawow import base_common as base_config
from datawow import responses


class Connector(object):

    def __init__(self, project_key=None, headers=None, base_url=None, model_type=None, path=None):

        if model_type is None or path is None:
            raise AttributeError('Missing class and model')

        if project_key is None:
            if 'Authorization' in os.environ:
                self.project_key = os.environ['Authorization']
            else:
                raise AttributeError('Project key is missing')
        else:
            self.project_key = project_key

        self.headers = self._build_header(headers)

        base_url = base_config.base_url(model_type)

        if path == 'Not found' or base_url == 'Not found':

            raise AttributeError('Incorrect model type for getting URL')

        self.base_api = base_url + path

    def _build_header(self, headers=None):

        if headers is None:
            headers = {}

        headers['Authorization'] = self.project_key
        headers['Accept'] = headers.get('Accept', 'application/json')
        headers['Content-Type'] = headers.get(
            'Content-Type', 'application/x-www-form-urlencoded')

        return headers

    def send(self, method='GET', data=None, query_str=False, doc_id=None):
        url = self.base_api
        builder = None

        if doc_id is not None:
            if query_str is False:
                url = "%s/%s" % (url, doc_id)
            else:
                url = "%s?id=%s" % (url, doc_id)

        session = Session()
        if self.headers['Content-Type'] == 'application/json':
            builder = Request(
                method,
                url,
                json=data,
                headers=self.headers)

        else:
            builder = Request(
                method,
                url,
                data=data,
                headers=self.headers)

        prepare = session.prepare_request(builder)

        response = session.send(prepare)

        if errors._raise_error_by_code(response.status_code):
            return responses.Responses(error_code=response.status_code,
                                       message=response.json())
        else:
            return responses.Responses(code=response.json()
                                       .get('meta').get('code'),
                                       message=response.json()
                                       .get('meta').get('message'),
                                       meta=response.json().get('meta'),
                                       data=response.json()
                                       .get('data'))
