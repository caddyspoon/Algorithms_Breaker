function solution(n, results) {
    let answer = 0

    const graph = new Array(n+1)

    for (let i = 1; i < n+1; i++) {
        graph[i] = new Array(2)
        graph[i][0] = new Set()
        graph[i][1] = new Set()
    }

    for (const result of results) {
        const [winner, loser] = result
        graph[winner][1].add(loser)
        graph[loser][0].add(winner)
    }

    for (let i = 1; i < n+1; i++) {
        const winners = graph[i][0]
        const losers = graph[i][1]

        // console.log(...winners)
        // console.log(...losers)

        for (const winner of winners) {
            // console.log(...graph[winner][1], ...losers)
            // graph[winner][1] = new Set (...graph[winner][1], ...losers)
            for (const loser of losers) {
                graph[winner][1].add(loser)
            }
        }

        // console.log()

        for (const loser of losers) {
            // console.log( ...graph[loser][0], ...winners)
            // graph[loser][0] = new Set (...graph[loser][0], ...winners)
            for (const winner of winners) {
                graph[loser][0].add(winner)
            }
        }

    }

    for (let i = 1; i < n+1; i++) {
        if (graph[i][0].size + graph[i][1].size === n-1) {
            answer += 1
        }
    }


    return answer
}

const n = 5
const results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
const result = 2

console.log(solution(n, results) === result)