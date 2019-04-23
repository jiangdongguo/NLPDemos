# 使用LTP分词
# _*_ coding：utf-8 _*_
import sys
import importlib
from pyltp import Segmentor # 导入pyltp库

importlib.reload(sys)
# 指定外部用户词典
user_dict = "F:\\2019AIAI\\PythonProject\\LTP_Test\\data\\fulluserdict.txt"
# 指定分词模型库路径
model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\cws.model"
# 实例化分词模块
segmentor = Segmentor()
# 加载分词库,登录专有名词
# segmentor.load_with_lexicon(model_path,user_dict)
# 加载分词库
segmentor.load(model_path)
# 执行分词操作
words = segmentor.segment("在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。")
# 打印分割后的结果
print(" | ".join(words))


