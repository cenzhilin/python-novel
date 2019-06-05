# coding=gbk
import jieba

#打开文档, 得到过滤掉标点符号,得到文本
book ='c1'

def c(book):
    txt = open('chinese/' + book + '.txt', "r").read()
    for ch in '。，\n  ? “ ” ．：？  ！ \' ':
        txt = txt.replace(ch, "")

    # 利用jieba进行分词 ,返回一个列表
    words = jieba.lcut(txt)

    # 分字
    def str_count2(str):
        list = []
        for s in str:
            # 中文字符范围
            if '\u4e00' <= s <= '\u9fff':
                list.append(s)

        return list

    words2 = str_count2(txt)

    def counts(words):
        # 统计各个词的次数,生成字典
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1

        # 把字典变为列表,对列表进行排序,从高到低
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)

        num = []  # 保存RF值

        # 对排名进行输出,和计算RF值
        for i in range(len(items)):
            word, count = items[i]
            r = i + 1
            rf = r * count
            num.append(rf)
            print("{0:<5}{1:<10}{2:>5}{3:>5}".format(r, word, count, rf))

        # 得到总和
        def getsum(list):
            sum = 0
            for i in list:
                sum = sum + i

            return sum

        # 平均数,最小值, 最大值除以总数
        average = getsum(num) / len(items) / len(items)
        minc = min(num) / len(items)
        maxc = max(num) / len(items)
        print(average)
        print(minc)
        print(maxc)

        content = "平均值除以总数:" + str(average) + "  最小值除以总数: " + str(minc) + "  最大值除以总数:" + str(maxc)

        print(content)
        return content

    content = "词语:  " + counts(words)
    content2 = "\n单字: " + counts(words2)
    # 保存进TXT
    f = open(book + "result.txt", 'w')
    f.write(content + content2)
    f.close()


for i in range(10):
    book ="c"+str(i+1)
    c(book)