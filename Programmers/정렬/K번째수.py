# 정렬
## K번째수

def solution(array, commands):

    answer = []

    for (i, j, k) in commands:
        answer.append(sorted(array[i-1:j])[k]) 

    return answer   

if __name__ == "__main__":
    answer1 = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	)

    print(solution(answer1))    # [5, 6, 3]