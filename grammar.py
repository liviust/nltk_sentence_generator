from stat_parser import Parser
from nltk.parse.generate import generate, _generate_all
from nltk import Nonterminal, induce_pcfg
from random import choice
from nltk.tokenize import PunktSentenceTokenizer
from contractions import contractions


sent_tokenizer = PunktSentenceTokenizer()

with open("<source of text>", "r") as f:
    text = f.read()

for k, v in contractions.items():
    text = text.replace(k, v)

sents = []
for paragraph in text.split('\n'):
    sents += sent_tokenizer.tokenize(paragraph)

parser = Parser()

productions = []
for sent in sents[:25]:
    try:
        tree = parser.parse(sent)
        productions += tree.productions()
    except:
        pass

S = Nonterminal('S')
grammar = induce_pcfg(S, productions)

for sentence in generate(grammar, depth=5):
    print " ".join(sentence) + "\n"
