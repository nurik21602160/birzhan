f = open('text.txt', 'r')
data = f.readlines()
array = [data]
f.close()
class Test:
    def __init__(self, *info):
        self.info = list(info)
        self.question = []

    def __getitem__(self, i):
        return self.info[i]

    def __str__(self):
        return f'{self.info}'

    def question(self):
        for i in array:
            if '?' in i:
                self.question.append(i)
                print(self.question)



class Question:
    def __init__(self):
        self.correct = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)


lesson = Test(array)
test = Test.question()
print(test)