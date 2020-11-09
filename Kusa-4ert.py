import random
f = open('text.txt', 'r')
data = f.readlines()
array = data
f.close()

class Test:

    def __init__(self, *info):
        self.array = array
        self.questions = []
        self.answers = []
        self.info = list(info)
        self.accept_percentage = int(array[1])
        self.correct_count = 0
        self.first_answer = []
        self.second_answer = []
        self.third_answer = []

    def add_question(self):
        for i in self.array:
            if '?' in i:
                self.questions.append(i)

    def add_answers(self):
        for i in self.array:
            if '.' in i:
                self.answers.append(i)

    def make_question(self):
        for i in self.answers:
            if '1.' in i:
                self.first_answer.append(i)
            elif '2.' in i:
                self.second_answer.append(i)
            elif '3.' in i:
                self.third_answer.append(i)
            else:
                print('Что-то пошло не так')

    def run_test(self):
        print(f'{self.questions[0]}')
        random.shuffle(self.first_answer)
        print(self.first_answer)
        answer = input('Введите ответ\n')
        if answer == 'arr = [].!':
            self.correct_count += 33
        print(f'{self.questions[1]}')
        random.shuffle(self.second_answer)
        print(self.second_answer)
        answer2 = input('Введите ответ\n')
        if answer2 == 'arr[index].':
            self.correct_count += 33
        print(f'{self.questions[2]}')
        random.shuffle(self.third_answer)
        print(self.third_answer)
        answer3 = input('Введите ответ\n')
        if answer3 == 'for key, value in my_dict.items():.':
            self.correct_count += 34

        print('Проходной балл %d, ваш балл %d' % (self.accept_percentage, self.correct_count))

    def __str__(self):
        return f'{self.info}'



t = Test(array)
t.add_question()
s = Test(array)
t.add_answers()
t.make_question()
print(t.questions)
print(t.make_question)
t.run_test()

