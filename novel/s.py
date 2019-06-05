# coding=gbk
import re
import jieba
book ='亿万斯年'
book2= '红楼梦'

#正则表达式
regx='chapter'
regx2='第.回'

# 计算中文字数
def str_count2(str):
    list=[]
    for s in str:
        # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            list.append(s)

    return len(list)

#得到章节数
def getChapter(book,regx):
    txt = open(book + '.txt', "r", encoding='UTF-8-sig').read() #打开文档
    for ch in '。，\n  ? “ ” ．：？  ！ \'  ':
        txt = txt.replace(ch, "")

    #进行正则匹配
    listx = re.findall(regx, txt)

    words = jieba.lcut(txt)

    # 统计各个词的次数,生成字典
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    # 把字典变为列表,对列表进行排序,从高到低
    items = list(count.items())
    items.sort(key=lambda x: x[1], reverse=True)

    num = []  # 保存RF值

    p=""
    # 对排名进行输出,和计算RF值
    for i in range(len(items)):
        word, count = items[i]
        r = i + 1
        rf = r * count
        num.append(rf)
        p=p+" \n{0:<5}{1:<10}{2:<5}{3:>5}".format(r, word, count, rf)


    content=book + ' 共有' + str(len(listx)) + '章'
    #打印结果

    c = str_count2(txt)
    fc = "总字数为"+str(c)+ " "

    f = open(book + "result.txt", 'w'  ,encoding='UTF-8-sig')
    f.write(fc+content+p)
    f.close()



getChapter(book2,regx2)



