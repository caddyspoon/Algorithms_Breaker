# import re

# def solution(words, queries):
#     answer = []

#     for query in queries:
#         regex = re.compile(query)
#         re.match(regex, words)
#     return answer


def solution(words, queries):
    answer = []

    tdict = {'od': {}, 'rod': {}}
    for word in words:
        ctd = {word[-1]: '*'}
        rctd = {word[0]: {'*'}}
        for i in range(len(word)-2, -1, -1):
            temp = {}
            char = word[i]
            temp[char] = ctd
            ctd = temp
        print(ctd)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]

print(solution(words, queries))
