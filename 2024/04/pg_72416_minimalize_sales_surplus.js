const createGraph = (sales, links) => {
  const graph = {};

  // 각 노드의 초기 정보 넣기
  sales.forEach((value, idx) => {
    graph[idx + 1] = {
      value,
      minValue: 0,
      myStaffWillGo: 0,
      IWillGo: value,
      isPicked: false,
      members: [],
    };
  });

  // 간선 정보로 그래프 만들기
  links.forEach(([leader, member]) => {
    graph[leader].members.push(member);
  });

  return graph;
};

function makePathOrder(graph) {
  // 무조건 1에서 시작
  let stack = [1];
  const pathOrder = [];

  while (stack.length) {
    const id = stack.pop();
    const node = graph[id];

    stack = [...stack, ...node.members];

    pathOrder.push(id);
  }

  return pathOrder;
}

function updatePickLeaderCase(node, memberNodes) {
  node.IWillGo =
    node.value +
    memberNodes.reduce((accum, member) => accum + member.minValue, 0);
}

function memberPickedCase(node, memberNodes) {
  let isSomeonePicked = false;
  let currentMinSum = 0;

  memberNodes.forEach((member) => {
    if (member.IWillGo === member.minValue) {
      isSomeonePicked = true;
    }

    currentMinSum += member.minValue;
  });

  if (isSomeonePicked) {
    node.myStaffWillGo = currentMinSum;
  }

  return isSomeonePicked;
}

function updatePickMemberAsALeader(node, memberNodes) {
  const memeberSize = memberNodes.length;
  let currentMinValue = Infinity;

  for (let i = 0; i < memeberSize; i += 1) {
    let currentSum = memberNodes[i].IWillGo;

    for (let j = 0; j < memeberSize; j += 1) {
      if (i !== j) {
        currentSum += memberNodes[j].minValue;
      }
    }

    currentMinValue = Math.min(currentMinValue, currentSum);
  }

  node.myStaffWillGo = currentMinValue;
}

function updatePickMemeberCase(node, memberNodes) {
  // 1. 팀원 중에 선택된 케이스가 있어야 한다.
  if (!memberPickedCase(node, memberNodes)) {
    // 2. 팀원 중에 선택된 케이스가 없다면, 하나의 팀원을 선택해 해당 팀에서 최소 한 명이 선택되도록 한다.
    updatePickMemberAsALeader(node, memberNodes);
  }
}

function updateNodeInfo(graph, pathOrder) {
  while (pathOrder.length) {
    const nodeId = pathOrder.pop();
    const node = graph[nodeId];

    if (node.members.length) {
      const memberNodes = node.members.map((member) => graph[member]);

      // 1. 팀장을 선택
      updatePickLeaderCase(node, memberNodes);

      // 2. 팀원을 선택
      updatePickMemeberCase(node, memberNodes);

      // 3. 각 케이스를 비교해서 최솟값 설정
      node.minValue = Math.min(node.IWillGo, node.myStaffWillGo);
    }
  }
}

function solution(sales, links) {
  // 트리 정보를 담은 그래프
  const graph = createGraph(sales, links);

  // 최하단 리프부터 탐색하기 위한 Arr = pathOrder
  const pathOrder = makePathOrder(graph);

  // 그래프 탐색 순서를 기반으로 각 노드의 정보 업데이트
  updateNodeInfo(graph, pathOrder);

  return Math.min(graph[1].IWillGo, graph[1].myStaffWillGo);
}

/*
 * 하단 코드를 제외하고 제출하시기 바랍니다.
 */

const verdict = (caseNo, result, yourAnswer) => {
  console.log(`테스트 케이스 #${String(caseNo + 1).padStart(2, "0")}번`);
  if (result === yourAnswer) {
    console.log("정답입니다!");
  } else {
    console.log(
      `실행한 결괏값 ${yourAnswer}이(가) 기댓값 ${result}와(과) 다릅니다.`
    );
  }
};

const testCases = [
  [
    [14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
    [
      [10, 8],
      [1, 9],
      [9, 7],
      [5, 4],
      [1, 5],
      [5, 10],
      [10, 6],
      [1, 3],
      [10, 2],
    ],
    44,
  ],
  [
    [5, 6, 5, 3, 4],
    [
      [2, 3],
      [1, 4],
      [2, 5],
      [1, 2],
    ],
    6,
  ],
  [
    [5, 6, 5, 1, 4],
    [
      [2, 3],
      [1, 4],
      [2, 5],
      [1, 2],
    ],
    5,
  ],
  [
    [10, 10, 1, 1],
    [
      [3, 2],
      [4, 3],
      [1, 4],
    ],
    2,
  ],
];

testCases.forEach((testCase, caseNo) => {
  const sales = testCase[0];
  const links = testCase[1];
  const result = testCase[2];

  if (caseNo > 0) {
    console.log("");
  }

  const yourResult = solution(sales, links);
  verdict(caseNo, result, yourResult);
});
