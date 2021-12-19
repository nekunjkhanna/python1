#python basics revision
#1 - String
x = "future engineer"
print(x[1::3])#the output should be u r e i e
#lesson 1 learned - the print statement of string follows x[start:stop:step]
#step follows convention that every elements position differs with step - 1
y = "perfectionist"
z = "Earth"
n = "nekunjkhanna123"
o = "bello"
print(y[::4])#the output should be peot

#traversing
for i in x:
    print(i)
    for i in y:
        print(y)
        #the output shall be f perfectionist e perfectionist and so on
#len
print(len(x) + len(y))#the output shall be 15 + 13 = 28
#capatilize
print(x.capitalize())#the output shall be Future engineer
#title
print(x.title())#the output shall be Future Engineer
#istitle
print(z.istitle())#the output shall be True
#upper
print(x.upper())#the output shall be FUTURE ENGINEER
#isupper
print(x.isupper())#the output shall be False
#lower
print(x.lower())#the output shall be future engineer
#islower
print(x.islower())#the output shall be True
print(z.islower())#the output shall be False
#count - counts the number of times a char appears in the given range of a string
print(x.count("u"))#output shall be 2
print(x.count("u",3,4))#output shall be 1
#index - tells us the index position of the first occurence of character and shows
#        error if not found
print(x.index("u"))#output shall be 1
#print(x.index("z"))#shows error
print("bello")
#find - it does the same work as index, only diff is it displays -1 if not found
print(x.find("u"))#output shall be 1
print(x.find("z"))#output shall be -1
#note---->
#the range of count follows same range as print statement
#alphanumeric(isalnum)- tells us if string is contains both alphabets and numbers
#note---->
#also applicable to isalpha, isdigit, istitle
#it displays true only if numbers and alphabets are present and nothing else
print(n.isalnum())#output shall be True
#split - it splits the string into
#note ---->
#the split takes place such that the char to be splited is not there and the splitted
#string appears in form of list
print(x.split("u"))#output shall be ['f', 't', 're engineer']
#partition - same work as split just that the out is displayed in form of tuple
#            and split taken in form ("string before char to be splitted","char
#            being splitted","char ahead of string")
print(x.partition("u"))#output shall be ('f', 'u', 'ture engineer')
#replace - it replaces the given alphabet/alphabets by the given alphabet
#even after replace the string remains same
print(o.replace("b","h"))#output shall be hello
#lstrip - strips off the given alphabets from the front
print(o.lstrip("b"))
#rstrip - strips off the given alphabets from behind the string
print(o.rstrip("o"))






      
