'''
 # @ Author: Jeff Chen
 # @ Create Time: 2023-10-19 14:45:27
 # @ Description:
 '''

import platform
import os
import HP_global as g
import time

# 数据主目录
# 当前路径
PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
g.datapath = os.path.join(PROJECT_PATH, 'xbdata')
g.grppath = os.path.join(PROJECT_PATH, 'xbjq')

# 软件
g.root = None
g.name = '小白量化投资平台'
g.title = '1.0 版 开发者：Jeff Chen'
g.ico = 'tt.ico'
g.winW = 1200
g.winH = 800
g.ver = 1.0
g.user = 'admin'
g.login = False
g.os = 3

# 白底色
g.ubg = 'w'
g.ufg = 'b'
g.utg = 'b'
g.uvg = '#1E90FF'


# TODO 其它全局配置


# 调试输出开关
g.isDebug = True

