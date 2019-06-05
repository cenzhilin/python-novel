book ='e10'


def n(book):
    def getText():
        txt = open('England/' + book + '.txt', "r").read()
        txt = txt.lower()
        for ch in '!#$%&()*+,-.\:;<>=?@[\\]^_{}|~\'':
            txt = txt.replace(ch, " ")
        return txt

    # 得到txt
    txt = getText()

    # 进行英文分词
    words = txt.split()
    # 统计各个词的次数,生成字典
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    # 把字典变为列表,对列表进行排序,从高到低
    items = list(count.items())
    items.sort(key=lambda x: x[1], reverse=True)
    num = []
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
    minx = min(num) / len(items)
    maxx = max(num) / len(items)
    print(average)
    print(minx)
    print(maxx)

    content = "平均值除以总数:" + str(average) + "  最小值除以总数: " + str(minx) + "  最大值除以总数:" + str(maxx)

    print(content)
    # 保存进TXT
    f = open(book + "result.txt", 'w')
    f.write(content)
    f.close()

for i in range(10):
    book ="e"+str(i+1)
    n(book)