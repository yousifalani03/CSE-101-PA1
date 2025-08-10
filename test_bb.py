from submission import myBranchBound

C2 = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4],
]
X, ub_list, node_count = myBranchBound(C2)

def cost(X, C):
    return sum(C[i][j] for i in range(len(C)) for j in range(len(C)) if X[i][j]==1)

print("X="); [print(r) for r in X]
print("ub_list:", ub_list)     # should start high and drop at least once
print("node_count:", node_count)
print("cost(X):", cost(X, C2)) # should equal ub_list[-1]
