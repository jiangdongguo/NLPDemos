# Parser.py 句法解析示例
# Date：2019-05-07 9:43
# Author：Jiangdongguo

from pyltp import *
import nltk
from scipy._lib.six import xrange

sentence = "中国南部的湖南省，省会是长沙市，也是一座世界知名的城市。"

segment_model_path = "data/ltp_models/cws.model"    # 中文分词模型
postagger_model_path = "data/ltp_models/pos.model"  # 词性标注模型
parser_model_path = "data/ltp_models/parser.model"  # 句法分析模型

# 1. 中文分词
segmentor = Segmentor()
segmentor.load(segment_model_path)
segResult = segmentor.segment(sentence)
tmp = " ".join(segResult)
print(tmp)

# 2. 词性标注
words = tmp.split(" ")
postagger = Postagger()
postagger.load(postagger_model_path)
postags = postagger.postag(words)

# 3. 句法分析
#   将词性标注和分词结果都加入到分析器进行句法解析
parser = Parser()
parser.load(parser_model_path)
arcs = parser.parse(words, postags)
arcLen = len(arcs)
conll = ""

# 构建Conll标准的数据结构
for i in xrange(arcLen):
    if arcs[i].head == 0:
        arcs[i].relation = "ROOT"
    conll += "\t"+words[i]+"("+postags[i]+")"+"\t"+postags[i]+"\t"+str(arcs[i].head)+"\t"+arcs[i].relation+"\n"
print(conll)

# 使用nltk构建依存句法关系树
conllTree = nltk.DependencyGraph(conll)  # 转换为依存句法图
tree = conllTree.tree()  # 构建树结构
tree.draw()  # 显示输出树



