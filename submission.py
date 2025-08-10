from copy import copy, deepcopy
import sys, os
import numpy as np

# Name: Yousif Alnai
# PID: 

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################

def rowMin(A):
    """
    Row min lower bound , LB = sum of each rows min
    
    """
    if not A:
        return 0
    s = 0
    for row in A:
        m = row[0]
        for v in row[1:]:
            if v < m:
                m = v
        s += m
    return s

def calcMatrixMinor(A, i, j):
    #remove row i and comumn j from A returns remaining matrix
    n = len(A)
    minor = []
    for r in range(n):
        if r == i:
            continue
        row = A[r]
        new_row = row[:j] + row[j+1:]
        minor.append(new_row)

    return minor

def minElement(arr):
    #return (min_value, min_index) for a list arr

    m_val = arr[0]
    m_idx = 0
    for i in range(1,len(arr)):
        if arr[i] < m_val:
            m_val = arr[i]
            m_idx = i
    return m_val, m_idx

def SNH(A):
    #smallest number heuristic

    if not A:
        return 0
    total = 0
    M = [row[:] for row in A]
    n = len(M)

    rows = list(range(n))
    cols = list(range(n))
    for _ in range(n):
        best_val = None
        best_r = best_c = None
        for ri, r in enumerate(rows):
            row = M[r]
            for ci, c in enumerate(cols):
                v = row[c]
                if best_val is None or v < best_val:
                    best_val = v
                    best_r = ri
                    best_c = ci
        total += best_val

        rows.pop(best_r)
        cols.pop(best_c)
    return total


def myBranchBound(C):
    def SNH_assign(A_sub, cols_sub):
        if not A_sub:
            return 0, []
        m = len(A_sub)
        rows = list(range(m))          # local row indices
        local_cols = list(range(m))    # local col indices 0..m-1
        total = 0
        # res[k] = original column index chosen for local row k
        res = [None] * m

        for _ in range(m):
            best = None  # (val, ri, ci) with ri,ci as indices into rows/local_cols
            for ri, r in enumerate(rows):
                for ci, c in enumerate(local_cols):
                    v = A_sub[r][c]
                    if best is None or v < best[0]:
                        best = (v, ri, ci)
            v, ri, ci = best
            total += v
            # map local column -> original column using cols_sub
            chosen_local_col = local_cols[ci]
            res[rows[ri]] = cols_sub[chosen_local_col]
            # remove chosen row & col from consideration
            rows.pop(ri)
            local_cols.pop(ci)

        return total, res


    #(lb, creation_id, depth, g, path_cols, A_sub, cols_sub)
    n = len(C)
    node_count = 0
    creation_id = 0

    # UB via SNH on full C (also store a feasible assignment path)
    init_cost, init_cols = SNH_assign(C, list(range(n)))
    best_ub = init_cost
    ub_list = [best_ub]
    best_path = init_cols[:]  #(feasible)

    #root
    root_lb = rowMin(C)
    root = (root_lb, creation_id, 0, 0, [], [row[:] for row in C], list(range(n)))
    creation_id += 1
    node_count += 1
    queue = [root]

    # best-first: repeatedly take node with smallest (lb, creation_id)
    while queue:
        # pop min
        idx = 0
        for i in range(1, len(queue)):
            if queue[i][0] < queue[idx][0] or (queue[i][0] == queue[idx][0] and queue[i][1] < queue[idx][1]):
                idx = i
        lb, cid, depth, g, path, A_sub, cols_sub = queue.pop(idx)

        # prune
        if lb >= best_ub:
            continue

        # if complete assignment
        if depth == n:
            if g < best_ub:
                best_ub = g
                ub_list.append(best_ub)
                best_path = path[:]  # exact completion
            continue

        # branch on current agent level (row 0 of A_sub)
        # branch on current agent level (row 0 of A_sub)
        m = len(A_sub)
        for j in range(m):
            new_g = g + A_sub[0][j]
            new_A = calcMatrixMinor(A_sub, 0, j)
            new_cols = cols_sub[:j] + cols_sub[j+1:]
            new_path = path + [cols_sub[j]]

            # count node as soon as it's constructed (even if pruned)
            node_count += 1

            child_lb = new_g + rowMin(new_A)

            # try greedy feasible to tighten UB
            greedy_cost, greedy_cols = SNH_assign(new_A, new_cols)
            child_ub = new_g + greedy_cost
            if child_ub < best_ub:
                best_ub = child_ub
                ub_list.append(best_ub)
                best_path = new_path + greedy_cols

            # enqueue only if worth exploring
            if child_lb < best_ub:
                queue.append((child_lb, creation_id, depth + 1, new_g, new_path, new_A, new_cols))
                creation_id += 1

    # ← OUTSIDE the while queue loop
    X = [[0] * n for _ in range(n)]
    if best_path and len(best_path) == n:
        for i, j in enumerate(best_path):
            X[i][j] = 1
    return X, ub_list, node_count


#######################################################
##############       QUESTION 2 HERE   ################
#######################################################
def myDynamicProgramming(n, c, V, W):
    """
    0/1 Knapsack DP
    Returns:
      Z: length-n 0/1 vector 
      DP: (n+1) x (c+1) value table
    """
    #build DP table
    DP = [[0] * (c + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wi = W[i - 1]
        vi = V[i - 1]
        for cap in range(c + 1):
            if wi > cap:
                DP[i][cap] = DP[i - 1][cap]
            else:
                without = DP[i - 1][cap]
                with_it = vi + DP[i - 1][cap - wi]
                DP[i][cap] = with_it if with_it > without else without

    # backtrack to build Z
    Z = [0] * n
    cap = c
    for i in range(n, 0, -1):
        if DP[i][cap] != DP[i - 1][cap]:
            Z[i - 1] = 1
            cap -= W[i - 1]
    return Z, DP

