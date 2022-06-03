# even numbers are those numbers which can be divided by two 
# eg. 2, 4, 6,  8, 10 
From  = int(input('Even number \n\tfrom : ')) # don't use from in lowercase because it is reserved keyword 
To = int(input('\tTo: '))
print(f'So even numbers b/w {From} to {To} are : ')

for num in range(From , To+1):
    if (num%2 ==0):
        print(num) 

