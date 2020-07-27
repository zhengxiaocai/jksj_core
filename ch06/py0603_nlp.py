# 自然语言处理，统计词频
# r 读取，w 写，rw 读写都有，a 追加
# r+ 读取并更新，不会清空；w+ 写入并更新，会清空。
# >>TODO: 权限管理比较重要，如果只要读取，就不要申请写入。
import re


def parse(text):
    # 使用正则去除标点符浩和回车
    text = re.sub(r'[^\w]', ' ', text)

    # 转换为小写
    text = text.lower()

    # 生成单词list
    word_list = text.split()

    # 去除空
    word_list = filter(None, word_list)

    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_cnt


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        text_file = f.read()

    word_and_freq = parse(text_file)

    with open('out.txt', 'w') as f:
        for word, freq in word_and_freq:
            f.write('{}\t{}\n'.format(word, freq))
