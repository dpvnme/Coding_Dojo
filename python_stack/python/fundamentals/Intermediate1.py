import random
def randInt(min=0, max=100):
    if(min>max or max<0):
        exit
    else:
        num = round(random.random()*(max-min)+min)
        return num
#print(randInt()) 		    # should print a random integer between 0 to 100
print("random integer between 0 and 100:",randInt())
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print("random integer between 0 and 50:",randInt(max=50))
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print("random integer between 50 and 100:",randInt(min=50))
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
print("random integer between 50 and 500:",randInt(max=500, min=50))
