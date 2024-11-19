users = []
data =  {}
python_scores ={}
dbms_scores ={}
dsa_scores ={}

def Registration():
     print("Registration")
     username = input("Enter a username: ").lower()
     if username in data :
         print("user already exists.Use different username.")
     else:
         password = input("Generate password ")
         users.append(username)
         data[username]=password
         print(f"You registered successfuly.")


def Login():
    print("For Login")
    username = input("Enter your username: ").lower()
    if username in users:
        print(f"Welcome {username}.")
        password = input("Enter password.")
        if password == data[username] :
            print("You are logged in.")
        else:
            print("you entered wrong password.")
    else:
        print("user doesn't exist. Register first ")


def  Attempt_quiz():
        username = input("Enter your username: ").lower()
        if username in users:
            print(f"Welcome {username}.")
            password = input("Enter password.")
            if password == data[username] :
                print("You can attempt quiz.")

                print("-----------QUIZ-----------")
                print("Choose which Quiz you want to attempt:")
                print("""     
                      1.PYTHON
                      2.DBMS 
                      3.DSA""" )
                while True:
                  choice = input("enter your choice:")

                  if choice =='1':

                    print("PYHTON QUIZ")

                    questions = ("1.What data type is the result of: 4 / 2 in Python?",
                     "2.Which keyword is used to define a function in Python?",
                     "3.What is the default return value of a function that does not return anything explicitly?",
                     "4.Which of the following functions is used to find the length of a list in Python?",
                     "5.What is the output of type([])?",
                     "6.Which function is used to get user input in Python 3?",
                     "7.Which method is used to add an element to a set in Python?"
                     )
                    options = (("A. int","B. float","C. str","D. bool"),
                            ("A. func","B. define","C. function","D. def"),
                            ("A. None","B. 0","C. false","D. null"),
                            ("A. count()","B. length()","C. len()","D. size()"),
                            ("A. list","B. dict","C. tuple","D. set"),
                            ("A. scanf()","B. raw_input()","C. get()","D. input()"),
                            ("A. insert()","B. append()","C. add()","D. extend()"))
            
                    answers = ("B","D","A","C","A","D","C")
                    guesses = []
                    py_score = 0
                    question_number = 0 
                    print()
                    for question in questions:
                        print(question)
                        for option in options[question_number]:
                            print(option)
                    
                        guess = input("Enter (A,B,C,D):").upper()
                        guesses.append(guess)
            
                        if guess == answers[question_number]:
                            print("CORRECT")
                            py_score += 1
                        else:
                            print("INCORRECT")    
                        question_number += 1
                        print()
                    
                    print()
                    py_score = int((py_score/len(questions))*100)
                    python_scores[username]= py_score
                    # print(f"Your score of PYTHON Quiz is {py_score}%")       

          
                  elif choice =='2':

                    print("DBMS QUIZ")

                    questions = (
                        "1. What does DBMS stand for?",
                        "2. Which of the following is a type of DBMS?",
                        "3. Which command is used to remove all records from a table in SQL?",
                        "4. Which of the following is not a type of database?",
                        "5. The primary key of a table must be?",
                        "6. SQL stands for?",
                        "7. In an ER diagram, what does a diamond shape represent?")
            
                    options = (
                        ("A. Database Management System", "B. Data Manipulation System", "C. DataBase Manipulation System","D. DataBase Management Solution"),
                        ("A. Hierarchical", "B. Network", "C. Relational", "D. All of the above"),
                        ("A. DELETE", "B. REMOVE", "C. DROP", "D. TRUNCATE"),
                        ("A. Hierarchical", "B. Distributed", "C. Flat file", "D. Programming"),
                        ("A. Unique", "B. Not Null", "C. Both A and B", "D. None of the above"),
                        ("A. Structured Query Language", "B. Simple Query Language", "C. Standard Query Language", "D. Sequential Query Language"),
                        ("A. Entity", "B. Attribute", "C. Relationship", "D. Weak Entity"))                
                            
            
                    answers = ("A", "D", "D", "C", "C", "A", "C")
                    guesses = []
                    dbms_score = 0
                    question_number = 0 
                    print()
                    for question in questions:
                        print(question)
                        for option in options[question_number]:
                            print(option)
                    
                        guess = input("Enter (A,B,C,D):").upper()
                        guesses.append(guess)
            
                        if guess == answers[question_number]:
                            print("CORRECT")
                            dbms_score += 1
                        else:
                            print("INCORRECT")    
                        question_number += 1
                        print()
            
                    print()
                    dbms_score = int((dbms_score/len(questions))*100)
                    dbms_scores[username]=dbms_score
                    # print(f"Your score of DBMS Quiz is {dbms_score}%")       
          

                  elif choice =='3':
                     print("DSA QUIZ")

            
                     questions = (
                         "1. Which of the following is a linear data structure?",
                         "2. What is the time complexity of binary search?",
                         "3. Which data structure follows the Last In First Out (LIFO) principle?",
                         "4. In which type of data structure are elements stored in a hierarchy?",
                         "5. What is the best time complexity for bubble sort?",
                         "6. Which of the following data structures allows insertion and deletion at both ends?",
                         "7. In a max heap, the highest value element is present at which position?"
                     )


                     options = (
                         ("A. Tree", "B. Graph", "C. Array", "D. Set"),
                         ("A. O(n)", "B. O(log n)", "C. O(n^2)", "D. O(1)"),
                         ("A. Queue", "B. Stack", "C. Array", "D. Tree"),
                         ("A. Queue", "B. Stack", "C. Array", "D. Tree"),
                         ("A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(n^2)"),
                         ("A. Stack", "B. Queue", "C. Deque", "D. Linked List"),
                         ("A. Root", "B. Leaf", "C. Middle", "D. None of these")
                     )

            
        
                     answers = ("C","B","B","D","A","C","A")
                     guesses = []
                     dsa_score = 0
                     question_number = 0 
                     print()
                     for question in questions:
                         print(question)
                         for option in options[question_number]:
                             print(option)
                    
                         guess = input("Enter (A,B,C,D):").upper()
                         guesses.append(guess)
            
                         if guess == answers[question_number]:
                             print("CORRECT")
                             dsa_score += 1
                         else:
                             print("INCORRECT")    
                         question_number += 1
                         print()
            
                     print()
                     dsa_score = int((dsa_score/len(questions))*100)
                     dsa_scores[username] = dsa_score
                    #  print(f"Your score of DSA Quiz is {dsa_score}%")       

                  else:
                      print("you entered wrong choice.")
                      break
            else:
                print("you entered wrong password.")
        else:
            print("user doesn't exist. Register first .")


def Show_results():
       username = input("Enter your username: ").lower()
       if username in users:
           print(f"Welcome {username}.")
           password = input("Enter password.")
           if password == data[username]:
               print("You can view results.")
               print(f"Results for {username}:")

               py_score = python_scores.get(username, 'Not attempted')
               dbms_score = dbms_scores.get(username, 'Not attempted')
               dsa_score = dsa_scores.get(username, 'Not attempted')

               print(f"Python Quiz Score: {py_score}%")
               print(f"DBMS Quiz Score: {dbms_score}%")
               print(f"DSA Quiz Score: {dsa_score}%")
           else:
               print("You entered the wrong password.")
       else:
            print("User doesn't exist. Register first.")


print("""Choices: 
        1.Registration
        2.Login
        3.Attempt Quiz
        4.Show Result
        5.Exit""")


while True:
    choice = input("enter your choice:")
    
    
    if choice =='1':
       Registration()
       
    elif choice =='2':
       Login()
     
    elif choice =='3':
        Attempt_quiz()
    
    elif choice == '4': 
        Show_results()

    elif choice =='5':    
          exit()
    
    else:
        print("Invalid choice.Enter correct choice.")
           