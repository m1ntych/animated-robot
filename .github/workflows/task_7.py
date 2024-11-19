from gensim.models import Word2Vec

sentences = [["māja", "dzīvoklis"], ["jūra", "māja"], ["dzīvoklis", "māja"]]
model = Word2Vec(sentences, min_count=1)

similarity = model.wv.similarity('māja', 'dzīvoklis')
print(f"Māja un dzīvoklis līdzība: {similarity}")
