#Program to find number of words and characters for a string
string=input("Enter a string")
print("1. Find the number of words in the string")
print("2. Find the number of characters in the string")
print("3. Create a new string")
print("4. Exit")
list=[]
while True:
    choice=int(input("Enter your choice"))
    if (choice==1):
        for i in range(0,len(string)):
            list.append(string[i])

        words=list.count(" ")+1
        print("The number of words in your string is", words)
        list=[]
    elif (choice==2):
        print("The number of characters in your string is", len(string))

    elif (choice==3):
        string=input("Enter a string")
        print("1. Find the number of words in the string")
        print("2. Find the number of characters in the string")
        print("3. Create a new string")
        print("4. Exit")
        list=[]
    elif (choice==4):
        break
    else:
        print("Invalid Input. Please Try Again")
        
