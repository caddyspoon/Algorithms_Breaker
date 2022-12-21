const solution = (clockHands) => {
  // 길이를 저장해줍니다.
  const l = clockHands.length;

  // 앞으로의 함수들은 핀을 돌리기 위한 작은 함수 조각들입니다.
  // 1. 인덱스가 범위 내 있는지
  const isInRange = (x, y) => {
    if (0 <= x && x < l && 0 <= y && y < l) return true;
    return false;
  };

  // 2. 그 핀을 돌립니다.
  const turnPin = (x, y, arr) => {
    arr[x][y] = arr[x][y] === 3 ? 0 : arr[x][y] + 1;
  };

  const dx = [0, 0, 1, 0, -1];
  const dy = [0, 1, 0, -1, 0];

  // 3. 선택한 좌표를 전해주면, 해당 핀을 중앙으로 4방향의 위치를 파악해 핀을 90도 돌립니다.
  const selectLoc = (x, y, arr) => {
    for (let i = 0; i < 5; i += 1) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (isInRange(nx, ny)) {
        turnPin(nx, ny, arr);
      }
    }
  };

  let answer = Infinity;

  // 실제로 시행을 해봅니다.
  const makeZero = (loc = 0, cnt = 0, myMap = clockHands) => {
    // 시행 종료
    if (loc === l) return;

    /**
     * 위의 줄에 따라 아랫줄의 시행이 정해집니다.
     * 따라서 맨 위의 줄이 해당 시행의 전체 경우의 수를 정합니다.
     * 맨 위의 줄은 모두 맞춰질 필요가 없으며 해당 줄의 시행이 어떻게 되는지 모든 경우의 수를 확인할 필요가 있습니다.
     * 맨 위의 줄이 어떤 상태이냐에 따라 전체 경우의 수가 정해지지만, 맨 윗줄의 어떤 상태에 따라 정해지는지 알 수 없기 때문이죠.
     * 따라서 맨 윗줄의 모든 경우의 수를 볼 필요가 있습니다.
     * 또한 핀을 돌리는 순서는 아무런 상관 없고, 돌리는 횟수만이 유효한 영향을 줍니다.
     * 따라서 4의 (맨 위의 줄의 길이) 제곱만큼의 시간 복잡도가 필요합니다.
     * 길이는 8이 최대이므로 최대 4^8번의 시행이 필요합니다.
     */

    // 순서는 상관없이 어떤 줄을 골라 돌려줄지만 정하면 됩니다.
    // 따라서 조합으로 돌릴 위치를 정하고, 해당 위치를 0~3번 돌려주는 모든 시행을 합니다.
    for (let i = loc; i < l; i += 1) {
      // 기준이 되는 현재 어레이
      const _clockHands = myMap.map((arr) => [...arr]);

      // 현재 i의 위치를 0번에서 3번까지 돌리는 모든 경우의 수를 시뮬레이션합니다.
      for (let j = 0; j < 4; j += 1) {
        // 실제 시행을 해볼 어레이
        const tempMap = _clockHands.map((elm) => [...elm]);

        // 현재 시행의 핀 회전 수
        let tempCnt = cnt + j;

        // 최적화를 위한 flag
        let flag = false;

        // 아래줄부터 0으로 만들기
        // 지금보다 위의 위치는 반드시 0으로 만들어져야 합니다.
        for (let x = 1; x < l; x += 1) {
          for (let y = 0; y < l; y += 1) {
            // 현재 위치를 기준으로 상단의 값이 0이 아니라면
            if (tempMap[x - 1][y]) {
              // 0이 될 때까지 회전을 해줍니다.
              while (tempMap[x - 1][y] !== 0) {
                selectLoc(x, y, tempMap);
                tempCnt += 1;
              }
            }

            // 최적화 관련 코드, 아래 코드가 없어도 정상적으로 작동합니다.
            // 현재 모든 시행을 마쳤는데 바로 위 줄에 0이 아닌 값이 있다면 해당 시행은 완료되지 않은 시행입니다.
            if (y > 1) {
              if (tempMap[x - 1][y - 1]) {
                flag = true;
                break;
              }
            }
          }
        }

        for (let x = 0; x < l; x += 1) {
          if (flag) return;
          for (let y = 0; y < l; y += 1) {
            if (tempMap[x][y]) {
              flag = true;
              break;
            }
          }
        }

        // Case 1. 전부 0으로 만들어진 상태
        if (!flag) {
          if (tempCnt < answer) {
            answer = tempCnt;
          }
          // Case 2. 그렇지 않은 상태
        } else {
          makeZero(i + 1, cnt + j, _clockHands);
          selectLoc(0, i, _clockHands);
        }
      }
    }
  };

  makeZero();

  return answer;
};

const clockHands = [
  [0, 3, 3, 0],
  [3, 2, 2, 3],
  [0, 3, 2, 0],
  [0, 3, 3, 3],
];

const result = 3;

// const clockHands = [
//   [1, 1, 1, 0],
//   [0, 1, 0, 0],
//   [0, 0, 3, 0],
//   [0, 3, 3, 3],
// ];

// const result = 4;

console.log(solution(clockHands) === result);

// NOTE: 아래 코드가 더 빠름
const solution2 = (clockHands) => {
  const l = clockHands.length;

  const isInRange = (x, y) => {
    if (0 <= x && x < l && 0 <= y && y < l) return true;
    return false;
  };

  const turnPin = (x, y, arr) => {
    arr[x][y] = arr[x][y] === 3 ? 0 : arr[x][y] + 1;
  };

  const dx = [0, 0, 1, 0, -1];
  const dy = [0, 1, 0, -1, 0];

  const selectLoc = (x, y, arr) => {
    for (let i = 0; i < 5; i += 1) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (isInRange(nx, ny)) {
        turnPin(nx, ny, arr);
      }
    }
  };

  let answer = Infinity;

  const makeZero = (loc = 0, cnt = 0, myMap = clockHands) => {
    // 시행 종료
    if (loc === l) return;

    for (let i = loc; i < l; i += 1) {
      // 기준이 되는 현재 어레이
      const _clockHands = myMap.map((arr) => [...arr]);
      for (let j = 0; j < 4; j += 1) {
        // 실제 시행을 해볼 어레이
        const tempMap = _clockHands.map((elm) => [...elm]);

        let tempCnt = cnt + j;

        // 아래줄부터 0으로 만들기
        for (let x = 1; x < l; x += 1) {
          for (let y = 0; y < l; y += 1) {
            if (tempMap[x - 1][y]) {
              while (tempMap[x - 1][y] !== 0) {
                selectLoc(x, y, tempMap);
                tempCnt += 1;
              }
            }
          }
        }

        let flag = false;
        for (let x = 0; x < l; x += 1) {
          if (flag) return;
          for (let y = 0; y < l; y += 1) {
            if (tempMap[x][y]) {
              flag = true;
              break;
            }
          }
        }

        if (!flag) {
          if (tempCnt < answer) {
            answer = tempCnt;
          }
        } else {
          makeZero(i + 1, cnt + j, _clockHands);
          selectLoc(0, i, _clockHands);
        }
      }
    }
  };

  makeZero();

  return answer;
};
