#Problem 5: Even Number Sum
#Write a Python program that calculates the sum of all even numbers from 1 to n (inclusive).

#Test Case:
#Input: 6 → Output: 2 + 4 + 6 = 12

n = int(input("Enter number: "))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum+i
print(sum)
