import random


class Question:
    def __init__(self, level, text, answers):
        self.text = text
        self.level = int(level)
        self.answers = answers

    def __str__(self):
        return "%s\n%s\n%s\n%s\n%s\n%s\n" % (self.text, self.level, self.answers[0],
                                             self.answers[1], self.answers[2], self.answers[3])


questions = []
questionsLevel_0 = []
questionsLevel_1 = []
questionsLevel_2 = []
questionsLevel_3 = []
questionsLevel_4 = []


def separateQuestionByLevel():
    for q in questions:
        if q.level == 0:
            questionsLevel_0.append(q)
        elif q.level == 1:
            questionsLevel_1.append(q)
        elif q.level == 2:
            questionsLevel_2.append(q)
        elif q.level == 3:
            questionsLevel_3.append(q)
        else:
            questionsLevel_4.append(q)


def readAndStoreQuestion():
    f = open(
        r"C:\Users\simon\OneDrive - HTL Anichstrasse\Dokumente\HTL-Anichstrasse\Mitschrift\4AHWII\CCDE\005_09-01-23\millionaire.txt",
        "r")
    lines = f.readlines()
    for i in range(1, len(lines)):
        fields = lines[i].split("\t")
        readAnswers = [fields[2], fields[3], fields[4], fields[5]]
        q = Question(fields[0], fields[1], readAnswers)
        questions.append(q)
    f.close()
    separateQuestionByLevel()


def getQuestion(level):
    if level == 0:
        print(len(questionsLevel_0))
        rand = random.randint(0, len(questionsLevel_0))
        randQuest = questionsLevel_0.__getitem__(rand)
        questionsLevel_0.remove(randQuest)
        return randQuest


    elif level == 1:
        rand = random.randint(0, len(questionsLevel_1))
        randQuest = questionsLevel_1.__getitem__(rand)
        questionsLevel_1.remove(randQuest)
        return randQuest

    elif level == 2:
        rand = random.randint(0, len(questionsLevel_2))
        randQuest = questionsLevel_2.__getitem__(rand)
        questionsLevel_2.remove(randQuest)
        return randQuest
    elif level == 3:
        rand = random.randint(0, len(questionsLevel_3))
        randQuest = questionsLevel_3.__getitem__(rand)
        questionsLevel_3.remove(randQuest)
        return randQuest
    else:
        rand = random.randint(0, len(questionsLevel_4))
        randQuest = questionsLevel_4.__getitem__(rand)
        questionsLevel_4.remove(randQuest)
        return randQuest


if __name__ == '__main__':
    readAndStoreQuestion()
    run = True
    level = 0
    while run:
        quest = getQuestion(level)
        answers = quest.answers
        correctAnswer = answers[0]
        random.shuffle(answers)

        print("Your current level is %s" % (level))
        print(quest.text)
        for a in range(0, len(answers)):
            print(quest.answers[a] + " (" + str(a) + ")")
        print("Please enter your Answer (0-3)")
        validAnswer = False
        userIn = None
        while not validAnswer:
            userIn = input()
            try:
                userIn = int(userIn)
                validAnswer = True
            except:
                print("please enter a valid number")
        if answers[userIn] == correctAnswer:
            print("Well done!")
            level = level + 1
        else:
            print("Unlucky...The correct answer would have been:")
            print(correctAnswer)
            print("Go again? (Y/N)")
            i = input()

            if str(i).lower() == "n":
                run = False
            else:
                level = 0
                readAndStoreQuestion()
        print("--------------------------------------------------------------------------------------")

        if level > 4:
            print("Great job you did it!!")
            #return render_template('03_session_object.html', feedback=feedback, question=session['question'])


