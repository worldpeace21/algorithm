import collections

def solution(clothes):
    answer = 1
    category_list = [] # 카테고리만 저장할 리스트
    category_index = 1 # clothes 리스트의 [?][1]은 항상 카테고리를 지칭한다.
    for cloth in clothes:
        category_list.append(cloth[category_index])
    
    counter_category = collections.Counter(category_list)
    for key, value in counter_category.items():
        answer *= (value+1) # 안 입는 경우도 셈
    
    answer -= 1 # 어떠한 것도 안 입는 경우는 제외
    return answer