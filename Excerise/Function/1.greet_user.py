import sys

def greet_users(str_list) :
    for x in str_list :
        print("Hello, "+str(x[0]).upper()+x[1:])

usernames = sys.argv[1:]
greet_users(usernames)