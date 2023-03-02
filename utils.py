# coding: utf-8
"""
システム名: SATLYS設計標準FW
モジュール名: satlys_nnfw.utilsモジュール
バージョン: v1.0

このプログラムの著作権は東芝デジタルソリューションズ株式会社にあります。
ファイルの内容の一部または全てを無断で使用および転載することは禁止されています。
Copyright (c) 2018 Toshiba Digital Solutions Corporation. All Rights Reserved.

本技術情報には当社の機密情報が含まれておりますので、当社の書面による承諾がなく第三者に開示することはできません。
また、当社の承諾を得た場合であっても、本技術情報は外国為替及び外国貿易管理法に定める特定技術に該当するため、
非居住者に提供する場合には、同法に基づく許可を要することがあります。
東芝デジタルソリューションズ 株式会社
"""
import json


def load_config(path):
    """

    """

    conf_file = open(path, 'r')
    conf = json.load(conf_file)
    return conf


# def json_serializer(obj):
#     """
#     JSONオブジェクトをシリアライズする.
#     :param obj: JOSNオブジェクト
#     :return: シリアライズした結果
#     """
#     # datetime.dateはJSON serializableではないので、文字列に変換する
#     if isinstance(obj, date):
#         return str(obj)
#
#     # datetime.date以外にJSON serializableではないものが、merged_confに含まれていたらwarningを挙げる
#     warnings.warn(ConfigurationFileWarning('{} is not JSON serializable'.format(type(obj)),
#                                            error_code='001'))
#     return str(obj)

