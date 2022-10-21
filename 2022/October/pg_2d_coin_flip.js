const solution = (beginning, target) => {
  let cntCase = 0;

  let standRow = "";

  for (let i = 0; i < beginning.length; i++) {
    let crntRow = "";
    for (let j = 0; j < beginning[0].length; j++) {
      if (beginning[i][j] !== target[i][j]) {
        crntRow += "1";

        // 세로 축 기준으로 합산
        if (i === 0) {
          cntCase += 1;
        } else {
          // 가로축 기준으로 합산
          if (standRow[0] === "0" && j === 0) {
            cntCase += 1;
          }
        }
      } else {
        crntRow += "0";
        if (i > 0 && standRow[0] === "1" && j === 0) {
          cntCase += 1;
        }
      }
    }

    // 첫째 줄의 경우 기준 줄로 만들어준다.
    if (i === 0) {
      standRow = crntRow;
    } else {
      // 같지 않을 때
      if (standRow !== crntRow) {
        // if (standRow[0] !== crntRow[0]) {
        // 둘을 합쳐 모두 1(바꿔야 되는 자리)로 만들 수 있는 경우 -1을 반환한다.
        if (!(+standRow + +crntRow === Number("1".repeat(standRow.length)))) {
          return -1;
        }
      }
    }
  }

  return Math.min(cntCase, target.length + target[0].length - cntCase);
};

console.log(
  solution(
    [
      [0, 0],
      [0, 0],
    ],
    [
      [1, 1],
      [1, 0],
    ]
  )
);
