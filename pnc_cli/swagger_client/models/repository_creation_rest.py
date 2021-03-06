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


class RepositoryCreationRest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RepositoryCreationRest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'repository_configuration_rest': 'RepositoryConfigurationRest',
            'build_configuration_rest': 'BuildConfigurationRest'
        }

        self.attribute_map = {
            'repository_configuration_rest': 'repositoryConfigurationRest',
            'build_configuration_rest': 'buildConfigurationRest'
        }

        self._repository_configuration_rest = None
        self._build_configuration_rest = None

    @property
    def repository_configuration_rest(self):
        """
        Gets the repository_configuration_rest of this RepositoryCreationRest.


        :return: The repository_configuration_rest of this RepositoryCreationRest.
        :rtype: RepositoryConfigurationRest
        """
        return self._repository_configuration_rest

    @repository_configuration_rest.setter
    def repository_configuration_rest(self, repository_configuration_rest):
        """
        Sets the repository_configuration_rest of this RepositoryCreationRest.


        :param repository_configuration_rest: The repository_configuration_rest of this RepositoryCreationRest.
        :type: RepositoryConfigurationRest
        """
        self._repository_configuration_rest = repository_configuration_rest

    @property
    def build_configuration_rest(self):
        """
        Gets the build_configuration_rest of this RepositoryCreationRest.


        :return: The build_configuration_rest of this RepositoryCreationRest.
        :rtype: BuildConfigurationRest
        """
        return self._build_configuration_rest

    @build_configuration_rest.setter
    def build_configuration_rest(self, build_configuration_rest):
        """
        Sets the build_configuration_rest of this RepositoryCreationRest.


        :param build_configuration_rest: The build_configuration_rest of this RepositoryCreationRest.
        :type: BuildConfigurationRest
        """
        self._build_configuration_rest = build_configuration_rest

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
		result[attr] = str(value.date())
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
