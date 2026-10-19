import os
import datetime
import re
import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",100)
    engine.say(text)
    engine.runAndWait()
if not os.path.exists("python all works"):#here we are creating a folder using os module and if already exist then use it
    os.mkdir("python all works")
file="python all works/ATM.txt"#here we have created a file in that folder if not exist then it is formed automatically
# f=open(file,'r')
# text=f.read()
print("File is formed here:", os.path.abspath("python all works/ATM.txt"))
# history=text.splitlines()#isse jo bhi pehle ka data hai vo list mein convert hojayega with /n operator wala matlab second line wale next ellemnt of list
#ab dekho yeh upper waali history wala sahi kaam kar raha tha per ek issue tha yeh ek baar bas chalne ke karan purana data hi rakhe rehta hai manlo tumne add kardiye toh reflect hi nahi hoga vo toh pura code restart hone per hi hoga bas isliye hamne isse while mein rakhdenge taaki har baar yeh apne aap ko update kar sake ok 
class BANK:
    def __init__(self,name):
        self.user_name=name
        self.l=5000
        speak("Please insert your passbook if you have")
        self.list=[]
        # self.list.append(li) ##look this will create an error because append statement will add li(which is a list) as list only so now it will become nested list which is a problem becuse when for loop will run that will create an issue when adding a new string to a nested list
        self.list.extend(history)#yeh list ke ander nahi add karta yeh banni banayi list mein ange add karta hai
        found=False
        for i in history:#yeh li list ke saare strings ko i variable se baar baar chalayega
            if self.user_name in i:#ab ham same i ke liye dekhenge ki kya yeh wala hi name required hai by user or not
                number=re.findall(r"\d+",i)#isse jo i select hua hoga vo ek string hoga toh ussmein jo part numbers liye hoga usski ek list banadega
                for intnumber in number:#isse vo number list se bahar aajayega or variable mein store ho jayega NOTE ab dekho yeh har string ke liye hoga per last wale ki hi value set hogi numbers mein bas usske pehle waali toh loop ke ssath change hoti rehti hain unse hame kya karna last wala jo note pad mein har insaan ki jo line hai vo total amount wali hi hai na toh bas wahi wala number aayega har baar
                        num=int(intnumber)
                        self.l=num
                        found=True
        if found:
            print(f"Account found:current balance {self.l}")
            speak(f"account found current balance is {self.l}")
        else:
            print(f"account not present. creating a new account with name as {self.user_name} with initial balance of 5000")
            speak(f"account not present. creating a new account with name as {self.user_name} with initial balance of 5000")
            print("you are requested to pay 5000 to branch manager")
            speak("you are requested to pay 5000 to branch manager")
            speak("payment received and account has been formed. you can go ahead with transactions now")
    def Time(self):
        now=datetime.datetime.now()#note yaha module datetime hai and usske ander func datetime.now() hota hai
        formatted_time = now.strftime("%d/%m/%Y %I:%M:%S %p")
        return formatted_time
    def save_info(self,input,totalamount): #note here 2 input i am taking one is for updating the transaction and second is for updating total amount left in user account 
        with open("python all works/ATM.txt",'a') as f:#NOTE yaha 'w' tha isliye mujhe har baar data bapis dalna padhraha tha vo sahi bhi tha write data lose karta hai toh bapis dalna hi tha(tho isske niche wala code use hota hi) but ek problem thi ki agar same loop mein 2 transactions kardu toh bas last waali update hoti thi kyuki history wala variable toh bahar wale loop se update hota tha toh ander wale loop mein agar 2 se jada changes kardiye toh bas last change hi save hoga jab ander wala loop khattam hoga because write use kiya tha toh history mein gaya hi bas last wala toh baki transactions losed now.####isliye i append daldiya ab data lose hi nahi hoga or duplicate bhi nahi because ab data bapis laane ki jarurat hi nahi vo pehle se hi rahega issliye ab next 2 lines not usefull
            # for i in self.list:#yeh bas list ki information bapis notepad mein dalne keliye kiya hai becauise write karne se notepad ka purana data hatjata hai issliye sabse pehle hamne list banayi thi purane data ki
            #     f.write(i+"\n")
            f.write(input + "\n")
            f.write(totalamount +"\n")
    def add(self):
        a=int(input("enter amount to be added"))
        if a<=0:
            print("amount must be greater then 0")
        self.l=self.l+int(a)
        print(f"total amount is {self.l}")
        speak(f"you have submitted {a} rupees")
        speak("your specified amount has been added")
        x=self.Time()
        texttoadd=f"name :-{self.user_name},at {x} added amount:-{a}"
        total=f"name :-{self.user_name},at {x} total amount:-{self.l}"
                # self.list.append(texttoadd)
        # self.list.append(texttoadd)#acha yaha yeh bhi karsakte the per yaha extend yaha nahi lagta warna problem hojati because extend ek string ko add kardeta or fir jab for loop chalta toh vo string hi ek ek letter se tutjati
        self.save_info(texttoadd,total)
    def withdraw(self):
        a=input("enter amount to be withdrawn")
        self.l=self.l-int(a)
        if self.l>=0:
            print(f"left amount is {self.l}")
            speak("amount have been withdrawn")
            speak("Transaction successful")
            x=self.Time()
            texttoadd=f"name :-{self.user_name},at {x}, removed amount:-{a}"
            total=f"name :-{self.user_name},at {x}, total amount:-{self.l}"
            #self.list.extend(texttoadd) yaha append kaam karta per extend lagane se string ke ek ek letters add hojate or fir for loop wale mein ek ek letter print hota transactions mein.. @@ by the way meine toh yeh sab use nahi kiya direct function mein hi input dediya iosse mujhe list mein add karne ki naubat hi nahi aayi 
            self.save_info(texttoadd,total)
        else:
            print("insufficient balance")
            speak("insufficient balance")
    def check(self):
        print(f"balance available is {self.l}")
    def tran(self):
        # file=open("python all works/ATM.txt","r")   #i used these earlier but they used to show complete data but now they will show data of any specific persion only
        # z=file.read()
        # print(z)
        for i in history:
            if self.user_name in i:
                print(i)
# while True:
#     t=input("enter your name")
#     k=ATM(t)
#     A=input("enter what you want, deposit,withdraw,check,transactions")
#     if A.lower()=="deposit":
#         k.add()
#     elif A.lower()=="withdraw":
#         k.withdraw()
#     elif A.lower()=="check":
#         k.check()
#     elif A.lower()=="transactions":
#         k.tran()
#iss while loop mein loop holes hain .like if you deposited or withdraw when it will execute again it will create a new class with earlier value of 5000 means everything restarts.also here if we put class out then other users cant be formed then only one user will work so for all these issue we use loop inside loop
while True:
    print("welcome to BANK")
    speak("welcome to BANK")
    speak("enter your name or type 'quit' to exit")
    name=input("enter your name or type 'quit' to exit")
    if name.lower()=="quit":
        break
    #NOTE isskoyaha isliye rakha taaaki yeh baar baar update hosake
    f=open(file,'r')
    text=f.read()
    history=text.splitlines()#isse jo bhi pehle ka data hai vo list mein convert hojayega with /n operator wala matlab second line wale next ellemnt of list 
    #per yaha per bhi ek problem hui because agar manle tu ek saath 2 deposit karde ek hi loop mein toh total toh saahi aayega but 1st transaction hat jayegi na because usske just baad second kardi or wite to uda dega data save hone se pehle hi toh ya toh yeh ander wale loop mein lejao but vo nahi ho payega because fir yeh class creation pehle chaljayega or history next loop mein create hoga toh pehle hi error maajayega or second ki jo vo tumhari list update horahi thi ussko ander wale loop mein daldo taaki har ek loop per update hojaye fir data save rahega 
    user=BANK(name)
    while True:
        speak("enter what you want, deposit,withdraw,check,transactions,logout")
        A=input("enter what you want, deposit,withdraw,check,transactions,logout")
        if A.lower()=="deposit":
            user.add()
            print("logout and login again to see changes if made")
        elif A.lower()=="withdraw":
            user.withdraw()
            print("logout and login again to see changes if made")
        elif A.lower()=="check":
            user.check()
        elif A.lower()=="transactions":
            user.tran()
        elif A.lower()=="logout":
            speak("Thank you for using our banking services")
            break
        else:
            print("invalid option try again")
            speak("please try again")
# now finally everything was working fine but there was an issue here if i add or withdraw then my transaction history will be saved but when i will come back then transaction histpory can be fetched but my money will agian start from 5000 only not from my last transactions
#so sol i thought is i will have to extract complete data of notepad and in that i have to get that first word(name ) and last number(that is total amount left)
#text="Raj total amount:-6000" NOTE :- number=re.findall(r"\d+",text) here module required will be "re" NOTE :- import re
