from pyltp import *
import os

sentence = "中国南部的湖南省，省会是长沙市，也是一座世界性的城市。"

MODELDIR = "F:/2019AIAI/ltp_data_v3.4.0/"

# 1. 中文分词
segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
words = segmentor.segment(sentence)
wordList = list(words)  # 从生成器转换为列表
print(wordList)

# 2. 词性标注
postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))
postags = postagger.postag(words)

# 3. 句法分析
#   将词性标注和分词结果都加入到分析器进行句法解析
parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))
arcs = parser.parse(words, postags)

# 4. 命名实体识别
recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))
netags = recognizer.recognize(words, postags)

# 5. 语义角色标注
labeller = SementicRoleLabeller()
labeller.load(os.path.join(MODELDIR, "pisrl_win_v3.4.model"))
roles = labeller.label(words, postags, arcs)
# 输出标注结果
print("\n语义角色标注结果：")
for role in roles:
    # 谓词
    print('rel：', wordList[role.index])
    for arg in role.arguments:
        if arg.range.start != arg.range.end:
            print(arg.name, ' '.join(wordList[arg.range.start:arg.range.end]))
        else:
            print(arg.name, wordList[arg.range.start])


segmentor.release()
postagger.release()
parser.release()
recognizer.release()
labeller.release()




