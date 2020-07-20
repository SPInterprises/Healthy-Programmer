def main():
    import datetime
    def gettime():
        return datetime.datetime.now()
    def take(k):
        if k==1:
            c=int(input("Enter 1 for food and 2 for exercise\n"))
            if c==1:
                value= (input("Type Here\n"))
                with open("sameer3-food.txt","a")as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfully written\n")
            if c==2:
                value=(input("Type here\n"))
                with open("sameer3-exe.txt","a")as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfull written\n")
        if k==2:
            c=int(input("Enter 1 for food and 2 for excercise \n"))
            if c==1:
                value= (input("type here \n"))
                with open("parag2-food.txt","a") as op:

                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("succesfully wriiten \n")
            if c==2:
                value=(input("type here \n"))
                with open("parag2-exe.txt","a")as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfully written \n")
        if k==3:
            c=int(input("Enter 1 for food and 2 for exercise\n"))
            if c==1:
                value=(input("Type Here\n"))
                with open("pramod-food.txt","a") as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfull written\n")
            if c==2:
                value=(input("Type Here\n"))
                with open("pramod-exe.txt","a")as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfull written\n")

        print("Do you want to Loc and Retrieve ? y for yes and n for not \n")
        user_choice = ""
        while (user_choice != "y" and user_choice != "n"):
            user_choice = input()
            if user_choice == "y":
                main()
            if user_choice == "n":
                print("Thank you for usin HMS \n Have a great day")
                exit()






    def retrieve(k):
        if k==1:
            c=int(input("Enter 1 for food and 2 for exercise\n"))
            if c==1:
                with open("sameer3-food.txt")as op:
                    for i in op:
                        print(i,end="")
            if c==2:
                with open("sameer3-exe.txt")as op:
                    for i in op:
                        print(i,end="")
        if k==2:
            c=int(input("Enter 1 for food and 2 for exercise\n"))
            if c==1:
                with open("parag2-food.txt")as op:
                    for i in op:
                        print(i,end="")
            if c==2:
                with open("parag2-exe.txt")as op:
                    for i in op:
                        print(i,end="")
        if k==3:
            c=int(input("Enter 1 for food and 2 for exercise\n"))
            if c==1:
                with open("pramod-food.txt")as op:
                    for i in op:
                        print(i,end="")
            if c==2:
                with open("pramod-exe.txt")as op:
                    for i in op:
                        print(i,end="")
        else:
            print("please type valid input (sammer parag and pramod)",end="")
    print("This code is developed by Sameer/Parag Jain:")
    print("Health Management System Main Aapka Swaagat Hai:\n")
    a=int(input("Press 1 for Loc and 2 for Retrieve\n"))
    if a==1:
        b=int(input("Press 1 for sameer 2 for parag and 3 for pramod\n"))
        take(b)
    else:
        b=int(input("1 for sameer 2 for parag and 3 for pramod\n"))
        retrieve(b)
        print("Do you want to Loc and Retrieve ? y for yes and n for not \n")
        user_choice = ""
        while (user_choice != "y" and user_choice != "n"):
            user_choice = input()
            if user_choice == "y":
                main()
            if user_choice == "n":
                print("Thank you for using HMS \n Have a great day")
                exit()
main()







