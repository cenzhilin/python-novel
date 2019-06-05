# coding=gbk
import jieba

#���ĵ�, �õ����˵�������,�õ��ı�
book ='c1'

def c(book):
    txt = open('chinese/' + book + '.txt', "r").read()
    for ch in '����\n  ? �� �� ������  �� \' ':
        txt = txt.replace(ch, "")

    # ����jieba���зִ� ,����һ���б�
    words = jieba.lcut(txt)

    # ����
    def str_count2(str):
        list = []
        for s in str:
            # �����ַ���Χ
            if '\u4e00' <= s <= '\u9fff':
                list.append(s)

        return list

    words2 = str_count2(txt)

    def counts(words):
        # ͳ�Ƹ����ʵĴ���,�����ֵ�
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1

        # ���ֵ��Ϊ�б�,���б��������,�Ӹߵ���
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse=True)

        num = []  # ����RFֵ

        # �������������,�ͼ���RFֵ
        for i in range(len(items)):
            word, count = items[i]
            r = i + 1
            rf = r * count
            num.append(rf)
            print("{0:<5}{1:<10}{2:>5}{3:>5}".format(r, word, count, rf))

        # �õ��ܺ�
        def getsum(list):
            sum = 0
            for i in list:
                sum = sum + i

            return sum

        # ƽ����,��Сֵ, ���ֵ��������
        average = getsum(num) / len(items) / len(items)
        minc = min(num) / len(items)
        maxc = max(num) / len(items)
        print(average)
        print(minc)
        print(maxc)

        content = "ƽ��ֵ��������:" + str(average) + "  ��Сֵ��������: " + str(minc) + "  ���ֵ��������:" + str(maxc)

        print(content)
        return content

    content = "����:  " + counts(words)
    content2 = "\n����: " + counts(words2)
    # �����TXT
    f = open(book + "result.txt", 'w')
    f.write(content + content2)
    f.close()


for i in range(10):
    book ="c"+str(i+1)
    c(book)