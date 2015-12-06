#!/usr/bin/python
import re, random
import cgi, cgitb
import os

cgitb.enable()


def createQuizHeader():
	print 'Content-type:text/html\r\n\r\n'
	print '<html>'
	print ' <head>'
	print '  <title>Vocabulary Quiz</title>'
	print ' </head>'
	print ' <body>'
	print ' <h2>Vocubulary Quiz</h2>'
	
def createQuizTail():
	print '	</body>'
	print ' </html>'
# qList[1]=word; qlist[2] = option list; qlist[3] = ans
def createQuizPage():
	qList = getQuestions()
	print '   <form action=vocab.cgi method=POST><br>'
    #print '   <input type="hidden" id="check" name="check" value="1">'
	print '<ol>'
	questionNum =0
	for question in qList:		
		
		print'	<li><b>'+ str(question[0])+'</b><br>'		
	        print '<input type=hidden name=ans'+str(questionNum)+' value='+str(question[2])+'>'
	        print '<input type=hidden name=ques'+str(questionNum)+' value='+str(question[0])+'>'
		for i in range(0, 4):
			options = question[1]
			print '<input type=radio name=q' + str(questionNum) + ' value=' + str(i) + '>' + options[i] 

			print '<br>'
		questionNum = questionNum+1		
	print '</ol>'
	print '<input type=SUBMIT value=Submit Quiz>'
	print'</form>'

def gradeQuiz():

	print 'Content-type:text/html\r\n\r\n'
	correctAns=0
	correctWords = []
	wrongWords = []
	qList=getQuestions()
	ans = []
	ques = []
	ansVal = []
	quesWord = []
	q = []
	inputValue = []
	
	for i in range(0, len(qList)):
		
		ans.append("ans"+str(i))
		ques.append("ques"+str(i))	
		q.append("q"+str(i))
	
	for i in range(0, len(qList)):
		
		ansVal.append(form.getvalue(ans[i]))
		quesWord.append(form.getvalue(ques[i]))
		inputValue.append(form.getvalue(q[i]))

	for i in range(0, len(qList)):	
		if (ansVal[i] == inputValue[i]):
			correctAns = correctAns+1
			correctWords.append(quesWord[i])
			#print quesWord[i]
		else:
			wrongWords.append(quesWord[i])
			#print quesWord[i]
	
	

	print '<html>'
	print '<head>'
	print '<title>Graded Vocabulary Quiz</title>'
	print '</head>'
	print '<body>'
	print 'You got <b>' + str(correctAns) + ' of 10 </b> answers correct.'
	print '<p><table border=1>'
	print '<tr>'
	print '<th>Correct</th>'
	print '<th>Incorrect</th>'
	print '</tr>'
	print '<tr>'
	print '<td valign=top><font color=black>'
	for i in range(0, len(correctWords)):
		print str(correctWords[i]) + ' <br>'
	print '</font></td>'
	print '<td valign=top><font color=red>'
	for j in range(0, len(wrongWords)):
		print str(wrongWords[j]) + ' <br>'
	print '</font></td></tr></table>'
	print '</body>'
	print '</html>'

def getQuestions():

	f = open('/home/unixtool/data/vocab.dat')
	linesInFile = list(f)

	noun = {}
	verb = {}
	adj = {}
	nounWord= []
	verbWord= []
	adjWord= []
#getting the actual words and its meanings
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

	QSet =[]
	for i in range(0,4):
		seti = []
		
		Qword = nounShuffle[i*4]
		optionList = [noun[nounShuffle[1+i*4]], noun[nounShuffle[2+i*4]], noun[nounShuffle[3+i*4]]]
		ansPos = random.randint(0,3)
		
		optionList.insert(ansPos, noun[nounShuffle[i*4]])	
		qNoun= [Qword, optionList, ansPos]
		QSet.append(qNoun)

	for i in range(0,3):
		seti = []
		
		Qword = verbShuffle[i*4]
		optionList = [verb[verbShuffle[1+i*4]], verb[verbShuffle[2+i*4]], verb[verbShuffle[3+i*4]]]
		ansPos = random.randint(0,3)
		
		optionList.insert(ansPos, verb[verbShuffle[i*4]])	
		qVerb= [Qword, optionList, ansPos]
		QSet.append(qVerb)

	for i in range(0,3):
		seti = []
		
		Qword = adjShuffle[i*4]
		optionList = [adj[adjShuffle[1+i*4]], adj[adjShuffle[2+i*4]], adj[adjShuffle[3+i*4]]]
		ansPos = random.randint(0,3)
		
		optionList.insert(ansPos, adj[adjShuffle[i*4]])	
		qAdj= [Qword, optionList, ansPos]
		QSet.append(qAdj)
		
	random.shuffle(QSet)
	# for i in range(0, len(QSet)):
	# 	print QSet[i]

	return QSet

form = cgi.FieldStorage()
if os.environ['REQUEST_METHOD'] == 'GET':

	createQuizHeader()
	getQuestions()	
	createQuizPage()
	createQuizTail()
if os.environ['REQUEST_METHOD'] == 'POST':

	gradeQuiz()

