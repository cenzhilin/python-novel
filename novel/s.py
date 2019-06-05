# coding=gbk
import re
import jieba
book ='����˹��'
book2= '��¥��'

#������ʽ
regx='chapter'
regx2='��.��'

# ������������
def str_count2(str):
    list=[]
    for s in str:
        # �����ַ���Χ
        if '\u4e00' <= s <= '\u9fff':
            list.append(s)

    return len(list)

#�õ��½���
def getChapter(book,regx):
    txt = open(book + '.txt', "r", encoding='UTF-8-sig').read() #���ĵ�
    for ch in '����\n  ? �� �� ������  �� \'  ':
        txt = txt.replace(ch, "")

    #��������ƥ��
    listx = re.findall(regx, txt)

    words = jieba.lcut(txt)

    # ͳ�Ƹ����ʵĴ���,�����ֵ�
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    # ���ֵ��Ϊ�б�,���б��������,�Ӹߵ���
    items = list(count.items())
    items.sort(key=lambda x: x[1], reverse=True)

    num = []  # ����RFֵ

    p=""
    # �������������,�ͼ���RFֵ
    for i in range(len(items)):
        word, count = items[i]
        r = i + 1
        rf = r * count
        num.append(rf)
        p=p+" \n{0:<5}{1:<10}{2:<5}{3:>5}".format(r, word, count, rf)


    content=book + ' ����' + str(len(listx)) + '��'
    #��ӡ���

    c = str_count2(txt)
    fc = "������Ϊ"+str(c)+ " "

    f = open(book + "result.txt", 'w'  ,encoding='UTF-8-sig')
    f.write(fc+content+p)
    f.close()



getChapter(book2,regx2)



