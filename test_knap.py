from submission import myDynamicProgramming

# Example from the PDF
n = 3
c = 11
V = [5, 8, 12]
W = [4, 5, 10]

Z, DP = myDynamicProgramming(n, c, V, W)

print("Z (chosen items):", Z)              # expected [1, 1, 0]
print("Max value:", DP[n][c])               # expected 13
print("DP table:")
for row in DP:
    print(row)
