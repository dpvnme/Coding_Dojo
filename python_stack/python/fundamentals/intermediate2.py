# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

#Change the last_name of the first student from 'Jordan' to 'Bryant'
# print(students)
# students[0]['last_name'] = 'Bryan'
# print(students)

#In the sports_directory, change 'Messi' to 'Andres'
# print(sports_directory)
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# print(z)
# z[0]['y']=30
# print(z)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def iterateDictionary(lst):
#     for i in range (len(lst)):
#         print(lst[i])
    
my_dict = { "name": "Noelle", "language": "Python" }
for k in students[1]:
    print(students[1]['first_name'])
# output: Noelle, Python




# iterateDictionary(students)
