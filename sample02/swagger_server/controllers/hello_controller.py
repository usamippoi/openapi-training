import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_hello(user_name):  # noqa: E501
    """get_hello

    ユーザに挨拶する。 # noqa: E501

    :param user_name: ユーザ名
    :type user_name: str

    :rtype: InlineResponse200
    """
    return 'Hello, ' + user_name  # 変更箇所
