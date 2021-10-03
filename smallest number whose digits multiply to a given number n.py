#Find the smallest number whose digits multiply to a given number n
Given a number ‘n’, find the smallest number ‘p’ such that if we multiply all digits of ‘p’, we get ‘n’. The result ‘p’ should have minimum two digits.
Examples: 
Input:  n = 36
Output: p = 49 
// Note that 4*9 = 36 and 49 is the smallest such number

Input:  n = 100
Output: p = 455
// Note that 4*5*5 = 100 and 455 is the smallest such number

Input: n = 1
Output:p = 11
// Note that 1*1 = 1

Input: n = 13
Output: Not Possible

Soluion:

n=int(input())
if n<10:
    print(n+10)
elif n>10:
    for i in range(10,n//2):
        if n%i==0:
            r=[]
            s=" "
            for i in range(9,1,-1):
                while n%i==0:
                    n=n/i
                    r.append(i)
            print(''.join(map(str, r[-1::-1])))
            break
        else:
            print("NOT POSSIBLE !!")
            break
