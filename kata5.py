def solution(blocks):
    n = len(blocks)
    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        if blocks[i] >= blocks[i - 1]:
            left[i] = left[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if blocks[i] >= blocks[i + 1]:
            right[i] = right[i + 1] + 1

    max_distance = 0
    for i in range(n):
        max_distance = max(max_distance, left[i], right[i])

    return max_distance

blocks1 = [2, 6, 8, 5]
result1 = solution(blocks1)
print("For the first set of blocks [2, 6, 8, 5], the longest possible distance between the frogs is:", result1)

blocks2 = [1, 5, 5, 2, 6]
result2 = solution(blocks2)
print("For the second set of blocks [1, 5, 5, 2, 6], the longest possible distance between the frogs is:", result2)

blocks3 = [1, 1]
result3 = solution(blocks3)
print("For the third set of blocks [1, 1], the longest possible distance between the frogs is:", result3)
