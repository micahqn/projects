import gensim.downloader as api

#word2vec-google-news-300
#glove-wiki-gigaword-100

model = api.load("word2vec-google-news-300")

add_words = ["king", "female"]
sub_words = ["male"]

result = model.most_similar(positive=add_words, negative=sub_words)
print("+", add_words)
print("-", sub_words)

for i in range(5):
    most_similar_key, similarity = result[i]
    print(str(i+1)+": "+most_similar_key, similarity)




