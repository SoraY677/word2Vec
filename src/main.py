import os
import re
import glob
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


dir_path = "./data"
file_path = dir_path + "/corpus.txt"
file_wakati_path = dir_path + "/corpus_wakati.txt"


def traceSourcesDate():
    '''
        記事の各ファイルからデータを抜き出す処理
    '''

    if os.path.exists(dir_path) is False:
        os.mkdir(dir_path)
    open(file_path, mode="w")

    file_list = glob.glob("sources/text/**/*.txt")
    with open(file_path, mode="a", encoding='utf-8') as add_file:
        for path in file_list:
            trace_list = []
            with open(path, encoding="utf-8") as f:
                txt_list = f.readlines()
                for i in range(3, len(txt_list)):
                    s = re.sub('\\n|\\u3000', '', txt_list[i])
                    trace_list.append(s)

            add_file.write("".join(trace_list))
            add_file.write("\n")


def createModel():
    sentences = []

    with open(file_wakati_path, encoding='utf-8') as f:
        while True:
            line = f.readline()

            if line == '':
                break
            line = re.sub('\\n', '', line)
            sentences.append(line.split(' '))

    model = Word2Vec(sentences, sg=1, size=100, window=5, min_count=1)
    model.wv.save_word2vec_format("./model.vec.pt", binary=True)


if __name__ == "__main__":
    # createModel()
    wv = KeyedVectors.load_word2vec_format('./model.vec.pt', binary=True)
    for i in wv.most_similar(positive="人間", negative="ミサイル"):
        print(i)
