def solve(line):
    ans = 0
    i = 0
    l = len(line)
    while i < len(line):
        if i + 4 <= l and line[i:i + 4] == 'mul(':
            j = i + 4
            if line[j:j + 3].isdigit():
                j = j + 3
            elif line[j:j + 2].isdigit():
                j = j + 2
            elif line[j:j + 1].isdigit():
                j = j + 1
            if line[j] == ',':

                if line[j + 1:j + 4].isdigit() and line[j + 4] == ')':
                    ans += int(line[j + 1:j + 4]) * int(line[i + 4: j])
                elif line[j + 1:j + 3].isdigit() and line[j + 3] == ')':
                    ans += int(line[j + 1:j + 3]) * int(line[i + 4: j])
                elif line[j + 1:j + 2].isdigit() and line[j + 2] == ')':
                    ans += int(line[j + 1:j + 2]) * int(line[i + 4: j])
        i += 1
    return ans


s = 0

with open('data.txt') as file:
    for line in file:
        s += solve(line)
print(s)


#from chatgpt
# import re


# def sum_mul_results(memory):
#     """
#     Scans the corrupted memory string for valid mul(X,Y) instructions
#     and returns the sum of all multiplication results.
#
#     Parameters:
#     memory (str): The corrupted memory string.
#
#     Returns:
#     int: The sum of all valid multiplication results.
#     """
#     # Define the regex pattern for valid mul instructions
#     pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
#
#     # Find all matches in the memory string
#     matches = re.findall(pattern, memory)
#
#     # Calculate the sum of all multiplication results
#     total = 0
#     for x, y in matches:
#         product = int(x) * int(y)
#         total += product
#         print(f"Found mul({x},{y}) = {product}")
#
#     return total
#
#
# # Example usage:
# if __name__ == "__main__":
#     corrupted_memory = (
#         "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#     )
#     result = sum_mul_results(corrupted_memory)
#     print(f"Total sum of multiplication results: {result}")
