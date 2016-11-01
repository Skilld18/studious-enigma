from studious import answer, question, utils


terminate = ['quit', 'exit']
quest = ['q', 'question']
ans = ['a', 'answer']
group = ['g', 'group']
user = ['u', 'user']

def help():
    print("Welcome to Studious Enigma")
    print("Q for questions")
    print("A for answers")
    print("U for users")
    print("G for groups")
    print("E for exit")


errors = 0
def interact(me):
    help()
    while True:
        user_input = input(": ").lower()
        if user_input in terminate:
            print("Bye!")
            exit(0)
        elif user_input in quest:
            for q in question.get_all():
                print(q)
            utils.update_answer(input("Select a question: "), me.key, input("Enter an answer: "))
        elif user_input in ans:
            for a in answer.get_all():
                print(a.__str__() + ("Correct" if a.correct() else "Incorrect"))
        elif user_input in user:
            print(list(me))
        elif user_input in group:
            print("group")
        elif "?" in user_input:
            help()
        else:
            global errors
            errors += 1
            if errors == 3:
                print("Press ? to get a list of commands")

