from time import *
import threading
import time
import random
import string
import tic_tok
import math
print("""You have 10 minute for 10 Question
Note:Time running in background      """)
def quiz_timer():
    global my_timer
    my_timer=600
    for x in range(600):
        my_timer+=-1
        sleep(1)
t_p_score=0 
def Python_Question():
    global t_p_score
    p_score=0
    total_time=time.time()
    quiz_timer_thread=threading.Thread(target=quiz_timer)
    quiz_timer_thread.start()
    print("Time Start Now")

    while my_timer>0:
    
        Q1_list=["Q1.for x in range(0.5, 5.5, 0.5): print(x)?\n (1)[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]\n (2)[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]\n (3)The Program executed with errors"
          ,"Q1.var ="'"James"'" * 2  * 3 then print(var)? \n (1)JamesJamesJamesJamesJames\n (2)Error: invalid syntax\n (3)JamesJamesJamesJamesJamesJames"]

        Q1=random.choice(Q1_list)
        print(Q1)
        ans1_index=Q1_list.index(Q1)
        A1_list=["The Program executed with errors","JamesJamesJamesJamesJamesJames"]
        ans1=input("ANS:")
        if my_timer==0:
            break
        if ans1==A1_list[ans1_index] or ans1=="3":
            print("correct!")
            p_score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break


        Q2_list=["Q2.Which operator has higher precedence in the following list?\n (1)% Modulus\n (2)**, Exponent\n (3)& BitWise AND\n (4)> Comparison"
          ,"Q2.var= "'"James Bond"'" then print(var[2::-1])? \n (1)py\n(2)yn\n (3)pyn\n (4)yna"]

        Q2=random.choice(Q2_list)
        print(Q2)
        ans2_index=Q2_list.index(Q2)
        A2_list=["**, Exponent","yn"]
        ans2=input("ANS:")
        if my_timer==0:
            break
        if ans2==A2_list[ans2_index] or ans2=="2":
            print("correct!")
            p_score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q3_list=["Q3.l = [None] * 10 then print(len(l))\n (1)10\n (2)0\n (3)Syntax Error"
          ,"Q3.my_list = ["'"Hello"'", "'"Python"'" then print("'"-"'".join(my_list))? \n (1)Hello-Python\n (2) HelloPython-\n (3)-HelloPython"]

        Q3=random.choice(Q3_list)
        print(Q3)
        ans3_index=Q3_list.index(Q3)
        A3_list=["10","Hello-Python"]
        ans3=input("ANS:")
        if my_timer==0:
            break
        if ans3==A3_list[ans3_index] or ans3=="1":
            print("correct!")
            p_score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break


        Q4_list=["Q4.Which one is NOT a legal variable name?\n (1) my-var \n (2) my_var\n (3)my_var  \n (4) _myvar"
        ,"""Q4.How do you insert COMMENTS in Python code?\n (1) #This is a comment \n (2) //This is a comment\n (3) /This is a comment/\n (4)None of above""",
        "Q4.How do you create a variable with the numeric value 5?\n (1) Both the other answers are correct \n (2) x = 5  \n (3) x = int(5)"
        ,"Q4.What is the correct file extension for Python files?\n (1).py \n (2).pt\n (3).pyt\n (4).pyth"]

        Q4=random.choice(Q4_list)
        print(Q4)
        ans4_index=Q4_list.index(Q4)
        A4_list=["my-var","#This is a comment","Both the other answers are correct",".py"]
        ans4=input("ANS:")
        if my_timer==0:
            break
        elif ans4==A4_list[ans4_index] or ans4=="1":
            print("correct!")
            p_score+=1
        else:
            print("incorrect!")
        print()

        if my_timer==0:
            break

        Q5_list=["Q5.How do you create a variable with the floating number 2.8?\n (1)x = float(2.8)\n (2)Both the other answers are correct\n (3)x = 2.8"
         ,"Q5.What is the correct syntax to output the type of a variable or object in Python?\n (1)print(typeof x)   \n (2)print(type(x))\n (3)print(typeOf(x))  \n (4)print(typeof(x))"
         ,"Q5.What is the correct way to create a function in Python?\n(1)create myFunction(): \n (2)def myFunction():\n (3)function myfunction():"
         ,"Q5.Which method can be used to remove any whitespace from both the beginning and the end of a string?\n (1)len()\n (2)strip() \n (3)ptrim()\n (4)trim()"]

        Q5=random.choice(Q5_list)
        print(Q5)
        ans5_index=Q5_list.index(Q5)
        A5_list=["Both the other answers are correct","print(type(x))","def myFunction():","strip()"]
        ans5=input("ANS:")
        if my_timer==0:
            break
        elif ans5==A5_list[ans5_index] or ans5=="2":
            print("correct!")
            p_score+=1
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q6_list=["Q6.Which method can be used to return a string in upper case letters?\n (1)upperCase()\n (2)uppercase()\n (3)toUpperCase()\n (4)upper()"
         ,"Q6.Which method can be used to replace parts of a string?\n (1)switch()\n (2)replaceString()\n (3)repl()\n (4)replace()"
         ,"Q6.Which operator is used to multiply numbers?\n (1)#\n (2)X\n (3)%\n (4)*"
         ,"Q6.Which operator can be used to compare two values?\n (1)!=\n (2)==\n (3)><\n (4)="]

        Q6=random.choice(Q6_list)
        print(Q6)
        ans6_index=Q6_list.index(Q6)
        A6_list=["upper()","replace()","*","="]
        ans6=input("ANS:")
        if my_timer==0:
            break
        elif ans6==A6_list[ans6_index] or ans6=="4":
            print("correct!")
            p_score+=1
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q7_list=["Q7.Which collection is ordered, changeable, and allows duplicate members?\n (1)DICTIONARY\n (2)TUPLE\n (3)LIST \n (4)SET"
         ,"Q7.Which collection does not allow duplicate members?\n (1)TUPLE\n (2)LIST\n (3)SET\n (4)Non of the above"
         ,"Q7.How do you start writing an if statement in Python?\n (1)if x > y then: \n (2)if (x > y)\n (3)if x > y:"]

        Q7=random.choice(Q7_list)
        print(Q7)
        ans7_index=Q7_list.index(Q7)
        A7_list=["LIST","SET","if x > y:"]
        ans7=input("ANS:")
        if my_timer==0:
            break
        elif ans7==A7_list[ans7_index] or ans7=="3":
            print("correct!")
            p_score+=1
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break
        Q8_list=["Q8.How do you start writing a while loop in Python?\n (1)while x > y:\n (2)while x > y {\n (3)x > y while {\n (4)while (x > y)"
         ,"Q8.How do you start writing a for loop in Python?\n (1)for x in y:\n (2)for each x in y:\n (3)for x in y:"
         ,"Q8.Which statement is used to stop a loop?\n (1)break\n (2)stop\n (3)return\n (4)exit"]

        Q8=random.choice(Q8_list)
        print(Q8)
        ans8_index=Q8_list.index(Q8)
        A8_list=["while x > y:","for x in y:","break"]
        ans8=input("ANS:")
        if my_timer==0:
            break
        if ans8==A8_list[ans8_index] or ans8=="1":
            print("correct!")
            p_score+=1
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q9_list=["Q9.What is the output for −- 'you are doing well' [2:999]\n (1)' '\n (2)Index error\n (3)'you are doing well'\n (4)'u are doing well'"
         ,"""Q9.y = [4, 5,1j] then y.sort()?\n (1)[1j,4,5]\n (2)[5,4,1j]\n (3)[4,5,1j]\n (4)Type Error"""
         ,"""Q9.Suppose we are given with two sets(s1&s2) then what is the output of the code −
s1 + s2\n (1)Adds the elements of the both the sets.\n (2)Removes the repeating elements and adds both the sets.\n (3)Output will be stored in S1.\n (4)It is an illegal command."""]

        Q9=random.choice(Q9_list)
        print(Q9)
        ans9_index=Q9_list.index(Q9)
        A9_list=["'u are doing well'","Type Error","It is an illegal command."]
        ans9=input("ANS:")
        if my_timer==0:
            break
        if ans9==A9_list[ans9_index] or ans9=="4":
            print("correct!")
            p_score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q10_list=["Q10.x = 36 / 4 * (3 +  2) * 4 + 2 then print(x)?\n (1)182\n (2)37\n (3)117\n (4)The Program executed with errors"
          ,"Q10.p, q, r = 10, 20 ,30 then print(p, q, r)? \n (1)10 20 30\n (2)10 20\n (3)Error: invalid syntax"]

        Q10=random.choice(Q10_list)
        print(Q10)
        ans10_index=Q10_list.index(Q10)
        A10_list=["182","10 20 30"]
        ans10=input("ANS:")
        if my_timer==0:
            break
        if ans10==A10_list[ans10_index] or ans10=="1":
            print("correct!")
            p_score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        break
        sleep(1)
    print("Time Up")
    print("Score:{}".format(p_score))
    t_p_score=p_score
    if p_score==10:
        total_secound=time.time()-total_time
        minutes=total_secound//60
        second=total_secound%60
        
        if minutes==0 and second<=59:
            print("Congratulation you have done 10 Question in %.2f seconds"%second)
        else:
            print("Congratulation you have done 10 Question in %d minutes %.2f seconds"%(minutes,second)) 
    
        
t_m_score=0     
def math_Question():
    global t_m_score
    score=0
    total_time=time.time()
    quiz_timer_thread=threading.Thread(target=quiz_timer)
    quiz_timer_thread.start()
    print("Time Start Now")

    while my_timer>0:
        Q1a=random.randint(1,10)
        Q1b=random.randint(1,10)
        ans1=Q1a+Q1b
        print("Q1.A={} and B={} C=a+b then C?\n ".format(Q1a,Q1b),end="")
        print("1.{}".format(random.randint(1,100))+"\t2.{}".format(random.randint(1,100))
                +"\n 3.{}".format(ans1)+"\t4.{}".format(random.randint(1,100)))
        ANS1=input(" ANS:")
        
        if my_timer==0 :
            break
        elif ANS1==str(ans1) or ANS1=="3":
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")

        print()
        if my_timer==0:
            break
        Q1a=random.randint(1,10)
        Q1b=random.randint(1,10)
        option1=random.randint(1,100)     
        option2=random.randint(1,100)
        option3=random.randint(1,100)
        ans2=Q1a*Q1b
        print("Q2.A={} and B={} C=A*B then C=?\n".format(Q1a,Q1b),end="")
        print(" 1.{}\t2.{}\n 3.{}\t4.{}".format(option1,ans2,option3,option2))
        ANS2=input(" ANS:")
        
        if my_timer==0:
            break
        elif ANS2==str(ans2) or ANS2=="2": 
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")
        print()
            
        if my_timer==0:
            break

        Q3a=random.randint(1,100)
        Q3b=random.randint(1,10)
        Q3c=random.randint(1,10)
        Q3d=random.randint(1,100)

        option1=round(random.uniform(1,100),2)
        option2=round(random.uniform(1,100),2)
        option3=round(random.uniform(1,100),2)
        ans3=round(Q3a/(Q3b/Q3c)+Q3d,2)
        print("Q3.Divide {} by {}/{} and add {}. What is the answer?\n".format(Q3a,Q3b,Q3c,Q3d),end="")
        print(" (1){}\t(2){}\n (3){}\t(4){}".format(option1,option3,option2,ans3))
        ANS3=input(" ANS:")
        
        if my_timer==0:
            break
        elif ANS3==str(ans3) or ANS3=="4": 
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")
        print()
            
        if my_timer==0:
            break
        
        Q4a=random.randint(1,100)
        Q4b=random.randint(1,5)
        Q4c=random.randint(1,5)

        option1=round(random.uniform(1,312500),2)
        option2=round(random.uniform(1,312500),2)
        option3=round(random.uniform(1,312500),2)
        ans4=round(Q4a*(Q4b**Q4c))
        print("Q4.({}*{}**{})=?\n".format(Q4a,Q4b,Q4c))
        print(" (1){}\t(2){}\n (3){}\t(4){}".format(option1,option3,option2,ans4))
        ANS4=input(" ANS:")
        if my_timer==0:
            break
        elif ANS4==str(ans4) or ANS4=="4": 
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")
        print()
            
        if my_timer==0:
            break
        

        Q5a=random.randint(1,20000)
        Q5b=random.randint(1,20000)
        Q5c=random.randint(1,20000)

        ans5=Q5c+Q5a+Q5b
        option1=ans5+random.randint(1,1000)
        option2=ans5+random.randint(1,1000)
        option3=ans5+random.randint(1,1000)
        print("Q5.(?)-{}-{}={}\n".format(Q5a,Q5b,Q5c))
        print(" (1){}\t(2){}\n (3){}\t(4){}".format(ans5,option1,option2,option3))
        ANS4=input(" ANS:")
        if my_timer==0:
            break
        elif ANS4==str(ans4) or ANS4=="1": 
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")
        print()
            
        if my_timer==0:
            break
        Q6_list=["Q6What is the symbol of pi?\n(1)π\n(2)€\n(3)Ω\n(4)∞"
          ,"Q6.Arrange the numbers in ascending order: 36, 12, 29, 21, 7? \n(1)7, 12, 21, 29, 36\n(2)36, 29, 21, 12, 7\n(3)36, 29, 7, 21, 12\n(4)None of these"
         ,"Q6.20 is divisible by ……… .\n(1)1\n(2)3\n(3)7\n(4)None of these"]

        Q6=random.choice(Q6_list)
        print(Q6)
        ans6_index=Q6_list.index(Q6)
        A6_list=["π","7, 12, 21, 29, 36","1"]
        ans6=input("ANS:")
        if my_timer==0:
            break
        if ans6==A6_list[ans6_index] or ans6=="1":
            print("correct!")
            score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q7_list=["Q7.What is the smallest three digit number?\n(1)101\n(2)999\n(3)111\n(4)100"
         ,"Q7.What is three fifth of 100?\n(1)3\n(2)5\n(3)20\n(4)60"
         ,"Q7.What is the remainder of 21 divided by 7?\n(1)21\n(2)7\n(3)1\n(4)None of these"]

        Q7=random.choice(Q7_list)
        print(Q7)
        ans7_index=Q7_list.index(Q7)
        A7_list=["100","60","None of these"]
        ans7=input("ANS:")
        if my_timer==0:
            break
        if ans7==A7_list[ans7_index] or ans7=="4":
            print("correct!")
            score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break
        Q8_list=["Q8.What is 7% equal to?\n(1)0.007\n(2)0.7\n(3)0.07\n(4)7"
         ,"Q8.What is the value of x if x2 = 169?\n(1)1\n(2)169\n(3)13\n(4)338"
         ,"Q8.What is the reciprocal of 17/15?\n(1)1.13\n(2)17/15\n(3)15/17\n(4)30/34"]

        Q8=random.choice(Q8_list)
        print(Q8)
        ans8_index=Q8_list.index(Q8)
        A8_list=["0.07","13","15/17"]
        ans8=input("ANS:")
        if my_timer==0:
            break
        if ans8==A8_list[ans8_index] or ans8=="3":
            print("correct!")
            score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        Q9_list=["Q9.Which number is missing? 1, 9, 25, 49, (?)\n(1)121\n(2)81\n(3)16\n(4)169"
         ,"Q9.From the alternatives, select the set which is most alike the set (23, 29, 31).\n(1) (17, 21, 29)\n(2) (41, 43, 47)\n(3) (31, 37, 49)\n(4) (13, 15, 23)"
         ,"Q9.What is 121 times 11?\n(1)1313\n(2)1331\n(3)1133\n(4)3131"]

        Q9=random.choice(Q9_list)
        print(Q9)
        ans9_index=Q9_list.index(Q9)
        A9_list=["81","(41, 43, 47)","1331"]
        ans9=input("ANS:")
        if my_timer==0:
            break
        if ans9==A9_list[ans9_index] or ans9=="2":
            print("correct!")
            score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        
        Q10_list=["Q10.3456 ÷ 12 ÷ 8 = ?\n(1)33.5\n(2)36.5\n(3)50\n(4)36"
         ,"Q10. 106 × 106 – 94 × 94 = ?\n(1)2004\n(2)1904\n(3)1906\n(4)2400"
         ,"Q10.10-2 means …………. .\n(1)milli\n(2)micro\n(3)deci\n(4)centi"]

        Q10=random.choice(Q10_list)
        print(Q10)
        ans10_index=Q10_list.index(Q10)
        A10_list=["36","2400","1331"]
        ans10=input("ANS:")
        if my_timer==0:
            break
        if ans10==A10_list[ans10_index] or ans10=="4":
            print("correct!")
            score+=1
            
        else:
            print("incorrect!")
        print()
        if my_timer==0:
            break

        break
        sleep(1)
    
    print("Time Up")
    print("Score:{}".format(score))
    t_m_score=score
    if score==10:
        total_secound=time.time()-total_time
        minutes=total_secound//60
        second=total_secound%60

        if minutes==0 and second<=59:
            print("Congratulation you have done 10 Question in %.2f seconds"%second)
        else:
            print("Congratulation you have done 10 Question in %d minutes %.2f seconds"%(minutes,second)) 


    


while True:
    print("""----------------------------------
-           Quiz With Game       -
-                                -
-           1.Python Quiz        -   
-           2.Math Quiz          -
-           3.Tic-Tok game       -
-           4.Exit               -
-                                -  
----------------------------------""")
    try:
        ch=input("Enter your choice:")
    except Exception as e:
        print("Enter right input!")
    if ch=="1":
        Python_Question()
    elif ch=="2":
        math_Question()
    elif ch=="3":
        if t_p_score>=1 and t_m_score>=1:
            tic_tok.Tik_tac()
        else:
            print("""Your score is low!!\nIF u got 6/10 in python and 6/10 in math then u able to play game!""")

    elif ch=="4":
        break
    else:
        print("Enter right input between 1 to 4 only!")
        
