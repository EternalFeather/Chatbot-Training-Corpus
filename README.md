Dialog Datasets for Training Chatbot
===

在进行Chatbot的研究过程中，除了要有一个漂亮的模型之外，还需要有大量可供训练的语料来强化我们的聊天机器人。越干净的语料就能训练出越接近人类自然语言回复的Chatbot。
- 目前网上公开的语料大多是一些带有噪音的、数量有限的语料。在这里总结了一些可行的语料以及一些利用爬取工具得到的语料，其中包括：

# 基本公开语料

+ [dgk_shooter_min.conv](https://github.com/rustch3n/dgk_lost_conv)
中文电影对白语料，噪音大，由于对话未区分说话人，因此对白问答关系难以对应。
**针对聊天机器人语料的处理：** [data_preprocessing](https://github.com/EternalFeather/Chatbot-Training-Corpus/blob/master/data_preprocessing.py)

+ [ChatBot多语种聊天语料](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/)
ChatterBot聊天引擎所提供的基本语聊，涵盖语种范围广，但是数量不多，但质量较高，适合模型测试。

+ [DataSets for Natural Language Processing](https://github.com/karthikncode/nlp-datasets#question-answering)
这个是人为收集总结的自然语言处理研究论文以及对应的数据资料集，主要覆盖方面包括了： **Question Answering, Dialogue Systems** 以及 **Goal-Oriented Dialogue System** 等。文本都由英文构成，可用于机器翻译和对话模型使用。

+ [小黄鸡对话机器人训练语料](https://github.com/rustch3n/dgk_lost_conv/tree/master/results)
这就是网络上流行的小黄鸡对话机器人的训练语料，包括了 **xiaohuangji50w_fenciA.conv.zip （已分词）** 和 **xiaohuangji50w_nofenci.conv.zip （未分词）** 两个部分，分词以 **“/”** 区隔开来，并没有语义上的划分。语料中含有较多表情颜文字，总体对话字数较少，杂讯较多。

+ [白鹭时代中文问答语料](https://github.com/Samurais/egret-wenda-corpus)
由白鹭时代官方论坛问答版块的问题及回复组成，回复选取了标注 **“最佳答案”** 的记录为目标。人工审核资料，给每一个问题一个可以接受的答案。数量不多，多为问答模式。

+ [Cornell_Movie-Dialogs_Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
康奈尔大学影视对话资料集，语料包含对话人名称信息，语料为英文，以多轮对话为主。

# 个人爬取语料（初步整理）

+ [中文新闻语料](https://github.com/EternalFeather/Chatbot-Training-Corpus/tree/master/news%20corpus)
利用爬虫从各大新闻网站上爬取的新闻头条和简讯。

+ [PTT八卦版推文](https://github.com/EternalFeather/Chatbot-Training-Corpus/tree/master/PTT_charactors)
利用爬虫从社交软体PTT上对于八卦分类板块的内容进行爬取，原始资料为 [PTT八卦板推文.txt](https://github.com/EternalFeather/Chatbot-Training-Corpus/blob/master/PTT%E5%85%AB%E5%8D%A6%E6%9D%BF%E6%8E%A8%E6%96%87.txt) 其中包括一些符号和空格杂讯，过滤杂讯（利用统计方式按比例替换成固定符号，降低资料复杂度）之后，通过 **单字** 或 [词组](https://github.com/EternalFeather/Chatbot-Training-Corpus/tree/master/PTT_words)（jieba段词） 等不同方式建立问答语料和字典。

# License:

公开语料的版权归原作者所有，未经允许不得一个人名义投入盈利性活动。

# Keywords:

Tags: `Corpus` `Chatbot`
