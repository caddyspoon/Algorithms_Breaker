const solution = (n, costs) => {
  const findSet = (x) => {
    if (p[x] === x) {
      return x;
    } else {
      p[x] = findSet(p[x]);
      return p[x];
    }
  };

  const union = (x, y) => {
    const px = findSet(x);
    const py = findSet(y);

    if (rank[px] > rank[py]) {
      p[py] = px;
    } else {
      p[px] = py;
      if (rank[px] === rank[py]) {
        rank[py] += 1;
      }
    }
  };

  // 정점의 개수, 관례적으로 사용하는 V로 재정의해준다.
  const V = n;
  //
  const E = costs.length;

  // 간선의 가중치를 기준으로 정렬한다.
  costs.sort((a, b) => {
    return a[2] > b[2] ? 1 : -1;
  });

  // 배열 상태를 확인
  console.log(costs);

  const p = new Array(E).fill(0).map((elm, idx) => idx);
  const rank = new Array(E).fill(0);

  let cnt = 0;
  let result = 0;

  for (let i = 0; i < E; i += 1) {
    const [s, e, c] = costs[i];

    if (findSet(s) === findSet(e)) {
      continue;
    }

    result += c;
    union(s, e);

    cnt += 1;
    if (cnt === V - 1) {
      break;
    }
  }

  return result;
};

// Test Cases
const n = 4;
const costs = [
  [0, 1, 1],
  [0, 2, 2],
  [1, 2, 5],
  [1, 3, 1],
  [2, 3, 8],
];
const result = 4;

console.log(solution(n, costs) === result);
