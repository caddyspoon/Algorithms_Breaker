function solution(info, edges) {
  let answer = 0;

  const tree = new Array(info.length).fill(new Array());
  let visited = new Array(info.length).fill(false);

  edges.forEach(node => {
    tree[node[0]] = [ ...tree[node[0]], node[1] ];
    tree[node[1]] = [ ...tree[node[1]], node[0] ];
  })

  const currInfo = {
    loc: 0,
    sheep: 0,
    wolf: 0,
  }

  visited[0] = true;
  const stack = [0];

  while (stack.length) {
    currNode = stack.pop();

    currInfo.loc = currNode;
    if (info[currNode] === 0) {
      currInfo.sheep += 1;
      info[currNode] = false;
      visited = new Array(info.length).fill(false);
    } else if (info[currNode] === 1) {
      currInfo.wolf += 1;
      info[currNode] = false;
    }

    visited[currNode] = true;
    
    console.log("currInfo: ", currInfo);
    // console.log(tree);
    console.log("info: ", info);
    console.log("visited: ", visited);
    console.log();
    console.log();
    console.log();

    // 자식들을 꺼냄
    tree[currNode].forEach(elm => {
      // 방문하지 않은 곳이며
      if (!visited[elm]) {
        const animalInfo = info[elm];

        // 해당 칸에 아직 동물이 있을 때
        if (typeof animalInfo === "number") {
          
          // 양일 때
          if (animalInfo === 0) {
            stack.push(elm);
            visited[elm] = true;
          // 늑대일 때
          } else if (animalInfo === 1) {
            // 갈 수 있으면 간다
            if (currInfo.sheep <= currInfo.wolf + 1) {
              return;
            } else {
              stack.push(elm);
              visited[elm] = true;
            }
          }

          // 이미 데려온 칸일 때
        } else {
          stack.push(elm);
          visited[elm] = true;
        }
      }
    })
  }

  answer = currInfo.sheep;
  console.log(answer)
  return answer;
}

// const info = [0,0,1,1,1,0,1,0,1,0,1,1];
// const edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]];
// const result = 5;

const info = [0,1,0,1,1,0,1,0,0,1,0];
const edges =	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]];
const result = 5;



console.log(solution(info, edges) === result);