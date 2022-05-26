# pip install chatterbot  
# pip install chatterbot_corpus
# pip install --upgrade chatterbot_corpus  
# pip install --upgrade chatterbot    
# importing the required modules  
'''
from chatterbot import ChatBot  
from chatterbot.trainers import ListTrainer  
from chatterbot.trainers import ChatterBotCorpusTrainer  
  
# creating a chatbot  
myBot = ChatBot(  
    name = 'Sakura',  
    read_only = True,  
    logic_adapters = [  
        'chatterbot.logic.MathematicalEvaluation',  
        'chatterbot.logic.BestMatch'  
        ]  
        )  
  
# training the chatbot  
small_convo = [  
    'Hi there!',  
    'Hi',  
    'How do you do?',  
    'How are you?',  
    'I\'m cool.',  
    'Always cool.',  
    'I\'m Okay',  
    'Glad to hear that.',  
    'I\'m fine',  
    'I feel awesome',  
    'Excellent, glad to hear that.',  
    'Not so good',  
    'Sorry to hear that.',  
    'What\'s your name?',  
    ' I\'m Sakura. Ask me a math question, please.'  
    ]  
  
math_convo_1 = [  
    'Pythagorean theorem',  
    'a squared plus b squared equals c squared.'  
    ]  
  
math_convo_2 = [  
    'Law of Cosines',  
    'c**2 = a**2 + b**2 - 2*a*b*cos(gamma)'  
    ]  
  
# using the ListTrainer class  
list_trainee = ListTrainer(myBot)  
for i in (small_convo, math_convo_1, math_convo_2):  
    list_trainee.train(i)  
  
# using the ChatterBotCorpusTrainer class  
corpus_trainee = ChatterBotCorpusTrainer(myBot)  
corpus_trainee.train('chatterbot.corpus.english')  


# starting a conversation
# >>> print(myBot.get_response("Hi, there!"))
# Hi
# >>> print(myBot.get_response("What's your name?"))
# I'm Sakura. Ask me a math question, please.
# >>> print(myBot.get_response("Do you know Pythagorean theorem"))
# a squared plus b squared equals c squared.
# >>> print(myBot.get_response("Tell me the formula of law of cosines"))
# c**2 = a**2 + b**2 - 2*a*b*cos(gamma)


'''
def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')


def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
    
greet('SBot', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()



'''


sl4-7@sl47-HP-ProDesk-400-G1-SFF:~/Downloads/hyperskill-SimpleChattyBot-python-main/Simple Chatty Bot$ python3 bot.py 
Hello! My name is SBot.
I was created in 2022.
Please, remind me your name.
Vivek
What a great name you have, Vivek!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
0
1
0
Your age is 21; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
5 
0 !
1 !
2 !
3 !
4 !
5 !
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.


'''