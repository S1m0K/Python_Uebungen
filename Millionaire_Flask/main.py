from dataclasses import dataclass

from flask import Flask, render_template, session, request, jsonify
from flask_session import Session
import random
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@dataclass
class Question:
    level: int
    text: str
    correct: str
    answers: [str,str,str,str]

    def __init__(self, level, text, answers):
        self.text = text
        self.level = int(level)
        self.correct = answers[0]
        self.answers = answers
        random.shuffle(answers)

    def __str__(self):
        return "%s\n%s\n%s\n%s\n%s\n%s\n" % (self.text, self.level, self.correct, self.answers[0],
                                             self.answers[1], self.answers[2], self.answers[3])


questions = []
questionsLevel_0 = []
questionsLevel_1 = []
questionsLevel_2 = []
questionsLevel_3 = []
questionsLevel_4 = []


def questions_to_dic():
    i = 0
    thisdict = dict()
    for q in questions:
        thisdict[i] = q
        i = i+1



    return thisdict


class SimpleData(Resource):
    def get(self, id):
        return jsonify(questions[id])

    def delete(self, id):
        questions.remove(id)
        if not questions.__contains__(id):
            return {"Message": "%s gelöscht" % id}
        return {"Message": "%s konnte nicht gelöscht werden" % id}

    def put(self, question):
        questions.__add__(question)
        if questions.__contains__(question):
            return {"Message": "Neu hinzugefügt"}
        return {"Message": "Question konnte nicht upgeloaded werden"}
    def patch(self, id):

        data =  data = request.get_json(force=True)
        if 'correct' in data:
            info.correct = data['correct']
        if 'level' in data:
            info.level = data['level']
        if 'text' in data:
            info.text = data['text']
        if 'answers' in data:
            info.answers = data['answers']
        return jsonify({'message': 'object with id %d modified' % id})

class SimpleAllData(Resource):
    def get(self):
        dic = questions_to_dic()
        return jsonify(dic)


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


api.add_resource(SimpleData, '/millionaire/questions/<int:id>')
api.add_resource(SimpleAllData, '/millionaire/questions')

@app.route('/millionaire/questions/random')
def randoQuestion():
    q = questions[random.randint(0, len(questions)-1)]
    return jsonify(q)



@app.route('/millionaire')
@app.route('/millionaire/<int:user_in>')
def home(user_in=0):
    feedback = ''

    if 'question' in session:
        q = session['question']
        print(q.correct)
        print(q.answers[user_in - 1])
        if q.answers[user_in - 1] == q.correct:
            feedback = 'correct!'
            if q.level == 4:
                return render_template('WinnerScreen.html', questions=questions)
            session['question'] = getQuestion(q.level + 1)

        else:
            feedback = 'wrong'
            readAndStoreQuestion()
            session['question'] = getQuestion(0)
    else:
        session['question'] = getQuestion(0)
    return render_template('MillionaireMainPage.html', feedback=feedback, question=session['question'])


@app.route('/millionaire/win')
def win():
    return render_template('WinnerScreen.html', questions=questions)


if __name__ == '__main__':
    readAndStoreQuestion()
    app.run()  # Startet den Server
