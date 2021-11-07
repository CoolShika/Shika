from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []

q = Question('Какой материк самый большой?', 'Евразия', 'Африка','Австралия','Америка')
q1 = Question('Сколько людей проживает в Одессе?', '1 миллион', '100 тысяч', '550 тысяч', '2 миллиона')
q2 = Question('В каком году появился майнкрафт?', '2009', '2007', '2012', '2015')
q3 = Question('Как зовут главного героя игры Метро?', 'Артём', 'Мельник', 'Сэм', 'Хан')
q4 = Question('Какая самая маленькая страна?', 'Ватикан', 'Сан-марино', 'Лихтейнштейн', 'Монако')

questions_list.append(q)
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
text = QLabel('Какой национальности не существует?') # текст вопроса
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton("Алеуты")
rbtn_4 = QRadioButton('Смурфы')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
#Создаем панель результата


AnsGroupBox = QGroupBox('Результат теста')
answer = QLabel('правильно/неправильно')
result = QLabel('тут будет правильный ответ')

layout_result = QVBoxLayout()
layout_result.addWidget(answer, alignment = Qt.AlignLeft | Qt.AlignTop)
layout_result.addWidget(result, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_result)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(text)
line2.addWidget(AnsGroupBox)
line2.addWidget(RadioGroupBox)
line3.addWidget(btn_OK)

layout_main = QVBoxLayout()
layout_main.addLayout(line1, stretch=2)
layout_main.addLayout(line2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(line3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

AnsGroupBox.hide()

window.setLayout(layout_main)
#------------------------------------------------------
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')



def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

'''def test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question()'''





answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
# после функции shuffle
#               0       1       2       3
# answers = [rbtn_2, rbtn_4, rbtn_1, rbtn_3]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    result.setText(q.right_answer)
    show_question()


def show_correct(res):
    answer.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score +=1
        print('Статистика\n-Всего вопросов:', window.total, '\nПравильных ответов:',  window.score)
        print('рейтинг:', window.score / window.total * 100)
    else:    
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('рейтинг:', window.score / window.total * 100)

def next_question():
    window.total +=1
    window.cur_question +=1
    if window.cur_question == len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() =='Следующий вопрос':
        next_question()
    else:
        check_answer()



btn_OK.clicked.connect(click_ok) 


window.cur_question = -1

window.total = 0
window.score = 0

next_question()

#print('Статистика')





window.show()
app.exec()
