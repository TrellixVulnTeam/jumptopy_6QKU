import threading

def print_hello():
    print("Hello World!")
    input()

t =  threading.Thread(target=print_hello)
t.daemon = True
t.start()

print("End")