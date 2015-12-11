# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class ErrorResponseRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ErrorResponseRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_type': 'str',
            'error_message': 'str',
            'details': 'object'
        }

        self.attribute_map = {
            'error_type': 'errorType',
            'error_message': 'errorMessage',
            'details': 'details'
        }

        self._error_type = None
        self._error_message = None
        self._details = None

    @property
    def error_type(self):
        """
        Gets the error_type of this ErrorResponseRest.


        :return: The error_type of this ErrorResponseRest.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """
        Sets the error_type of this ErrorResponseRest.


        :param error_type: The error_type of this ErrorResponseRest.
        :type: str
        """
        self._error_type = error_type

    @property
    def error_message(self):
        """
        Gets the error_message of this ErrorResponseRest.


        :return: The error_message of this ErrorResponseRest.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ErrorResponseRest.


        :param error_message: The error_message of this ErrorResponseRest.
        :type: str
        """
        self._error_message = error_message

    @property
    def details(self):
        """
        Gets the details of this ErrorResponseRest.


        :return: The details of this ErrorResponseRest.
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ErrorResponseRest.


        :param details: The details of this ErrorResponseRest.
        :type: object
        """
        self._details = details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, datetime):
                result[attr] = str(value)
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
