#Program to display the Fibonacci sequence up to nth terms
nterms = int(input("Enter the no. of terms: "))

#First two terms
n1,n2 = 0,1
count = 0

#Check if the number of terms is valid
if nterms <= 0:
    print("Enter only positive no.")
else:
    print("Fibonacci Sequence upto",":", nterms)
    while count < nterms:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1

# Enter the no. of terms: 1
# Fibonacci Sequence upto : 1
# 0

# Enter the no. of terms: 2
# Fibonacci Sequence upto : 2
# 0
# 1

# Enter the no. of terms: 5
# Fibonacci Sequence upto : 5
# 0
# 1
# 1
# 2
# 3
