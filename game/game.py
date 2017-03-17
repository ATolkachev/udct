#assign questions to variables
level1 = 'If you multiply 2 by 2 correct answer is going to be: __1__'
level2 = 'If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__'
level3 = "If you multiply 2 by 2 correct answer is going to be: __1__. If you then multiply it by 3 it became __2__. And if you add 9 it'll became __3__"

#assign answers
answers = [4, 12, 21]

#Array to search through question
questions =['__1__', '__2__', '__3__']

# Select a level
def level_of_dif():
    try:
        level = int(input("How dificult this quiz supposed to be? \n 1. Super ease \n 2. Harder \n 3. Very hard \n"))
        if 1 <= level <= 3:
            return level
        else:
            print 'Sorry, but you can only choose between 1 to 3 here'
            level_of_dif()
    except NameError:
        print 'Sorry, but you can only use integers here'
        level_of_dif()

#method to print a question based on level of dificilty
def ask_a_question(dificulty):
    if dificulty == 1:
        global level1
        print level1
        level1 = level1.split()
        return level1
    elif dificulty == 2:
        global level2
        print level2
        level2 = level2.split()
        return level2
    else:
        global level3
        print level3
        level3 = level3.split()
        return level3

def find_in_question(question):
    for element in questions:
        if element in question:
            print element, 'is in ', question
            index = question.index(element)
            try:
                answer = input('Type an answer for ' + element + '\n')
                if answer in answers:
                    question[index] = answer
                    print question
                    find_in_question(question)
                else:
                    print "your answer wrong, try again"
                    find_in_question(question)
            except NameError:
                print 'Your answer supposed to be an integer'
                find_in_question(question)


find_in_question(ask_a_question(level_of_dif()))
