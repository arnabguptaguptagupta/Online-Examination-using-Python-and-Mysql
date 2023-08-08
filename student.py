#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
import pandas as pd
import random
from datetime import datetime
import re


# In[4]:


import string
import datetime


# In[5]:


cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='85@2002$gA',
    port='3306',
    database='student'
)
cursor = cnx.cursor()  


# In[ ]:


def login():
    
        email = input('Email Address: ')
        password = input('Password: ')        
        query = "SELECT name FROM student_details WHERE email = %s AND password = %s"
        values = (email, password)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
                    print('\n Welcome,', user[0], '!\n')
                    while True:
                        print('1. Update Password')
                        print('2. Take Test')
                        print('3. Logout')
                    
                        c1=input('\n Enter your choice \n') 
                    
                        if c1 == '1':
                             update_password()
                        elif c1 =='2':
                             take_test()
                        elif c1 == '3':
                             break
                        else:
                            print('\n Invalid Choice \n')                                       
        else:
             print('Invalid Credentials. Login failed.\n')
                
                
def update_password():
    email = input('Enter your email address: ')
    old_password = input('Enter your old password: ')
    new_password = input('Enter your new password: ')

    query = "SELECT name FROM student_details WHERE email = %s AND password = %s"
    values = (email, old_password)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        update_query = "UPDATE student_details SET password = %s WHERE email = %s"
        update_values = (new_password, email)
        cursor.execute(update_query, update_values)
        cnx.commit()  
        print('Password updated successfully!\n')
        
    else:
        
        print('Invalid Email or Password. Password update failed.\n')

def display_time_remaining(start_time):
    elapsed_time = datetime.datetime.now() - start_time
    remaining_time = max(datetime.timedelta(minutes=2) - elapsed_time, datetime.timedelta())
    print("\nTime remaining: {}".format(remaining_time))

def take_test():
    email = input('Enter your email address: ')

    query = "SELECT roll, name FROM student_details WHERE email = %s"
    values = (email,)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        print('\nWelcome to the test, {}!'.format(user[1]))
        print('You have 2 minutes to complete the test.')
        print('The test will be auto-submitted after 2 minutes.\n')

        questions = [
            "What is the National Animal of India?",
            "What is the capital of the state Tamil Nadu?",
            "What is the square root of 144?",
        ]
        options = [
            ["A) Tiger", "B) Lion", "C) Elephant", "D) Monkey"],
            ["A) Bengaluru", "B) Vellore", "C) Chennai", "D) Trichy"],
            ["A) 17", "B) 13", "C) 11", "D) 12"],
        ]
        answers = ['A', 'C', 'D']

        score = 0
        start_time = datetime.datetime.now()

        for i in range(len(questions)):
            display_time_remaining(start_time)

            if datetime.datetime.now() - start_time >= datetime.timedelta(minutes=2):
                print("\nTime's up! Test auto-submitted.")
                break

            print("\nQuestion {}: {}".format(i + 1, questions[i]))
            for option in options[i]:
                print(option)

            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == answers[i]:
                score += 10

        elapsed_time = datetime.datetime.now() - start_time


        insert_query = "INSERT INTO student_scores1 (roll , name, email, score) VALUES (%s, %s, %s, %s)"
        insert_values = (user[0], user[1], email, score)
        cursor.execute(insert_query, insert_values)
        cnx.commit()

        print('\nTest completed!')
        print('Your score: {}/{}'.format(score, 30))
        print('Time taken: {} seconds'.format(elapsed_time.total_seconds()))
        print('Thank you for taking the test!\n')
    else:
        print('Invalid email. Test cannot be taken.\n')
    
while True:
    
        print('Student Quiz');
        print('************')
        print('\n')

        print('1. Login')
        print('2. Not interested')

        choice = input('Enter your choice: ')

        if choice == '1':   
                 login()
               
        elif choice =='2':
              break;
        else:
             print('Invalid choice')           


# In[ ]:





# In[ ]:




