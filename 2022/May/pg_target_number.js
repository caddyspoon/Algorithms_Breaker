function solution(numbers, target) {
    let answer = 0;

    const recur = (crntValue = 0, n = 0) => {
        if (n == numbers.length) {
            if (target === crntValue) {
                answer += 1
            }
            return
        }

        recur(crntValue + numbers[n], n + 1)
        recur(crntValue - numbers[n], n + 1)
    }

    recur()

    return answer;
}

// case 1
// const numbers = [1, 1, 1, 1, 1]
// const target = 3
// const answer = 5

// case 2
const numbers = [4, 1, 2, 1]
const target = 4
const answer = 2

console.log(solution(numbers, target) === answer)