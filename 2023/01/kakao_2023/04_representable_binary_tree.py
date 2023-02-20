# 현재 수 이진 값으로 만들기
def conv_to_bin(num):
    # 이진 값으로로 변환된 수
    target_num = bin(num)[2:]

    # 노드개수
    node_cnt = len(target_num)
    
    # 완전 이진트리로 만들기 (포화 이진트리가 아닌 완전 이진트리로 판별하게 됨 cf. 42의 경우)
    # 다음은 2의 지수가 될 변수
    # 'exp' stands for exponential
    # (2의 제곱수 - 1)는 이진트리로 변환 했을 때 완전 이진트리가 된다.
    # 가령 (2**2 - 1 = 3)의 경우 2층 포화 이진트리, (2**3 - 1 = 7)의 경우 3층 포화 이진트리가 된다.
    # 그러므로 현재 값보다 큰 가장 가까운 2의 제곱수로 만든 이진트리가 말단 노드가 몇 개 비워진 이진트리가 된다.
    # 따라서 현재 수를 이진트리로 바꿨을 때 가장 이상적인 형태의 트리, 즉 완전 이진트리를 찾아준다.
    exp = 0
    while True:
        # 현재 값을 넘는 가장 가까운 2의 제곱 수인 경우
        if node_cnt < 2 ** exp:
            # 비어진 말단 최하단이자 최좌단의 노드 경우 0을 채워준다.
            return target_num.zfill(2 ** exp - 1)
        
        # 목표가 되는 수가 2**지수 보다 작을 경우 지수를 하나 더해줌
        else:
            exp += 1

def verdict(target_num):
    stack = [target_num]
    
    while stack:
        num = stack.pop()
        # 현재 노드의 길이가 2보다 작으면 리프 노드
        if len(num) <= 2:
            continue
    
        # 현재 이진수로 표현된 트리의 가운데 값이 최상단 부모 노드
        parent_node = len(num) // 2

        # 부모노드가 0인데 자식노드가 존재하는 경우 -> 트리로 표현되지 않는 표현식
        # 따라서 이진 트리로 만들 수 없다고 판별하여 0을 반환
        if (num[parent_node]) == '0' and '1' in num:
            return 0

        # 현재 이진트리를 반으로 쪼개서 왼쪽 트리를 스택에 넣기
        stack.append(num[:parent_node])
        # 오른쪽 트리를 스택에 넣기
        stack.append(num[parent_node + 1:])

    # 순회가 끝난 경우 완성할 수 있는 트리이므로 1을 반환
    return 1


def solution(numbers):
    answer = []

    # 현재 숫자들의 이진 값들이 담길 리스트
    bin_nums = []
    for num in numbers:
        # 현재 수를 이진수로 변환하기
        bin_nums.append(conv_to_bin(num))

    for bin_num in bin_nums:
        # 변환된 수를 이진트리로 만들 수 있는지 확인하기
        answer.append(verdict(bin_num))    

    return answer

# 확인해보기
solution([42])