#!/usr/bin/python
import re, random
import cgi, cgitb



f = open('/home/unixtool/data/vocab.dat')
linesInFile = list(f)

noun = {}
verb = {}
adj = {}
nounWord= []
verbWord= []
adjWord= []

for	i in range(0, len(linesInFile)):
	#print linesInFile[i] 
	singleLine = linesInFile[i].split('|')
	
	if singleLine[1] == 'n.':
		noun[singleLine[0]] = singleLine[2]
		nounWord.append(singleLine[0])
	elif singleLine[1] == 'v.':
		verb[singleLine[0]] = singleLine[2]
		verbWord.append(singleLine[0])
	elif singleLine[1] == 'adj.':
		adj[singleLine[0]] = singleLine[2]
		adjWord.append(singleLine[0])

random.shuffle(nounWord)
random.shuffle(verbWord)
random.shuffle(adjWord)

#getting the 1st n random words in each part of speech
nounShuffle = nounWord[0:16]
verbShuffle = verbWord[0:12]
adjShuffle = adjWord[0:12]
#for n in range(0, len(nounShuffle)):
#	print nounShuffle[n] + "  " + noun[nounShuffle[n]]

nounQSet =[]
verbQSet =[]
adjQSet =[]

for i in range(0,4):
	seti = []
	for j in range(0,4):
		seti.append(nounShuffle[j+i*4])
	nounQSet.append(seti)


for i in range(0, 3):
	seti = []
	for j in range(0,4):
		seti.append(verbShuffle[j+i*4])
	verbQSet.append(seti)
	

for i in range(0, 3):
	seti = []
	for j in range(0,4):
		seti.append(adjShuffle[j+i*4])
	adjQSet.append(seti)
	
print nounQSet
print verbQSet
print adjQSet




