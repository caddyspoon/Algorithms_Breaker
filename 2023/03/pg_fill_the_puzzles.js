const solution = (game_board, table) => {

};

const game_board = [
  [1, 1, 0, 0, 1, 0],
  [0, 0, 1, 0, 1, 0],
  [0, 1, 1, 0, 0, 1],
  [1, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 0, 0],
];
const table = [
  [1, 0, 0, 1, 1, 0],
  [1, 0, 1, 0, 1, 0],
  [0, 1, 1, 0, 1, 1],
  [0, 0, 1, 0, 0, 0],
  [1, 1, 0, 1, 1, 0],
  [0, 1, 0, 0, 0, 0],
];
const result = 14;

// const game_board = [
//   [0, 0, 0],
//   [1, 1, 0],
//   [1, 1, 1],
// ];
// const table = [
//   [1, 1, 1],
//   [1, 0, 0],
//   [0, 0, 0],
// ];
// const result = 0;

console.log(
  solution(game_board, table),
  solution(game_board, table) === result
);
