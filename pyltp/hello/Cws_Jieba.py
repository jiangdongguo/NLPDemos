# 使用Jieba分词
# _*_ coding：utf-8 _*_
import jieba  # 导入结巴库

# jieba.load_userdict("data\\userdict.txt")

sent = '在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。'
# 结巴分词-全模式
wordList = jieba.cut(sent, cut_all=True)
print()
print(" | ".join(wordList))
# 结巴分词-精确模式
wordList = jieba.cut(sent)
print(" | ".join(wordList))
# 结巴分词-搜索引擎模式
wordList = jieba.cut_for_search(sent)
print()
print(" | ".join(wordList))

