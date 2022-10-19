const solution = (beginning, target) => {
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

  // 그냥 개수만 세기
  const countMinimum = () => {
    const w = board[0].length;
    const h = board.length;

    let cntCase1 = 0;
    let cntCase2 = 0;
    let cntCase3 = 0;
    let cntCase4 = 0;

    // case 1.
    // 행(세로축)부터 뒤집기
    for (let i = 0; i < w; i++) {
      if (board[0][i] === 1) {
        cntCase1 += 1;
      }

      if (board[h - 1][i] === 1) {
        cntCase3 += 1;
      }

      // case 2.
      if (i !== 0) {
        if (board[0][0] === 1) {
          if (board[0][i] === 0) {
            cntCase2 += 1;
          }
        } else {
          if (board[0][i] === 1) {
            cntCase2 += 1;
          }
        }
      }

      // case 4.
      if (i !== w - 1) {
        if (board[0][w - 1] === 1) {
          if (board[0][i] === 0) {
            cntCase4 += 1;
          }
        } else {
          if (board[0][i] === 1) {
            cntCase4 += 1;
          }
        }
      }
    }

    for (let i = 0; i < h; i++) {
      // case 1.
      if (i !== 0) {
        if (board[0][0] === 1) {
          if (board[i][0] === 0) {
            cntCase1 += 1;
          }
        } else {
          if (board[i][0] === 1) {
            cntCase1 += 1;
          }
        }
      }

      // case 3.
      if (i !== h - 1) {
        if (board[h - 1][0] === 1) {
          if (board[i][0] === 0) {
            cntCase3 += 1;
          }
        } else {
          if (board[i][0] === 1) {
            cntCase3 += 1;
          }
        }
      }

      if (board[i][0] === 1) {
        cntCase2 += 1;
      }

      if (board[i][w - 1] === 1) {
        cntCase4 += 1;
      }
    }

    // 난 가로축이야
    // for (let i = 0; i < h; i++) {
    //   if (board[i][0] === 1) {
    //     cntCase2 += 1;
    //   }

    //   if (board[i][w - 1] === 1) {
    //     cntCase4 += 1;
    //   }
    // }

    // for (let i = 0; i < w; i++) {
    //   // case 2.
    //   if (i !== 0) {
    //     if (board[0][0] === 1) {
    //       if (board[0][i] === 0) {
    //         cntCase2 += 1;
    //       }
    //     } else {
    //       if (board[0][i] === 1) {
    //         cntCase2 += 1;
    //       }
    //     }
    //   }

    //   // case 4.
    //   if (i !== w - 1) {
    //     if (board[0][w - 1] === 1) {
    //       if (board[0][i] === 0) {
    //         cntCase4 += 1;
    //       }
    //     } else {
    //       if (board[0][i] === 1) {
    //         cntCase4 += 1;
    //       }
    //     }
    //   }
    // }

    return Math.min(cntCase1, cntCase2, cntCase3, cntCase4);
  };

  // 시뮬레이션
  // const simCountMinimum = () => {
  //   const _board1 = makeCheckBoard();
  //   const _board2 = makeCheckBoard();
  //   const _board3 = makeCheckBoard();
  //   const _board4 = makeCheckBoard();

  //   const w = _board1[0].length;
  //   const h = _board1.length;

  //   let cntCase1 = 0;
  //   let cntCase2 = 0;
  //   let cntCase3 = 0;
  //   let cntCase4 = 0;

  //   // case 1.
  //   // 행(세로축)부터 뒤집기
  //   for (let i = 0; i < w; i++) {
  //     if (_board1[0][i] === 1) {
  //       for (let j = 0; j < h; j++) {
  //         _board1[j][i] = flipNum(_board1[j][i]);
  //       }
  //       cntCase1 += 1;
  //     }
  //   }

  //   for (let i = 0; i < h; i++) {
  //     if (_board1[i][0] === 1) {
  //       for (let j = 0; j < w; j++) {
  //         _board1[i][j] = flipNum(_board1[i][j]);
  //       }
  //       cntCase1 += 1;
  //     }
  //   }

  //   // case 3.
  //   for (let i = 0; i < w; i++) {
  //     if (_board3[h - 1][i] === 1) {
  //       for (let j = 0; j < h; j++) {
  //         _board3[j][i] = flipNum(_board3[j][i]);
  //       }
  //       cntCase3 += 1;
  //     }
  //   }

  //   for (let i = 0; i < h; i++) {
  //     if (_board3[i][0] === 1) {
  //       for (let j = 0; j < w; j++) {
  //         _board3[i][j] = flipNum(_board3[i][j]);
  //       }
  //       cntCase3 += 1;
  //     }
  //   }

  //   // case 2.
  //   // 세로축으로 먼저!
  //   for (let i = 0; i < h; i++) {
  //     if (_board2[i][0] === 1) {
  //       for (let j = 0; j < w; j++) {
  //         _board2[i][j] = flipNum(_board2[i][j]);
  //       }
  //       cntCase2 += 1;
  //     }
  //   }

  //   for (let i = 0; i < w; i++) {
  //     if (_board2[0][i] === 1) {
  //       for (let j = 0; j < h; j++) {
  //         _board2[j][i] = flipNum(_board2[j][i]);
  //       }
  //       cntCase2 += 1;
  //     }
  //   }

  //   // case 4.
  //   for (let i = 0; i < h; i++) {
  //     if (_board4[i][w - 1] === 1) {
  //       for (let j = 0; j < w; j++) {
  //         _board4[i][j] = flipNum(_board4[i][j]);
  //       }
  //       cntCase4 += 1;
  //     }
  //   }

  //   for (let i = 0; i < w; i++) {
  //     if (_board4[0][i] === 1) {
  //       for (let j = 0; j < h; j++) {
  //         _board4[j][i] = flipNum(_board4[j][i]);
  //       }
  //       cntCase4 += 1;
  //     }
  //   }

  //   return Math.min(cntCase1, cntCase2, cntCase3, cntCase4);
  // };

  return countMinimum();
};
