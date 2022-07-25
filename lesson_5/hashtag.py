from string import punctuation


text = input()
#text = 'Python Community'
#text = 'i like python community!'
#text = 'Should, I. subscribe? Yes!'

symbs = punctuation

for char in text:
    if char in symbs:
        text = text.replace(char, '')

text_list = [i.capitalize() for i in text.split()]

hashtag = '#' + ''.join(text_list)

if len(hashtag) > 140:
    hashtag = hashtag[:140]
    print(hashtag)
else:
    print(hashtag)