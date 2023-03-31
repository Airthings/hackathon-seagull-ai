# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GptMessageRes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message: str=None, status_code: int=None, conversation_id: str=None):  # noqa: E501
        """GptMessageRes - a model defined in Swagger

        :param message: The message of this GptMessageRes.  # noqa: E501
        :type message: str
        :param status_code: The status_code of this GptMessageRes.  # noqa: E501
        :type status_code: int
        :param conversation_id: The conversation_id of this GptMessageRes.  # noqa: E501
        :type conversation_id: str
        """
        self.swagger_types = {
            'message': str,
            'status_code': int,
            'conversation_id': str
        }

        self.attribute_map = {
            'message': 'message',
            'status_code': 'status_code',
            'conversation_id': 'conversation_id'
        }
        self._message = message
        self._status_code = status_code
        self._conversation_id = conversation_id

    @classmethod
    def from_dict(cls, dikt) -> 'GptMessageRes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The gptMessageRes of this GptMessageRes.  # noqa: E501
        :rtype: GptMessageRes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this GptMessageRes.


        :return: The message of this GptMessageRes.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this GptMessageRes.


        :param message: The message of this GptMessageRes.
        :type message: str
        """

        self._message = message

    @property
    def status_code(self) -> int:
        """Gets the status_code of this GptMessageRes.


        :return: The status_code of this GptMessageRes.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int):
        """Sets the status_code of this GptMessageRes.


        :param status_code: The status_code of this GptMessageRes.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def conversation_id(self) -> str:
        """Gets the conversation_id of this GptMessageRes.


        :return: The conversation_id of this GptMessageRes.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str):
        """Sets the conversation_id of this GptMessageRes.


        :param conversation_id: The conversation_id of this GptMessageRes.
        :type conversation_id: str
        """

        self._conversation_id = conversation_id