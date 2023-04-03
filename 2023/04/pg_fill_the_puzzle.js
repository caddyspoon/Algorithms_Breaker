const solution = (game_board, table) => {
  const l = game_board.length;

  const blanks = [];
  const blocks = [];

  const dx = [0, 1, 0, -1];
  const dy = [1, 0, -1, 0];
  const visited = new Array(l).fill().map((_) => new Array(l).fill(false));
  const blocksVisited = new Array(l)
    .fill()
    .map((_) => new Array(l).fill(false));
  const makingMap = new Array(l).fill().map((_) => new Array(l).fill(0));
  const blockMap = new Array(l).fill().map((_) => new Array(l).fill(0));
  let shapeMarker = 1;
  let blockMarker = 1;

  const isTarget = (i, j, isBlock = false) => {
    if (i < 0 || j < 0 || i >= l || j >= l) {
      return false;
    }

    let boardValue;
    let thisVisited;

    if (isBlock) {
      boardValue = table[i][j];
      thisVisited = blocksVisited[i][j];
    } else {
      boardValue = !game_board[i][j];
      thisVisited = visited[i][j];
    }

    if (boardValue && !thisVisited) {
      return true;
    }
    return false;
  };

  const findInfo = (i, j) => {
    let minX = l - 1;
    let maxX = 0;
    let minY = l - 1;
    let maxY = 0;

    const stack = [[i, j]];
    while (stack.length) {
      const [p, q] = stack.pop();

      if (p > maxX) {
        maxX = p;
      }
      if (p < minX) {
        minX = p;
      }
      if (q > maxY) {
        maxY = q;
      }
      if (q < minY) {
        minY = q;
      }

      for (let x = 0; x < 4; x++) {
        const nx = p + dx[x];
        const ny = q + dy[x];
        if (isTarget(nx, ny)) {
          stack.push([nx, ny]);
          makingMap[nx][ny] = shapeMarker;
          visited[nx][ny] = true;
        }
      }
    }

    const resultShape = [];
    for (let i = minX; i <= maxX; i++) {
      const temp = [];
      for (let j = minY; j <= maxY; j++) {
        if (makingMap[i][j] === shapeMarker) {
          temp.push(1);
        } else {
          temp.push(0);
        }
      }
      resultShape.push(temp);
    }

    blanks.push(resultShape);
  };

  const findBlocks = (i, j) => {
    let minX = l - 1;
    let maxX = 0;
    let minY = l - 1;
    let maxY = 0;

    const stack = [[i, j]];
    while (stack.length) {
      const [p, q] = stack.pop();

      if (p > maxX) {
        maxX = p;
      }
      if (p < minX) {
        minX = p;
      }
      if (q > maxY) {
        maxY = q;
      }
      if (q < minY) {
        minY = q;
      }

      for (let x = 0; x < 4; x++) {
        const nx = p + dx[x];
        const ny = q + dy[x];
        if (isTarget(nx, ny, true)) {
          stack.push([nx, ny]);
          blockMap[nx][ny] = blockMarker;
          blocksVisited[nx][ny] = true;
        }
      }
    }

    const resultShape = [];
    for (let i = minX; i <= maxX; i++) {
      const temp = [];
      for (let j = minY; j <= maxY; j++) {
        if (blockMap[i][j] === blockMarker) {
          temp.push(1);
        } else {
          temp.push(0);
        }
      }
      resultShape.push(temp);
    }

    blocks.push(resultShape);
  };

  const rotateBlock = (arr) => {
    const l = arr.length;
    const m = arr[0].length;

    const tempArr = new Array(m).fill().map((_) => new Array(l).fill(0));
    for (let i = 0; i < l; i++) {
      for (let j = 0; j < m; j++) {
        if (arr[i][j]) {
          tempArr[j][l - 1 - i] = arr[i][j];
        }
      }
    }

    return tempArr;
  };

  const makeString = (arr) => {
    return arr
      .map((elm) => {
        return elm.join("");
      })
      .join("-");
  };

  for (let i = 0; i < game_board.length; i++) {
    for (let j = 0; j < game_board[0].length; j++) {
      if (isTarget(i, j)) {
        makingMap[i][j] = shapeMarker;
        findInfo(i, j);
        shapeMarker += 1;
      }
    }
  }

  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table[0].length; j++) {
      if (isTarget(i, j, true)) {
        blockMap[i][j] = blockMarker;
        findBlocks(i, j);
        blockMarker += 1;
      }
    }
  }

  const stringBlocks = [];
  blocks.forEach((arr) => {
    const temp = [];
    for (let i = 0; i < 4; i++) {
      temp.push(makeString(arr));
      arr = rotateBlock(arr);
    }
    stringBlocks.push(temp);
  });

  let answer = 0;

  blanks.forEach((blank) => {
    const targetStr = makeString(blank);

    for (let i = 0; i < stringBlocks.length; i++) {
      if (stringBlocks[i].includes(targetStr)) {
        // console.log(targetStr, stringBlocks[i]);
        stringBlocks.splice(i, 1);
        [...targetStr].forEach((chr) => {
          if (chr === "1") {
            answer += 1;
          }
        });
        break;
      }
    }
  });

  return answer;
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

console.log(
  solution(game_board, table)
  // ,solution(game_board, table) === result
);
