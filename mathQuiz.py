#! python3
# mathQuiz.py - similar to randomQuizGenerator.py but with math

import random

for quizNum in range(20):
    quizFile = open('mathQuiz%s.txt' % (quizNum + 1), 'w')                       
    answerKeyFile = open('mathQuiz_answers%s.txt' % (quizNum + 1), 'w')
    
    quizFile.write('Name:\t\tDate:\t\tPeriod:\n\n')                                 
    quizFile.write((' ' * 20) + 'Assorted Mathimatics (Quiz %s)' % (quizNum + 1))    
    quizFile.write('\n\n')

    for questionNum in range(50):

        number1 = random.randint(0,12)
        number2 = random.randint(0,12)
        correctAnswer = number1 + number2
        wrongAnswers = list(range(0,25))
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 4)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('Question %s:\t%s + %s  = __\n' % (questionNum + 1, number1, number2))
        for i in range(5):
            quizFile.write('\t%s. %s\t\n' % ('ABCDE'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCDE'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
    

    

        
