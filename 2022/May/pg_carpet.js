function solution(brown, yellow) {
    const answer = [];

    let line = parseInt(brown / 2) - 2
    for (let i = 1; i < line; i++) {
        if (i * (line - i) === yellow) {
            let temp = line - i
            if (i < temp) {
                [i, temp] = [temp, i];
            }
            answer.push(i+2)
            answer.push(temp+2)
            break
        }
    }
    return answer;
}