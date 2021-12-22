import spacy
from spacy.tokens import token

nlp = spacy.load('en_core_web_sm')

doc = nlp(open('./got.txt', encoding="utf-8").read())
# secondDoc = nlp(open('./got2.txt', encoding="utf-8").read())

for token in doc:
    print(token.text, token.pos_)
    
# for token in secondDoc:
#     print(token.text, token.pos_)
