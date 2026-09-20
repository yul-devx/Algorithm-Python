## 해시
## 완주하지 못한 선수 

### 접근방법: 해시테이블
### 시간복잡도: O(n)
### 공간복잡도: O(n)

from collections import Counter     # dict 기반 자료구조

def solution(participant, completion):

    participant_dict = Counter(participant)

    for c in completion:
        participant_dict[c] -= 1

    for name, count in participant_dict.items():
        if count == 1:
            return name

    return ""

if __name__ == "__main__":
    answer1 = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    answer2 = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    answer3 = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

    print(answer1)  # "leo"
    print(answer2)  # "vinko"
    print(answer3)  # "mislav"