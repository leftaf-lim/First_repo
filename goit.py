#sentence = "The quick brown fox jumps over the lazy dog"
#length = 0

#for i in sentence:
    #if i != " ": 
        #length += 1 

#print("Кількість не пробільних символів:", length)


#summary = 0

#for i in range(1 , 101 , 1):
    #summary = summary + i

    #print(summary)


#N = 10
#sum_squares = 0
#i = 1
#while  i <= N :
    #sum_squares += i * i
    #i = i + 1

#print(f"The sum of the squares of numbers from 1 to {N} is {sum_squares}")

#def function(n):
   #sum_squares = 0
    #i = 1
    #while i <= n:
        #sum_squares = sum_squares + i * i
        #i = i + 1
    #return sum_squares


#result = function(10)
#print(result)

#first_name = "John"
#last_name = "Doe"


#def get_initials(first_name, last_name):
    #length = len(first_name)
    #return last_name + " " + first_name[0] + "."


#formatted_name  = get_initials(first_name, last_name)
#print (formatted_name)


first = "Python"
second = "python"


def compare(first, second):
    
    if first.lower() == second:
        return True
    else:
        return False


result = compare(first, second)

print(result)


first = "World"
second = "WORLD"

def compare(first, second):
    
    if first.lower() == second.lower():
        return True
    else:
        return False


result = compare(first, second)

print(result)