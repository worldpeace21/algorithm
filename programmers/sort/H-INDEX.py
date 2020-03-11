def solution(citations):
    answer = 0
    max = len(citations) # H-INDEX의 최댓값은 N 즉 citations의 길이이다.
    for h in range(max,0,-1): # citations의 길이부터 1까지 거꾸로 조사한다.
        count = 0
        for citation in citations:
            if citation >= h:
                count = count + 1
            if count >= h:
                answer = h
                return answer
    return answer # 위 이중 for문의 조건을 만족하지 못하면 H-INDEX는 0이다.