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

  // 그냥 개수만 세기
  const countMinimum = () => {
    const w = board[0].length;
    const h = board.length;

    let cntCase = 0;

    // 행(세로축)부터 뒤집기
    for (let i = 0; i < w; i++) {
      if (board[0][i] === 1) {
        cntCase += 1;
      }
    }

    for (let i = 0; i < h; i++) {
      if (i !== 0) {
        if (board[0][0] === 1) {
          if (board[i][0] === 0) {
            cntCase += 1;
          }
        } else {
          if (board[i][0] === 1) {
            cntCase += 1;
          }
        }
      }
    }
    return Math.min(cntCase, w + h - cntCase);
  };

  return countMinimum();
};
