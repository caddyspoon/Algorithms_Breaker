tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    answer = []
    rawRoutes = ['ICN']

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
    answer.sort()
    return answer[0]

print(solution(tickets))