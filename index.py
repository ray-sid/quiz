class score:
    sc = 0
    #to store score info
    def s():
        print("YOUR TOTAL SCORE IS: ",score.sc)


class category(score):
    def q1():
        f = open("q1.txt",'r')
        fa = open("a1.txt",'r')
        lines = f.readlines()
        linesa = fa.readlines()
        lines = [line.rstrip() for line in lines]
        linesa = [line.rstrip() for line in linesa]
        for i in range(len(lines)):
            print(lines[i])
            ans = input()
            if(ans.lower() == linesa[i]):
                print("correct!!")
                score.sc = score.sc + 1
            elif(ans.lower() == "stop"):
                score.s()
                mode().m()  
            else:
                print("incorrect") 
        
        score.s()

    def q2():
        f = open("q2.txt",'r')
        fa = open("a2.txt",'r')
        lines = f.readlines()
        linesa = fa.readlines()
        lines = [line.rstrip() for line in lines]
        linesa = [line.rstrip() for line in linesa]
        for i in range(len(lines)):
            print(lines[i])
            ans = input()
            if(ans.lower() == linesa[i]):
                print("correct!!")
                score.sc = score.sc + 1
            elif(ans.lower() == "stop"):
                score.s()
                mode().m()  
            else:
                print("incorrect") 
        
        score.s()

    #to choose a category 
    def choose1(): #objective
        cat = input("choose a category\n1.science\n2.sports\n3.music\n4.literature\n5.technology\n6.conundrums\ntype \"quit\" to quit the game")
        if(cat == "1"):
            category.q1()
        elif(cat == "2"):
            category.q2()
        elif(cat == "3"):
            category.q3()
        elif(cat == "4"):
            category.q2()
        elif(cat == "5"):
            category.q2()
        elif(cat == "6"):
            category.q2()
        elif(cat.lower() == "quit"):
            exit
        else:
            print("choose a valid category")

    def choose2(): #subjective
        cat = input("choose a category\n 1.science/n2.sports\n3.music\n4.literature\n5.technology\n6.conundrums")
        if(cat == "1"):
            category.q11()
        elif(cat == "2"):
            category.q22()
        elif(cat == "3"):
            category.q33()
        elif(cat == "4"):
            category.q44()
        elif(cat == "5"):
            category.q55()
        elif(cat == "6"):
            category.q66()
        elif(cat.lower() == "quit"):
            exit
        else:
            print("choose a valid category")

class mode(category):
    def m(self):
        c = input("choose a mode: 1.objective 2. subjective")
        if(c == "1"):
            category.choose1()
        elif(c == "2"):
            category.choose2()
        else:
            print("wrong choice 1 for objective 2 for subjective")
            mode().m()
    '''def cont():
        rep = input("do you want to continue?? (y/n")
        if(rep == 'y'):
            mode.m()
        elif(rep == 'n'): 
            exit
        else:
            print("enter (y or n)")
            mode.cont()'''


obj = mode()
print("WELCOME TO QUIZ GAME")
obj.m()