function solution(info, edges) {
  let answer = 0;

  const tree = new Array(info.length).fill(new Array());
  let intVisited = new Array(info.length).fill(false);

  edges.forEach(node => {
    tree[node[0]] = [ ...tree[node[0]], node[1] ];
    tree[node[1]] = [ ...tree[node[1]], node[0] ];
  });

  const initInfo = [ ...info ];

  const recur = (cur = 0, sheep = 0, wolf = 0, cnt = 1, info = initInfo, visited = intVisited) => {
    if (cnt > info.length) {
      if (sheep > answer) {
        answer = sheep;
      }
      return;
    }

    const tempInfo = [ ...info ];
    let tempVisited = [ ...visited ];

    if (typeof tempInfo[cur] === 'number') {
      if (tempInfo[cur] === 0) {
        sheep += 1;
      } else if (tempInfo[cur] === 1) {
        wolf += 1;
        if (wolf === sheep) {
          if (sheep > answer) {
            answer = sheep;
          }
          return;
        }
      }
      cnt += 1;
      tempInfo[cur] = false;
      tempVisited = new Array(info.length).fill(false); 
    }

    tree[cur].forEach(elm => {
      if (!tempVisited[elm]) {
        tempVisited[elm] = true;
        recur(elm, sheep, wolf, cnt, tempInfo, tempVisited);

        tempVisited[elm] = false;
      }
    });
  };

  intVisited[0] = true;
  recur();

  return answer;
}

// const info = [0,0,1,1,1,0,1,0,1,0,1,1];
// const edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]];
// const result = 5;

const info = [0,1,0,1,1,0,1,0,0,1,0];
const edges =	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]];
const result = 5;



console.log(solution(info, edges) === result);