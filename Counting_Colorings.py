#################
#
# 
# This program is to show that Theorem 3 
#
#################

import math as math
import itertools as iter
from tqdm import tqdm

# 
# params (num_rows, num_cols)
# Creation of the incidence matrix. Asks the user to specify what vertices are connected between each edge
# Returns a 2D Matrix
#
def incidenceM_Creation(num_rows, num_cols):
    # Initialize the incidence matrix with zeros
    matrix = [[0] * num_cols] * num_rows

    print("Enter the incidence matrix(one row at a time and space-seperated values):")
    for cols in range(num_cols):
        if (cols == 0):
            print(f"    E{cols + 1}", end=" ")
        else:
            print(f"E{cols + 1}", end=" ")
    for i in range(num_rows):
        print()
        row = input(f"V{i + 1}: ").strip().split()
        if len(row) != num_cols:
            print("Error: Number of elements in the row does not match the number of columns.")
            return None
        matrix[i] = [int(val) for val in row]
    print()
        
    return matrix


# 
# params (num_rows)
# Creation of the edge matrix. Asks the user to specify what edges to keep. 
# Returns a 1D Matrix
#
def edgeID_Creation(num_rows):
    matrix = []
    print(f"\nEnter the edges you want to keep('1' to keep, '0' for identity): ")
    for i in range(num_rows):
        matrix.append(int(input(f"Edge {i + 1}: ")))
        print()
    return matrix


#
# params (n, length)
# Takes in a range for the permutation should be
#
def generate_permutations(n, length):
    return [list(perm) for perm in iter.product(range(1, n + 1), repeat=length)]


#
# params (m, num_vertices, num_edges, incidence_matrix, p_edges, colorings)
# Takes in the fold number, vertices, edges, the incidence matrix, the permutation of edges, and every coloring.
# Will then compute every coloring which succeeds.
# Returns every good coloring, c.
# TODO: Explain c is mathcal u
#
def coloring_function(m, num_vertices, num_edges, incidence_matrix, p_edges, colorings):
    c = 0
    for i in range(m**num_vertices):
        z = 0
        for j in range(num_edges):
            a = -1
            b = -1
            for k in range(num_vertices):
                if (incidence_matrix[k][j] == 1):
                    a = b
                    b = k
            if (p_edges[j][colorings[i][a] - 1] != colorings[i][b]):
                z += 1
        if (z == num_edges):
            c += 1
    return c



# Get the vertices and edges from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Get the graph
incidence_matrix = incidenceM_Creation(num_vertices, num_edges)
#print(incidence_matrix)

#Ask for the fold number from the user, 'm'
m = int(input("\nEnter the fold number: "))


permutations = list(iter.permutations(range(1, m + 1)))
#print(permutations)

#p_edges = array2D_Creation(num_edges, m, "edge permutation")
#print(p_edges)


# Generate every possible coloring by taking the fold number and then the length of the permutation from the vertices
colorings = generate_permutations(m, num_vertices)
#print(colorings)

# D is the max
# d is the min
D = 0
d = (m**num_vertices)

permutations = list(iter.permutations(range(1, m + 1)))
#print(permutations)

edges_id = edgeID_Creation(num_edges)
edges_sum = 0 
#print(edges_id)
for i in range(num_edges):
    edges_sum += edges_id[i]

L = generate_permutations(math.factorial(m), edges_sum)
#print(L)


p = [[0] * m] * num_edges #Cols and Rows
for i in tqdm (range(math.factorial(m)**edges_sum), desc="Calculating..."):
    for j in range(num_edges):
        count = 0
        if edges_id[j]== 1:
            p[j] = permutations[L[i][count] - 1]
            count += 1
        else:
            p[j] = permutations[0]
    c = coloring_function(m, num_vertices, num_edges, incidence_matrix, p, colorings)
    if c > D:
        D = c
    if c < d:
        d = c
print(f'Max: {D}')
print(f'Min: {d}')


#print(f"Number of colorings: {fold_Num**num_vertices}")
#print(f"Number of {fold_Num}-fold combinations: {m.factorial(fold_Num)**num_edges}")