def solution(phone_book):
    answer = True
    num_phone_number = len(phone_book) # 전화번호 리스트의 길이
    for index1 in range(0, num_phone_number):
        last_index = len(phone_book[index1]) # 비교할 전화번호의 길이 -> 접두어 범위를 결정한다.
        for index2 in range(0, num_phone_number):
            if index1 != index2: # 자기 자신과는 비교하지 않는다.
                if phone_book[index1] == phone_book[index2][0:last_index]: # 접두어가 같다면
                    answer = False
                    return answer # 이렇게 하면 for문을 끝까지 돌지 않아도 된다. -> 효율을 높이는 방법!
                
    return answer