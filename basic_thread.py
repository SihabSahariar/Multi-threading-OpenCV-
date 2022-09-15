# importing the threading module 
import threading 
# importing the time module 
import time
# Function to print "Hello", however, the function sleeps
# for 2 seconds at the 11th iteration
def print_hello(): 
  for i in range(20):
    if i == 10:
      time.sleep(2)
    print("Hello")
# Function to print numbers till a given number
def print_numbers(num): 
  for i in range(num+1):
    print(i)
# Creating the threads. Target is set to the name of the
# function that neeeds to be executed inside the thread and
# args are the arguments to be supplied to the function that
# needs to be executed.
print("Greetings from the main thread.")
thread1 = threading.Thread(target = print_hello, args = ())
thread2 = threading.Thread(target = print_numbers, args = (10,))  
# Starting the two threads
thread1.start() 
thread2.start() 
print("It's the main thread again!")
