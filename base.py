# coding: utf-8
"""
システム名: SATLYS設計標準FW
モジュール名: satlys_nnfw.baseモジュール
バージョン: v1.0

このプログラムの著作権は東芝デジタルソリューションズ株式会社にあります。
ファイルの内容の一部または全てを無断で使用および転載することは禁止されています。
Copyright (c) 2018 Toshiba Digital Solutions Corporation. All Rights Reserved.

本技術情報には当社の機密情報が含まれておりますので、当社の書面による承諾がなく第三者に開示することはできません。
また、当社の承諾を得た場合であっても、本技術情報は外国為替及び外国貿易管理法に定める特定技術に該当するため、
非居住者に提供する場合には、同法に基づく許可を要することがあります。
東芝デジタルソリューションズ 株式会社
"""

import os
from abc import ABCMeta, abstractmethod
from six import with_metaclass
import datetime
import copy
import warnings

from utils import load_config

#
# class AbstractTrainer():
#     """
#     Trainer抽象クラス. 学習機能を提供する.
#     """
#
#     model_conf = None
#     model = None
#     model_dir = None
#
#     def __init__(self, data_dir='./', work_dir='./'):
#         self.data_dir = data_dir
#         self.work_dir = work_dir
#
#     def initialize(self, model_configuration_path, model_factory_class, model_factory=None):
#         """
#         初期化メソッド.
#         :param model_configuration_path: モデル設定ファイルへのパス
#         :param model_factory_class: 利用するSATLYSModelFactoryの具象クラス
#         :param model_factory: 利用するSATLYSModelFactoryのインスタンスを指定する場合に与える
#         """
#         if model_configuration_path is None:
#             warnings.warn(ConfigurationFileWarning(
#                 _WARN_COMMON_NO_MODEL_CONF, model_configuration_path), error_code='001')
#             self.model_conf = {}
#         else:
#             self.model_conf = load_config(model_configuration_path)
#
#         if utils.KEY_MODEL_OUTPUT in self.model_conf.keys() \
#                 and self.model_conf[utils.KEY_MODEL_OUTPUT] is not None:
#             self.model_dir = os.path.dirname(os.path.join(
#                 self.work_dir, self.model_conf[utils.KEY_MODEL_OUTPUT])
#             )
#             if not os.path.exists(self.model_dir):
#                 os.makedirs(self.model_dir)
#
#         if model_factory_class is None and model_factory is None:
#             raise ModelFactoryError(_ERR_COMMON_NO_MODEL_FACTORY, error_code='001')
#         elif model_factory is None:
#             model_factory = model_factory_class()
#
#         if utils.KEY_IS_FINE_TUNE in self.model_conf.keys() \
#                 and self.model_conf[utils.KEY_IS_FINE_TUNE] == 1:
#             self.model = model_factory.load_model(self.model_conf)
#         else:
#             self.model = model_factory.create_model(self.model_conf)
#
#         if self.model is None:
#             raise ModelFactoryError(_ERR_TRAINER_NO_MODEL_STRUCTURE_CONFIGURED, error_code='002')
#
#     def train_model(self, exe_conf={}, exe_conf_path=None):
#         """
#         学習処理のラッパー関数.
#         :param exe_conf: 学習実行時のパラメータリスト
#         :param exe_conf_path: 学習実行パラメータファイルへのパス
#         """
#         if self.model_conf is None:
#             raise NotInitializedError(_ERR_COMMON_CALL_INIT_FIRST.format(['The trainer']), error_code='001')
#
#         temp_conf = copy.deepcopy(exe_conf)
#         if exe_conf_path is not None:
#             temp_conf.update(load_config(exe_conf_path))
#
#         merged_conf = copy.deepcopy(self.model_conf)
#         merged_conf[utils.KEY_START_DATE] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#         merged_conf.update(temp_conf)
#         report = Report(merged_conf, self.work_dir)
#
#         result = self._train_model(self.model, self.data_dir, merged_conf)
#         model = result[0]
#         if len(result) > 1:
#             loss_report = result[1]
#         else:
#             loss_report = []
#         if len(result) > 2:
#             additional = result[2:]
#         else:
#             additional = []
#
#         print(merged_conf)
#
#         if model is None:
#             raise TrainingResultsError(
#                 _ERR_TRAINER_NO_MODEL_TRAINED.format([self.model_conf, exe_conf]), error_code='001')
#         if loss_report is None:
#             warnings.warn(TrainingResultsWarning(
#                 _WARN_TRAINER_NO_REPORTS_RETURNED.format([model, self.model_conf, exe_conf]), error_code='001'))
#         if additional is None:
#             warnings.warn(TrainingResultsWarning(
#                 _WARN_TRAINER_NO_ADDITIONAL_RETURNED.format([model, self.model_conf, exe_conf]), error_code='002'))
#         self._store_model(model, self.model_dir, merged_conf)
#         report.write_report(merged_conf, loss_report, additional)
#
#     @abstractmethod
#     def _train_model(self, model, data_dir, merged_conf):
#         """
#         学習処理を行う抽象メソッド.
#         :param model: モデル
#         :param data_dir: データディレクトリのパス
#         :param merged_conf: モデルの設定情報と学習実行時のパラメータがマージされたdict
#         :return: モデル, 損失情報, 補足情報(任意)
#         """
#         pass
#
#     @abstractmethod
#     def _store_model(self, model, model_dir_path, merged_conf):
#         """
#         学習済みモデルの保存を行う抽象メソッド.
#         :param model: 学習済みモデル
#         :param model_dir_path: モデルの出力先ディレクトリ
#         :param merged_conf: モデルの設定情報と学習実行時のパラメータがマージされたdict
#         """
#         pass
#
#
# class AbstractPredictor(with_metaclass(ABCMeta)):
#     """
#     Predictor抽象クラス. モデルを用いた推論機能を提供する.
#     """
#
#     model_conf = None
#     model = None
#     model_dir_path = None
#
#     def __init__(self, data_dir='./', work_dir='./'):
#         self.data_dir = data_dir
#         self.work_dir = work_dir
#
#     def initialize(self, model_configuration_path, model_factory_class, model_factory=None):
#         """
#         初期化メソッド.
#         :param model_configuration_path: モデル設定ファイルへのパス
#         :param model_factory_class: 利用するSATLYSModelFactoryの具象クラス
#         :param model_factory: 利用するSATLYSModelFactoryのインスタンスを指定する場合に与える
#         """
#
#         if model_configuration_path is None:
#             warnings.warn(ConfigurationFileWarning(_WARN_COMMON_NO_MODEL_CONF, error_code='002'))
#             self.model_conf = {}
#         else:
#             self.model_conf = load_config(model_configuration_path)
#
#         if utils.KEY_MODEL_OUTPUT in self.model_conf.keys() \
#                 and self.model_conf[utils.KEY_MODEL_OUTPUT] is not None:
#             self.model_dir_path = os.path.dirname(os.path.join(
#                 self.work_dir, self.model_conf[utils.KEY_MODEL_OUTPUT])
#             )
#
#         if model_factory_class is None and model_factory is None:
#             raise ModelLoadError(_ERR_COMMON_NO_MODEL_FACTORY, error_code='003')
#         elif model_factory is None:
#             model_factory = model_factory_class()
#
#         self.model = model_factory.load_model(self.model_dir_path, self.model_conf)
#         if self.model_conf is None:
#             raise ModelLoadError(_ERR_PREDICTOR_NO_MODELS_LOADED, error_code='004')
#
#     def batch_predict(self, data_dir, exe_conf={}, exe_conf_path=None):
#         """
#                 推論処理のラッパー関数.
#                 :param data_dir: データディレクトリ
#                 :param exe_conf: 推論実行時のパラメータ
#                 :param exe_conf_path: 推論実行パラメータファイルへのパス
#                 :return: 推論結果
#                 """
#
#         if self.model_conf is None:
#             raise NotInitializedError(_ERR_COMMON_CALL_INIT_FIRST.format(['The predictor']), error_code='001')
#
#         temp_conf = copy.deepcopy(exe_conf)
#         if exe_conf_path is not None:
#             temp_conf.update(load_config(exe_conf_path))
#
#         merged_conf = copy.deepcopy(self.model_conf)
#         merged_conf.update(temp_conf)
#         result = self._batch_predict(self.model, data_dir, merged_conf)
#         return result
#
#     def predict(self, input_data, exe_conf={}, exe_conf_path=None):
#         """
#         推論処理のラッパー関数.
#         :param input_data: 入力データ
#         :param exe_conf: 推論実行時のパラメータ
#         :param exe_conf_path: 推論実行パラメータファイルへのパス
#         :return: 推論結果
#         """
#
#         if self.model_conf is None:
#             raise NotInitializedError(_ERR_COMMON_CALL_INIT_FIRST.format(['The predictor']), error_code='001')
#
#         temp_conf = copy.deepcopy(exe_conf)
#         if exe_conf_path is not None:
#             temp_conf.update(load_config(exe_conf_path))
#
#         merged_conf = copy.deepcopy(self.model_conf)
#         merged_conf.update(temp_conf)
#         result = self._predict(self.model, input_data, merged_conf)
#         if result is None:
#             raise PredictionResultsError(
#                 _ERR_PREDICTOR_NO_RESULTS.format(self.model, self.model_conf, exe_conf), error_code='001')
#         return result
#
#     @abstractmethod
#     def _batch_predict(self, model, data_dir, merged_conf):
#         """
#         推論処理を行う抽象メソッド.
#         :param model: 使用する学習済みモデル
#         :param data_dir: データディレクトリ
#         :param merged_conf: モデルの設定情報と学習実行時のパラメータがマージされたdict
#         :return: 推論結果
#         """
#         pass
#
#     @abstractmethod
#     def _predict(self, model, input_data, merged_conf):
#         """
#         推論処理を行う抽象メソッド.
#         :param model: 使用する学習済みモデル
#         :param input_data: 入力データ
#         :param merged_conf: モデルの設定情報と学習実行時のパラメータがマージされたdict
#         :return: 推論結果
#         """
#         pass


class AbstractModelFactory:
    """
    ModelFactory抽象クラス.
    """

    @abstractmethod
    def create_model(self, model_configuration):
        """
        モデルを生成する抽象メソッド.
        :param model_configuration: モデル設定情報
        :return: モデル
        """
        pass

    @abstractmethod
    def load_model(self, model_dir_path, model_configuration):
        """
        学習済みモデルを読み込む抽象メソッド.
        :param model_dir_path: モデルのディレクトリ
        :param model_configuration: モデルの設定情報
        :return: 学習済みモデル
        """
        pass


class AbstractModel:
    """
    Model抽象クラス.
    """
    pass


class AbstractPreProcessor:
    """
    前処理用抽象クラス.
    """
    pass
