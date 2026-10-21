import tiktoken

encoding = tiktoken.get_encoding("o200k_harmony")  # the tokenizer gpt-oss uses

ids = encoding.encode("hi how are you?")
print(ids)
print([encoding.decode([i]) for i in ids])
print(len(ids), "tokens")

for text in ["refund", "unsubscribing", "My parcel has not arrived", "मेरा पार्सल नहीं आया"]:
    ids = encoding.encode(text)
    print(len(ids), [encoding.decode([i]) for i in ids])

ids = encoding.encode("The parcel arrived but the box was crushed")
print(ids)
print(encoding.decode(ids))
print(encoding.n_vocab, "tokens in the vocabulary")