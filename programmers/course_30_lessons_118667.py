from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1S, q2S = sum(queue1), sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    while True:
        if q1S > q2S:
            n = q1.popleft()
            q2.append(n)
            q1S -= n
            q2S += n
            answer += 1
        elif q1S < q2S:
            n = q2.popleft()
            q1.append(n)
            q1S += n
            q2S -= n
            answer +=1
        else:
            break
        if answer > 1000000:
            answer = -1
            break

    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2]	, [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))