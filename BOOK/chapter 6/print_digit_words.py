n=(int(input("Enter a number : ")))
while n!=0:
    num=n%10
    if num==1:
        print("one",end=" ")
    if num==2:
        print("two",end=" ")
    if num==3:
        print("three",end=" ")
    if num==4:
        print("four",end=" ")
    if num==5:
        print("five",end=" ")
    if num==6:
        print("six",end=" ")
    if num==7:
        print("seven",end=" ")
    if num==8:
        print("eight",end=" ")
    if num==9:
        print("nine",end=" ")
    if num==0:
        print("zero",end=" ")
    n//=10
    
