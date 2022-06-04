import spacy
import sys


nlp = spacy.load("en_core_web_sm")
doc = nlp(sys.argv[1])
propns = []
l = []


for token in doc:
    if token.pos_ == "NUM":
        if len(token.text) > 1:
            for string in token.text:
                if string.isdigit():
                    l.append(string)
        else:
            l.append(token.text)

    if token.pos_ ==  "PROPN":
        propns.append(token.text)


print("""
    <table>
    <caption>Tokens:</caption>
    """)

for propn in propns:
    print(f"<tr><td>{propn}</td><td>{propns.count(propn)}</td></tr>")

for digit in set(l):
    print(f"<tr><td>{digit}</td><td>{l.count(digit)}</td></tr>")

print("</table>")
