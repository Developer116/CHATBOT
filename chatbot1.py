import sys
import os
import random
import time

# ChatBot templates for the Username and the Password
userName_template = "CHATBOT1"
password_template = "chatbot"

# Define a dictionary that stores the responses of a chatbot
normal_responses = {"What is your name" : ["My name is ChatBot1",
                                    "ChatBot1!", "Tell me your name",
                                    "Try Something else!"], 
             "Who is your creater" : ["I was created by Avi"],
             "Default" : ["ChatBot1 is not working!",
                          "The message your are looking for is not here"]}

# function to return response for the user question
def return_message(user_message):
    if user_message in normal_responses:
        bot_message = random.choice(normal_responses[user_message])
    else:
        bot_message = random.choice(normal_responses["Default"])
    return bot_message

# Function to terminate the ChatBot
def bot_termination():
    print("ChatBot1 is now Shutting Down")
    time.sleep(2)
    print("ChatBot1 off")

# function to perform ask and return function
def chatbot1_function():
    invoke_user = (int)(input("Press 1 to ask questions from the chatbot and 2 to Exit"))
    # Continue ask the user till 2 is pressed
    while invoke_user != 2:
        if invoke_user == 1:
            invoke_message = (str)(input("User : "))
            take_return_value = return_message(invoke_message)
            time.sleep(1)
            print("ChatBot : {}".format(take_return_value))
            invoke_user = (int)(input("Press 1 to ask questions from the chatbot and 2 to Exit"))
        elif invoke_user == 2:
            bot_termination()
    bot_termination()

# default function main() to process and call function return_message()
if __name__ == "__main__":
    print("Hey! Welcome to ChatBot1")
    invoke_userName = (str)(input("UserName : "))
    invoke_password = (str)(input("Password : "))
    if ((invoke_userName == userName_template) and (invoke_password == password_template)):
        chatbot1_function()
    else:
        print("Hey! I think the username and the password are wrong or either of them is wrong")
        bot_termination()
        
