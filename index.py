class score:
    sc = 0
    #to store score info
    def s():
        print("YOUR TOTAL SCORE IS: ",score.sc,"\n")


class category(score):
    def cont():
        rep = input("do you want to continue?? (y/n)")
        if(rep == 'y'):
            mode().m()
        elif(rep == 'n'): 
            exit
        else:
            print("enter (y or n)")
            category.cont()
        
    def q1():
        print("type \"stop\" to stop the current game")
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
                print("correct answer: ",linesa[i])
        score.s()
        category.cont()
        

    def q2():
        print("type \"stop\" to stop the current game")
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
                print("correct answer: ",linesa[i])
        
        score.s()

    def q3():
        print("type \"stop\" to stop the current game")
        f = open("q3.txt",'r')
        fa = open("a3.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()

    def q4():
        print("type \"stop\" to stop the current game")
        f = open("q4.txt",'r')
        fa = open("a4.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()

    def q5():
        print("type \"stop\" to stop the current game")
        f = open("q5.txt",'r')
        fa = open("a5.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()

    def q6():
        print("type \"stop\" to stop the current game")
        f = open("q6.txt",'r')
        fa = open("a6.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()

    def q11():
        print("type \"stop\" to stop the current game")
        f = open("q11.txt",'r')
        fa = open("a11.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()

    
    def q22():
        print("type \"stop\" to stop the current game")
        f = open("q22.txt",'r')
        fa = open("a22.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()


    def q33():
        print("type \"stop\" to stop the current game")
        f = open("q33.txt",'r')
        fa = open("a33.txt",'r')
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
                print("correct answer: ",linesa[i])
        
        score.s()


    def q44():
        print("type \"stop\" to stop the current game")
        f = open("q44.txt",'r')
        fa = open("a44.txt",'r')
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
                print("correct answer: ",linesa[i]) 
        
        score.s()

    def q55():
        print("type \"stop\" to stop the current game")
        f = open("q55.txt",'r')
        fa = open("a55.txt",'r')
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
                print("correct answer: ",linesa[i]) 
        
        score.s()

    def q66():
        print("type \"stop\" to stop the current game")
        f = open("q66.txt",'r')
        fa = open("a66.txt",'r')
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
                print("correct answer: ",linesa[i]) 
        
        score.s()
        

    #to choose a category 
    def choose1(): #objective
        cat = input("\nChoose a category:\n\n1.science\n2.sports\n3.music\n4.literature\n5.technology\n6.conundrums\ntype \"quit\" to quit the game :")
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
        cat = input("\nChoose a category: \n1.science\n2.sports\n3.music\n4.literature\n5.technology\n6.conundrums\ntype \"quit\" to quit the game :")
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
            print("Choose a valid category ")

class mode(category):
    def m(self):
        c = input("Choose a mode: \n1.Objective \n2.Subjective :")
        if(c == "1"):
            category.choose1()
        elif(c == "2"):
            category.choose2()
        else:
            print("wrong choice 1 for objective 2 for subjective")
            mode().m()

obj = mode()
print("\n ~~~~ WELCOME TO QUIZ GAME  ~~~~ \n")
obj.m()
