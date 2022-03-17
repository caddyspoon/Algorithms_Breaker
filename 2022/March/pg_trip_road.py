tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
answer2 = []
def solution(tickets):
    answer = []
    rawRoutes = ['ICN']
    tickets.sort()
    def dfs(tickets, routes):
        nonlocal answer

        if len(tickets) == 0:
            tempArr = routes[:]
            answer.append(tempArr)
            return

        crntLoc = routes[-1]
        for idx, ticket in enumerate(tickets):
            dep = ticket[0]
            arv = ticket[1]

            if dep == crntLoc:
                routes.append(arv)
                tempTickets = tickets[:]
                tempTickets.pop(idx)
                dfs(tempTickets, routes)
                routes.pop()


    dfs(tickets, rawRoutes)
    # print(answer)
    # answer.sort()
    # print(answer)
    return answer[0]
print('answer2: ', answer2)
print(solution(tickets))