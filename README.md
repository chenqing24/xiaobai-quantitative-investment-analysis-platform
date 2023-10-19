# xiaobai-quantitative-investment-analysis-platform

看书后自己实现的小白量化投资分析平台的实现。
优化部分过期代码，补充了注释。
Mac，Python 3.11，Vscode下运行测试通过。

## 参考

* 《零基础搭建量化投资系统》（作者：何战军、杨茂龙、何天琦）的第九章

## 功能

* 数据获取：通过API、爬虫和文件导入
* 数据分析：
  * 股价和成交量分析趋势
  * 构造自定义指标
  * 根据股票基本信息、行业数据、政策面来筛选股票和预测
  * 多因子模型
  * 深度学习模型
* 策略定制
* 历史回测
* 策略执行：API和外挂2种方式

## 文件说明

1. HP_global.py:    全局变量定义
2. HP_set.py:       全局变量初始化
3. HP_data.py:      本地数据管理和数据处理
4. HP_formula.py:   基础函数库
5. HP_view.py:      窗口容器定义
6. HP_draw.py:      指标绘制库
7. HP_sys.py:       回测模块
8. HP_robot.py:     聊天机器人
9. HP_edit.py:      策略编辑器
10. HP_MainPage.py: 总框架
11. HP_main.py:     主程序入口
