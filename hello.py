#This program asks your name.

print('Hello World!')
print('What is your name?') #asks your name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(str(len(myName)) + ' digits long.')
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')