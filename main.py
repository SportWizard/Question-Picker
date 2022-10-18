import random as rd

running = True
read = False
size = 0

numChapter = 5
numQuestionPerChapter = 115

questionDone = []

def readFile():
  file = open("Question.txt", "r")
  line = file.readline()

  while line != "":
    #restore the previously done question
    chapters = (line[len("Chapter ")])
    questions = (line[len("Chapter n, Question: "):-1])

    questionDone.append(chapters + questions)
  
    #read next line
    line = file.readline()
  
  file.close()

def writeFile():
  file = open("Question.txt", "w")

  for i in range(len(questionDone)):
    #write the file
    file.write("Chapter %s, Question: %s\n" % ((questionDone[i])[0], (questionDone[i])[1]))

  file.close()

def checkFileSize():
  global size
  file = open("Question.txt", "r")

  size = len(file.readlines())

  file.close()

while running:
  if read == False:
    readFile()
    read = True

  checkFileSize()
  #determine if the all the questions are done
  if size ==  numChapter * numQuestionPerChapter:
    print("All question are finished")
    running = False

  #choose a randome chapter and question
  chapter = str(rd.randint(1, numChapter)) #first chapter to the last chapter
  question = str(rd.randint(1, numQuestionPerChapter)) #first question to the last question

  combine = chapter + question

  #check if the chapter and qustion has already been done
  if combine not in questionDone:
    print("Chapter %s, Question: %s" % (chapter, question))
  else:
    continue
  
  #add chapter and question to the list of chapter and question that has been done
  questionDone.append(combine)

  writeFile()
  
  #ask the user if they want to keep doing it
  keepDoing = input("Continue to work[Y/N]?: ").strip().upper()
  
  #check if the user inputted the correct input
  while keepDoing != "Y" and keepDoing != "N":
    keepDoing = input("Continue to work[Y/N]?: ").strip().upper()

  #end the program
  if keepDoing == "N":
    running = False