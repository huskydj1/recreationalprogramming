# Problem: Print the first 31 fibonacci numbers
# Source: https://code.golf/fibonacci#python
# Status: 77/36 bytes

# Submission
f = lambda i: i if i<=1 else f(i-1)+f(i-2)
print(*map(f,range(31)), sep='\n')