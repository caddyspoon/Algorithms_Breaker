const solution = (beginning, target) => {
  let checkCnt = 0;
  const makeCheckBoard = () => {
    const board = new Array(beginning.length)
      .fill(0)
      .map(() => new Array(beginning[0].length).fill(0));

    for (let i = 0; i < beginning.length; i++) {
      for (let j = 0; j < beginning[0].length; j++) {
        if (beginning[i][j] !== target[i][j]) {
          board[i][j] = 1;        
        }
      }
    }
    return board;
  };

  const board = makeCheckBoard();
  const template = board[0].slice().join("");
  const revTemplate = [...template]
    .map((elm) => {
      if (elm === "0") {
        return 1;
      }
      return 0;
    })
    .join("");

  const isSameRow = (rowArr) => {
    const stringRowArr = rowArr.join("");
    let stand = "";

    if (template[0] !== stringRowArr[0]) {
      stand = revTemplate;
    } else {
      stand = template;
    }

  if (stand !== stringRowArr) {
    return false;
  }

    return true;
  };

  const isPossibleToMake = () => {
    for (let i = 0; i < board.length; i++) {
      if (!isSameRow(board[i])) {
        return false;
      }
    }
    return true;
  };

  if (!isPossibleToMake()) {
    return -1;
  }

  const flipNum = (num) => {
    if (num === 0) {
      return 1;
    }
    return 0;
  };

  // 시뮬레이션
  const countMinimum = () => {
    const _board1 = makeCheckBoard();
    const _board2 = makeCheckBoard();

    const w = _board1[0].length;
    const h = _board1.length;

    let cntCase1 = 0;
    let cntCase2 = 0;
    // 행(세로축)부터 뒤집기
    // console.log("We go right first");
    // console.log("init:");
    // console.log(_board);
    // console.log();
    for (let i = 0; i < w; i++) {
      if (_board1[0][i] === 1) {
        for (let j = 0; j < h; j++) {
          _board1[j][i] = flipNum(_board1[j][i]);
        }
        cntCase1 += 1;
      }
      // console.log(_board1);
      // console.log();
    }

    for (let i = 0; i < h; i++) {
      if (_board1[i][0] === 1) {
        for (let j = 0; j < w; j++) {
          _board1[i][j] = flipNum(_board1[i][j]);
        }
        cntCase1 += 1;
      }
      // console.log(_board1);
      // console.log();
    }

    // 세로축으로 먼저!
    // console.log("We go down first");
    // console.log("init:");
    // console.log(_board);
    // console.log();
    for (let i = 0; i < h; i++) {
      if (_board2[i][0] === 1) {
        for (let j = 0; j < w; j++) {
          _board2[i][j] = flipNum(_board2[i][j]);
        }
        cntCase2 += 1;
      }
      // console.log(_board2);
      // console.log();
    }

    for (let i = 0; i < w; i++) {
      if (_board2[0][i] === 1) {
        for (let j = 0; j < h; j++) {
          _board2[j][i] = flipNum(_board2[j][i]);
        }
        cntCase2 += 1;
      }
      // console.log(_board);
      // console.log();
    }

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (_board1[i][j] === 1) {
                cntCase1 = Infinity;
            }
            
            if (_board2[i][j] === 1) {
                cntCase2 = Infinity;
            } 
        }
    }

      if (cntCase1 === Infinity && cntCase2 === Infinity) {
          return -1
      }
      
    return Math.min(cntCase1, cntCase2);
  };

  return countMinimum();

  // return checkCnt;
};

// function solution(beginning, target) {
//   let answer = 0;

//   let checkCnt = 0;
//   const makeCheckBoard = () => {
//     const board = new Array(beginning.length)
//       .fill(0)
//       .map(() => new Array(beginning[0].length).fill(0));

//     for (let i = 0; i < beginning.length; i++) {
//       for (let j = 0; j < beginning[0].length; j++) {
//         if (beginning[i][j] === target[i][j]) {
//           board[i][j] = 0;
//         } else {
//           board[i][j] = 1;
//         }
//       }
//     }

//     const h = board.length;
//     const w = board[0].length;

//     // 가로가 길 경우 -> 세로를 먼저 탐색
//     if (w > h) {
//       for (let i = 0; i < h; i++) {
//         if (board[i][0] === 1) {
//           checkCnt += 1;
//         }
//       }

//       if (h > 1) {
//         for (let i = 1; i < w; i++) {
//           if (board[0][0] === 0 && board[0][i] === 1) {
//             checkCnt += 1;
//           } else if (board[0][0] === 1 && board[0][i] === 0) {
//             checkCnt += 1;
//           }
//         }
//       }
//     } else {
//       for (let i = 0; i < h; i++) {
//         if (board[0][i] === 1) {
//           checkCnt += 1;
//         }
//       }

//       if (w > 1) {
//         for (let i = 1; i < w; i++) {
//           if (board[0][0] === 0 && board[i][0] === 1) {
//             checkCnt += 1;
//           } else if (board[0][0] === 1 && board[i][0] === 0) {
//             checkCnt += 1;
//           }
//         }
//       }
//     }

//     // for (let i = 0; i < beginning.length; i++) {
//     //   for (let j = 0; j < beginning[0].length; j++) {
//     //     if (beginning[i][j] === target[i][j]) {
//     //       if (i > 0 && j === 0 && board[0][0] === 1) {
//     //         checkCnt += 1;
//     //       }
//     //       board[i][j] = 0;
//     //     } else {
//     //       if (i === 0) {
//     //         checkCnt += 1;
//     //       } else {
//     //         if (j === 0 && board[0][0] === 0) {
//     //           checkCnt += 1;
//     //         }
//     //       }
//     //       board[i][j] = 1;
//     //     }
//     //   }
//     // }

//     return board;
//   };

//   const board = makeCheckBoard();
//   const template = board[0].slice().join("");
//   const revTemplate = [...template]
//     .map((elm) => {
//       if (elm === "0") {
//         return 1;
//       }
//       return 0;
//     })
//     .join("");

//   const isSameRow = (rowArr) => {
//     const stringRowArr = rowArr.join("");
//     let stand = "";

//     if (template[0] !== stringRowArr[0]) {
//       stand = revTemplate;
//     } else {
//       stand = template;
//     }

//     for (let i = 1; i < stand.length; i++) {
//       if (stand[i] !== stringRowArr[i]) {
//         return false;
//       }
//     }

//     return true;
//   };

//   const isPossibleToMake = () => {
//     for (let i = 0; i < board.length; i++) {
//       if (!isSameRow(board[i])) {
//         return false;
//       }
//     }
//     return true;
//   };

//   console.log(board);

//   if (!isPossibleToMake()) {
//     return -1;
//   } else {
//     return checkCnt;
//   }
// }