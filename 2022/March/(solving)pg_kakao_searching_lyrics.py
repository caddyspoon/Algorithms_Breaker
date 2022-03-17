# import re

# def solution(words, queries):
#     answer = []

#     for query in queries:
#         regex = re.compile(query)
#         re.match(regex, words)
#     return answer


def solution(words, queries):
    answer = []

    # tdict = {'od': {}, 'rod': {}}
    # for word in words:
        # tdict = {tdict.get('od')
        # ctd = {word[-1]: '*'}
        # rctd = {word[0]: {'*'}}
        # for i in range(len(word)-2, -1, -1):
        #     temp = {}
        #     char = word[i]
        #     temp[char] = ctd
        #     ctd = temp
    # print(tdict)

    dict = {'straight': {}, 'reverse': {}}
    for word in words:
        pointer = dict['straight']
        rev_pointer = dict['reverse']
        for i in range(len(word)):
            char = word[i]
            rev_char = word[(i+1)* -1]
            pointer[char] = pointer.get(char, {})
            rev_pointer[rev_char] = rev_pointer.get(rev_char, {})
            if i == len(word) - 1:
                pointer[char] = '*'
                rev_pointer[rev_char] = '*'
            else:
                pointer = pointer[char]
                rev_pointer = rev_pointer[rev_char]
    for query in queries:
        if query[0] == '?':
            pointer = dict['reverse']
            query = query[::-1]
        else:
            pointer = dict['straight']

        cnt = 0
        flag = 1
        stack = []
        temp_answer = 0
        for i in range(len(query)):
            if query[i] == '?':
                cnt = len(query) - i
                stack = [pointer[elm] for elm in pointer]
                break
            try:
                pointer = pointer[query[i]]
            except:
                flag = 0
                break
        if flag:
            for elm in stack:
                depth = 1
                for char in str(elm):
                    if char == '{':
                        depth += 1
                    elif char == '}':
                        depth -= 1
                    elif char == '*' and depth == cnt:
                        temp_answer += 1

        answer.append(temp_answer)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]

print(solution(words, queries))
