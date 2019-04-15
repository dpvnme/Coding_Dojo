# # 1. TASK: print "Hello World"
# print( "Hello World" )
# # 2. print "Hello Noelle!" with the name in a variable
# name = "Noelle"
# print( "Hello " + name + "!" )	# with a comma
# print( "Hello", name, "!" )	# with a +
# # 3. print "Hello 42!" with the number in a variable
# name = 42
# print( "Hello", name+"!")	# with a comma
# print( "Hello"+ str(name) )	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print( fave_food1.format() ) # with .format()
# print( f"{fave_food2}" ) # with an f string

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz
