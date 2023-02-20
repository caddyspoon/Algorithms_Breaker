const solution = (n, times) => {
  // 이분탐색으로 해결하자!

  // 심사 시간은 1분 이상이므로 왼쪽 값은 1
  let left = 1;
  // 오른쪽 값은 현재 times 중 가장 큰 값에 n을 곱해준 값이 된다.
  let right = Math.max(...times) * n;

  let answer = null;

  while (left <= right) {
    // 중간 시간
    const middle = parseInt((left + right) / 2);

    // 중간 시간을 기준으로 처리할 수 있는 민원인 수
    let currAvailTasks = times.reduce((prev, taskTime) => {
      // 현재 시간 기준으로 각 심사대가 처리할 수 있는 민원 수
      prev += parseInt(middle / taskTime);
      return prev;
    }, 0);

    // 중과부적일 경우!
    if (currAvailTasks < n) {
      left = middle + 1;

      // 할 수 있는 경우!
    } else {
      // 답이 될 수 있는 후보인 middle을 answer 값으로 업데이트 해주자
      answer = middle;
      right = middle - 1;
    }
  }

  return answer;
};

const n = 6;
const times = [7, 10];
const result = 28;
console.log(solution(n, times) === result);
