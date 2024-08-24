def all_variants(text):
    for i in text:
        yield i
    for i in range(len(text)):
        if i < (len(text) - 1):
            yield text[i:i+2]
        else:
            yield text

a = all_variants("abc")
for i in a:
    print(i)




















