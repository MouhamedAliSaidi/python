#1 DIFFERENT THAN SOLUTIONS CODE !! ?
print("p1")
def countdown(n):
    return list(range(n, -1, -1))
print(countdown(5)) 


#2

print("p2")
def print_return(list):
    print(list[0])
    return list[1]
print(print_return([5,3]))

#3
print("p3")
def acclist(list):
    return list[0] + len(list)

print(acclist([1,2,3,4]))


#4 from solutions
print("p4")
def acclistcr(list):
    if len(list)<2:
        return False
    output=[]

    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

print(acclistcr([5,2,3,2,1,4]))
print(acclistcr([3]))               #no matter what the output will result in false statement 

#5 
print("p5")
def sizevalue(size,value):
    output=[]
    for i in range(0,size):
        output.append(value)
    return output

print(sizevalue(2,7))
print(sizevalue(6,2))

