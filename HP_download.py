'''
 # @ Author: Jeff Chen
 # @ Create Time: 2023-10-20 14:18:18
 # @ Description: 下载股票信息工具
 '''

import os
import time
from dotenv import load_dotenv
import tushare as ts
import HP_global as g
from HP_set import *


# 获取指定股票的k线信息
# 从配置中读取token，在通过sdk获取数据
load_dotenv()
token = os.getenv("TUSHARE_TOKEN")
# 指定的股票代码，6位数字+.+SZ或SH，参考网上公开的股票代号，多个代码用,分割
ts_code_names = os.getenv("TS_CODE_NAMES")
ts_codes = []
if ',' in ts_code_names:
    _codes = str(ts_code_names).split(',')
    for _c in _codes:
        if len(_c)>0:
            ts_codes.append(str(_c).strip().upper())
else:
    # 只有1个股票代码
    ts_codes.append(str(ts_code_names).strip().upper())

# 获取开始时间
start_date = os.getenv("START_DATE")


# 获取访问实例
ts.set_token(token)
pro = ts.pro_api()


# 获取数据，写入csv
def download2csv(code_name, start_date=start_date):
    # 查询日线数据
    data_df = pro.daily(ts_code=code_name, start_date=start_date)
    print(data_df)

    # 下载后的文件名格式 股票代码_daily.csv
    _csv_filename = os.path.join(g.datapath, code_name+'_daily.csv')
    print(_csv_filename)

    # 执行写
    data_df.to_csv(_csv_filename)


# 主程序
if __name__ == "__main__":
    for code_name in ts_codes:
        download2csv(code_name)
        time.sleep(0.5)

    print('end')
