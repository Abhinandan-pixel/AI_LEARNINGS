# Calculate the first 1,000,000 terms of the series 1 - 1/3 + 1/5 - 1/7 + ...

# Initialize variables
num_terms = 1000000
result = 0.0

# Calculate the series
for n in range(num_terms):
    term = (-1) ** n / (2 * n + 1)  # Alternating series: 1, -1/3, 1/5, -1/7...
    result += term

# Multiply the total by 4 to get pi approximation
final_result = result * 4

# Print the result
print(final_result)