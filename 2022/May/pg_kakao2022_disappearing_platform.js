function solution(board, aloc, bloc) {
    let answer = -1;

    return answer;
}

// Test Case 1.
const board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]];
const aloc = [1, 0];
const bloc = [1, 2];
const answer = 5;

// // Test Case 2.
// const board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]];
// const aloc = [1, 0];
// const bloc = [1, 2];
// const answer = 4;
// // Test Case 3.
// const board = [[1, 1, 1, 1, 1]];
// const aloc = [0, 0];
// const bloc = [0, 4];
// const answer = 4;
//
// // Test Case 4.
// const board = [[1]];
// const aloc = [0, 0];
// const bloc = [0, 0];
// const answer = 0;

console.log(solution(board, aloc, bloc) === answer);