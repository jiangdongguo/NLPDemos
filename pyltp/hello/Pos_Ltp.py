from pyltp import *

sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。"
segment_model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\cws.model"
postagger_model_path = "F:\\2019AIAI\\ltp_data_v3.4.0\\pos.model"
user_dict = "F:\\2019AIAI\\PythonProject\\LTP_Test\\data\\fulluserdict.txt"

# 1. 分词，并指定用户词典
segmentor = Segmentor()
segmentor.load_with_lexicon(segment_model_path, user_dict)
segResult = " ".join(segmentor.segment(sent))  # 处理分词结果，即将每个词用空格隔开
print("1. 分词结果：" + segResult)

# 2. 词性标注
words = segResult.split(" ")
postagger = Postagger()  # 实例化词性标注类
postagger.load(postagger_model_path)  # 导入词性标注模型
postags = postagger.postag(words)
print("2. 词性标注结果：")
for word, postag in zip(words, postags):
    print(word+"/"+postag)

