const solution = (n, info) => {
  let answer = [-1];

  const initApeachPoint = info.reduce((totalPoint, point, idx) => {
    return point > 0 ? totalPoint + (10 - idx) : totalPoint;
  }, 0)


  const initRyanInfo = new Array(11).fill(0);
  let answers = [];

  let pointGap = 0;

  const dfs = (ryanInfo = initRyanInfo, ryanPoint = 0, apeachPoint = initApeachPoint, currentPoint = 10, leftArrow = n) => {
    if (leftArrow === 0 || currentPoint === 0) {
      resultArr = [...ryanInfo];

      if (leftArrow > 0) {
        resultArr[10] = leftArrow;
      }
      
      if (ryanPoint > apeachPoint) {
        if (ryanPoint - apeachPoint > pointGap) {
          pointGap = ryanPoint - apeachPoint;
          answers = [resultArr];
  
        } else if (ryanPoint - apeachPoint === pointGap) {
          answers.push(resultArr);
        }
      }

      return
    }

    for (let pointNo = currentPoint; pointNo > -1; pointNo--) {
      // 현재 노리고 있는 점수가 0일 경우 해당 재귀를 종료
      if (pointNo === 0) {
        dfs(ryanInfo, ryanPoint, apeachPoint, 0, leftArrow);
        break;
      }


      // 그렇지 않을 경우 어피치 점수와 비교
      const idx = 10 - pointNo;
      const currentApeachArrows = info[idx];

      // 현재 화살 갯수로 이길 수 없다면 현재 시행을 종료하고 다음으로 진행한다.
      if (leftArrow - (currentApeachArrows + 1) < 0) {
        continue;
      }

      // 득점할 수 있다면 득점한다.
      leftArrow -= currentApeachArrows + 1;
      ryanInfo[idx] = currentApeachArrows + 1;
      if (currentApeachArrows > 0) {
        apeachPoint -= pointNo;
      }
      ryanPoint += pointNo;
      dfs(ryanInfo, ryanPoint, apeachPoint, pointNo - 1, leftArrow);

      // 원상복귀
      leftArrow += currentApeachArrows + 1;
      ryanInfo[idx] = 0;
      if (currentApeachArrows > 0) {
        apeachPoint += pointNo;
      }
      ryanPoint -= pointNo;
    }
  }

  dfs();
  
  if (answers.length) {
    answer = [...answers[0]];
    if (answers.length > 1) {
      answers
        .filter((elm, idx) => {
          if (idx === 0) {
            return false;
          }
          return true;
        })
        .map((answerJunior) => {
        for (let i in answerJunior) {
          const idx = 10 - i;
          if (answer[idx] < answerJunior[idx]) {
            answer = [...answerJunior];
            return
          } else if (answer[idx] > answerJunior[idx]) {
            break;
          }
        }
      })
    }
  }

  return answer;
};

const ns = [5, 1, 9, 10];
const infos = [
  [2,1,1,1,0,0,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,2,0,1,1,1,1,1,1],
  [0,0,0,0,0,0,0,0,3,4,3]
];

const results = [
  [0,2,2,0,1,0,0,0,0,0,0],
  [-1],
  [1,1,2,0,1,2,2,0,0,0,0],
  [1,1,1,1,1,1,1,1,0,0,2]
];

for (i in [0, 1, 2, 3]) {
  const n = ns[i];
  const info = infos[i];
  const result = results[i];
  console.log(solution(n, info).join(",") === result.join(","));
};