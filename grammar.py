from stat_parser import Parser
from nltk.parse.generate import generate, _generate_all
from nltk import Nonterminal, induce_pcfg
from random import choice



with open("<source of text>", "r") as f:
            sents = f.read().replace(',', '').replace('(', '').replace('(', '').split("\n")

parser = Parser()
productions = []

for sent in sents[:-2]:
	try:
		tree = parser.parse(sent)
		productions += tree.productions()
	except:
		pass


S = Nonterminal('S')
grammar = induce_pcfg(S, productions)


for sentence in generate(grammar, depth=5):
	print sentence
