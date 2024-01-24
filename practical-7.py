fh=open("output7.txt",'w')
string = input(' Enter the value:')
reverse = string[::-1]
if(reverse == string):
    fh.write(' The string is palindrome ')
else:
    fh.write(' The string is not palindrome ')