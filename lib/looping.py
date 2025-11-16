#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    w=10   #create a variable w and assign it to 10
    while w>0:   #create a while loop that runs while w is greater than 0
        print(w)  #print the value of w in the console as the loop runs
        w-=1    #decrease the value of w by 1 each time the loop runs and also makes sure the loop will eventually end

    print("Happy New Year!")    #print "Happy New Year!" after the loop ends

def square_integers(int_list):
    # code goes here!
    return [num * num for num in int_list]  #use a list comprehension to create a new list containing the squares of each integer in the input list

square_integers([1, 2, 3, 4, 5])  #example input list to test the function

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()  #call the fizzbuzz function to execute it
