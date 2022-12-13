#Basic Assignment
#-------------------------------------------------------------------------------------------------------------------------------------------
def Ques1():
    print("WAP to take 10 numbers from a user and store them in a list")
    Listt=[]
    for i in range(10):
        user_inp=int(input("Enter number : "))
        Listt.append(user_inp)
    print(Listt)
    return  
 

def Ques2():
    print("Display numbers divisible by 5 from a list.")
    Sample_list=[]
    n=int(input("Enter how many numbers you wanna chcek : "))
    for i in range(n):
        numberinp=int(input("Enter  no "))
        Sample_list.append(numberinp)
    print(Sample_list)    
    for j in Sample_list:
         if j%5==0:
                print(j)
    return   



def Ques3():
    print("WAP to calculate the count of elements in a string taken as input from the user.")
    user_string=input("Enter a sentance: ")
    print("\n")
    len_string=user_string.split()
    string_space=user_string.replace(" ","")                       #used it to eliminate spaces so that only alphabets are counted

    print("Total no of words in this string are: ",len(len_string))

    print("\n")

    print("Total no of Characters in this sentance are with space: ",len(user_string))

    print("\n")

    print("Total no of Characters in this sentance are without space: ",len(string_space))
    
    return



def Ques4():
    input_integer=int(input("Write a Number to check if a number is even or odd where number is taken as input  : "))
    print("\n")
    if input_integer%2==0:
        print("Number",input_integer,"is an even number")
    else:
            if input_integer%2!=0:
                print("Number",input_integer,"is a odd number")
    print("\n")
    print("Thank You for using my code !!!")            
    return



def Ques5():  
    print("WAP to reverse a string taken as input from the user.")
    inp_str=input("Write something: ")
    print("\n")
    print(inp_str[::-1])
    return



def Ques6():
    print("WAP to reverse all the strings present in a list and save them in a new list.")
    inpu_user=input("Write something to reverse all the strings present in a list: ")

    j=list(inpu_user)

    print(inpu_user[::-1])

    m=list((inpu_user[::-1]).split(" "))

    print(m)
    return


def Ques7():    
    i_user=input("Find charaters that present in even index number. Try Me : ")
    for i in range (len(i_user)):
        if i%2==0: 
            print('')                           #if the input divisible by 2 then its even
    print(i)
    return        
      
    
def Ques8():
    Lst_num=[]
    for i in range(4):
        Numbr=input("Check if the first and last number of a list is the same, Type 1 number and Press Enter :")
        Lst_num.append(Numbr)
    print(Lst_num)    
    if Lst_num[0]==Lst_num[-1]:                                 #check whether 1st number is equal to last no
         print("yes")
    else:
         print("no")
    return        


def Ques9():   
    user_salary=int(input("Enter Your Salary to calculate your Income Tax : "))

    if user_salary<=250000:                                  #If income is 2.5 lakhs
        tax=0
    elif user_salary>250000 and user_salary<=500000:         #If income is in between 2.5 lakhs and 5 lakhs  
        tax=(user_salary-250000)*0.05
    elif user_salary>500000 and user_salary<=750000:         #If income is in between 5 lakhs and 7.5 lakhs  
        tax=(user_salary-500000)*0.1+12500
    elif user_salary>750000 and user_salary<=1000000:        #If income is in between 7.5 lakhs and 10 lakhs
        tax=(user_salary-750000)*0.15+37500
    elif user_salary>1000000 and user_salary<=1250000:       #If income is in between 10 lakhs and 12.5 lakhs
        tax=(user_salary-1000000)*0.2+75000
    elif user_salary>1250000 and user_salary<=1500000:       #If income is in between 12.5 lakhs and 15 lakhs
        tax=(user_salary-1250000)*0.25+125000
    elif user_salary>1500000:                                #If income is more than 15 lakhs
        tax=(user_salary-1500000)*0.30+187500

    print("Your calculated tax is : ", tax)

    return


def Ques10():
    Str_user=input("Enter Something to check whether a string starts with vowel or not: ")
    check_user=['a','e','i','o','u']
    if Str_user[0].lower() in check_user:                         #checking wether first word is in the check_user list or not
        print("yes",Str_user,"Starts with Vowel ",Str_user[0])
    else:
         print("No")
    return     



def Ques11():
    print("Write a Python program to check if all the characters of a string are vowel or not.")
    Str_user1=input("Enter Something: ")
    str_user1=Str_user1.lower()
    check_user=('aeiou')
    for i in str_user1:
        if i in check_user: 
            print("yes",Str_user1,"contains vowel",i)
            print('')        
        else:
            print("No")
    return   


def Ques12():
    print("WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.")    
    a=[]
    for i in range(5):
        l=int(input("Enter Your Marks : "))
        a.append(l)
    print("")    
    print("Your Marks are",a)
    print("")
    z=sum(a)
    print("Your Total Marks is :", z)
    print("")
    print("Percentage you achieved : ",(z/5),"%")
    return



def Ques13():
    print("Write a Python program to find the sum of the first n positive integers. Take n as input from the user.")
    s=0
    n=int(input("write a no upto which you want the sum : "))
    for i in range(n):
        s+=i
    print(s)
    return
          
          

def Ques14():       
    print("This Function will concatenate 2 list and make a new list")
    listOne=['hello','How','you','Today']
    listTwo=['Harshal sir','are','!!!']
    listThree=list(zip(listOne,listTwo))
    print(listThree)
    return
          
          

def Ques15():
    print("calculate the surface area of a triangle.")
    hyp=int(input("Enter the length of hypotenuse (h) cm : "))
    base=int(input("Enter the length of base (b) cm :"))
    if hyp<=base:
        print("The hypotenuse is always longer than the Base, Please give correct Input ")
        Ques15()
    else: 
        Surface_Area=(0.5)*hyp*base
        print("The Surface Area of this Triangle is : ", Surface_Area,"sqcm")
    return
          
          

def Ques16():
    print("WAP to convert two lists into a dictionary. Take the elements from first list as keys and elements from second list as values.") 
    list11=['Name','Age','Place','Learning Platform']
    list12=['Krishanu Dutta','23','Jharkhand','LearnBay']
    Dictionary_new=dict(zip(list11,list12))
    print(Dictionary_new)
    return
          
          

def Ques17():
    print("Input and store the marks of 10 students in a list. Print max and min marks.")
    Marks_list=[]
    for i in range(10):
        inpt=int(input("Enter Marks : "))
        Marks_list.append(inpt)
    print("Yours marks are : ", Marks_list)
    print("")
    print("Minimum Marks is : ", min(Marks_list))
    print("Maximum Marks is : ", max(Marks_list))
    return
          
          
          

def Ques18():
    print("WAP to convert '95.3' taken as input from the user into float value.")     
    user_put=input("Write a float no : ")
    float_user=float(user_put)
    print(float_user)
    print(type(float_user))
    return
          
          
def Ques19():
    print("WAP to count the number of zeroes present in a number taken as input from the user")      
    zero0=0
    non_zero=0
    inpt=input("Enter Marks : ")
    Marks_list=[str(x) for x in inpt]
    for i in range(len(Marks_list)):
        if Marks_list[i] == '0':
            zero0+=1
        else:
            non_zero+=0
    print("There are {} zeroes in {}".format(zero0,inpt))
    return
          
          

def Ques20():
    print("WAP to save the username and password of 10 users in a dictionary.")      
    Usrnm=[]
    passw=[]
    for i in range(3):
        Usrnm_l=input("Write your username : ") 
        Usrnm.append(Usrnm_l)
        passw_l=input("Write your Pass : ")
        passw.append(passw_l)

    Username_pass={k:v for k,v in zip(Usrnm,passw)}
    print(Username_pass)
    return



