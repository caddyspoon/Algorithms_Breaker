def solution(sales, links):
    answer = 0

    return answer

case_cnt = 4
sales = [[14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [5, 6, 5, 3, 4], [5, 6, 5, 1, 4], [10, 10, 1, 1]]
links = [
    [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]],
    [[2,3], [1,4], [2,5], [1,2]],
    [[2,3], [1,4], [2,5], [1,2]],
    [[3,2], [4,3], [1,4]]
]
result = [44, 6, 5, 2]

for case in range(case_cnt):
    print(solution(sales[case], links[case]) == result[case])