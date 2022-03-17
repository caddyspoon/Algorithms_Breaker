class tree():
    def __init__(self, sp=0, p=-1):
        self.profit = sp
        self.parent = p
        self.children = []


def solution(sales, links):
    answer = 0
    return answer

# case 01.
sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
answer = 44

# # case 02.
# sales = [5, 6, 5, 3, 4]
# links = [[2,3], [1,4], [2,5], [1,2]]
# answer = 6
#
# # case 03.
# sales = [5, 6, 5, 1, 4]
# links = [[2,3], [1,4], [2,5], [1,2]]
# answer = 5
#
# # case 04.
# sales = [10, 10, 1, 1]
# links = [[3,2], [4,3], [1,4]]
# answer = 2

print(solution(sales, links) == answer)