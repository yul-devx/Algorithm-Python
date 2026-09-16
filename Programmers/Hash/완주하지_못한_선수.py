## 해시
## 완주하지 못한 선수 

from collections import Counter

def solution(participant, completion):

    participant_dict = dict(Counter(participant))

    for c in completion:
        participant_dict[c] -= 1

        if not participant_dict[c]:
            participant_dict.pop(c)

    return list(participant_dict)[0]

if __name__ == "__main__":
    answer1 = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
    answer2 = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
    answer3 = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

    print(answer1)  # "leo"
    print(answer2)  # "vinko"
    print(answer3)  # "mislav"