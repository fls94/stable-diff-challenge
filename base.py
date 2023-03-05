# coding: utf-8
"""

"""

import os
from abc import ABCMeta, abstractmethod
from six import with_metaclass
import datetime
import copy
import warnings

from utils import load_config


class AbstractModelFactory:
    """
    ModelFactory抽象クラス.
    """

    @abstractmethod
    def create_model(self, model_configuration):
        """

        """
        pass

    @abstractmethod
    def load_model(self, model_dir_path, model_configuration):
        """

        """
        pass


