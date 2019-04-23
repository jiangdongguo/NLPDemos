from pyltp import *


sentence = "中国南部的湖南省，省会是长沙市，是一座世界知名的城市。"

segment_model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\cws.model"    # 分词模型
postagger_model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\pos.model"  # 词性标注模型
namedEntity_model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\ner.model"  # 命名实体模型

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
for word, postag in zip(words, postags):
    print(word+"/"+postag)

# 3. 命名实体识别
recognizer = NamedEntityRecognizer()
recognizer.load(namedEntity_model_path)
netags = recognizer.recognize(words,postags)
for word, postag, netag in zip(words, postags,netags):
    print(word+"/"+postag+"/"+netag)
