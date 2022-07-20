def solution(numbers):
    answer = 0

    for index in range(10):
        if index not in numbers:
            answer += index

    return answer

print(solution([5,8,4,0,6,7,9]))
print(solution([1,2,3,4,6,7,8,0]))