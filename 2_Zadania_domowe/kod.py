# zad 1
def buzz_fizz(liczba): 
    for i in range(liczba):
        string = ""
        if (i % 3 == 0) and (i % 5 == 0):
            string = string + "BuzzFizz"
        elif i % 3 == 0:
            string = string + "Fizz"
        elif i % 5 == 0:
            string = string + "Buzz"
        elif (i % 3 != 0) and (i % 5 !=0):
            string = string + str(i)
        print(string, end=" ")
    # else:
        # print("Ups coś poszlo nie tak")
# zad 2
def rok_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

#zad 3 
def word_wrap(string, length):
    return((string[0 : length]) + "..."
    
# print(buzz_fizz(19))
#print(rok_przestepny(2020))
#print(word_wrap("wszyscy mamy żle w głowach, że żyjemy", 3))
print(word_wrap("wszyscy mamy żle w głowach, że żyjemy", 14))

print(word_wrap("hello word"), 3)