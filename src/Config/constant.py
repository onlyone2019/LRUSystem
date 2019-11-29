# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : Pycharm
#   File name   : constant.py
#   Author      : WangJin
#   Created date: 2019-11-29 12:19:26
#   Description : 常量验证性文件（不需要改动）
#
#================================================================
class Const():
    class ConstError(TypeError): pass

    class ConstCaseError(ConstError): pass

    def __setattr__(self, key, value):
        print()
        if key in self.__dict__.keys():
            # 存在性验证
            raise self.ConstError("Can't change a const variable: '%s'" % key)

        if not key.isupper():
            # 语法规范验证
            raise self.ConstCaseError("Const variable must be combined with upper letters:'%s'" % key)

        self.__dict__[key] = value


