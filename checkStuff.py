# Example list A
A = [[10, 5], [20, 55], [30, 10], [40, 55]]

# Sort list A in descending order of the second elements of lists B
sorted_A = sorted(A, key=lambda x: x[1], reverse=True)

print(sorted_A)
