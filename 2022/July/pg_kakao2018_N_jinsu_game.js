
const solution = (n, t, m, p) => {
  // n 진법 / t 미리 구할 숫자의 갯수 / m 게임에 참가하는 인원 / p 튜브의 순서
  let answer = '';

  let decimalStr = '';

  for (let i = 0; i <= m*t; i++) {
    decimalStr +=  i.toString(n).toString().toUpperCase();
  }

  let cur = p - 1;
  while (answer.length < t) {
    answer += decimalStr[cur];
    cur += m;
  }

  return answer;
};

// const n = 2;
// const t =	4;
// const m = 2;
// const p =	1;
// const result = "0111";

// const n = 16;
// const t = 16;
// const m = 2;
// const p = 1;
// const result = "02468ACE11111111";

const n = 16;
const t = 16;
const m = 2;
const p = 2;
const result = "13579BDF01234567";

console.log(solution(n, t, m, p) === result);