import os
import math


def computegcd(n1,n2):
    if n2> n1 :
        n1,n2 = n2 , n1 

    if n1 == n2:
        return n1 
    
    if n1 == 0 or n2 ==0:
        return 0
    
    if n1 ==1 or n2 ==1 :
        return 1
    
    ###if n2 divides n1 then n2 is the gcd
    if n1%n2 ==0 :
        return n2 
    else:
        ##otherwise as per euclid we will search for the diff  and try to find the gcd between the smallest 
        ## of the the two numbers and the difference between the two numbers. 
        diff = n1 - n2 
        return computegcd(n2 , diff)

def euclidgcd(n1 , n2):
    if n2 > n1 :
        n1,n2 = n2 , n1 
    
    if n2 ==1 :
        return 1

    rem = n1%n2 
    if rem == 0:
        return n2

    else:
        return euclidgcd(n2, rem)

if __name__ == "__main__":
    first_num = int(input("Enter the first input:"))
    Second_num = int(input("Enter the Second input:"))
    print(f" GCD is {computegcd(first_num,Second_num)}")
    print(f" Euclid GCD is {euclidgcd(first_num,Second_num)}")