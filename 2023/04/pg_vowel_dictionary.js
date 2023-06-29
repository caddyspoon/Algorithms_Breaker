const solution = (n, wires) => {
  l = wires.length;

  wires.sort((a, b) => {
    if (a[0] < b[0]) {
      return -1;
    }
  });

  const tree = new Array(l + 2).fill().map((_) => new Array());
  const pNodeDict = new Map();
  wires.forEach((nodes) => {
    const crntValue = pNodeDict.get(nodes[0]);
    if (!crntValue) {
      pNodeDict.set(nodes[0], 1);
    } else {
      pNodeDict.set(nodes[0], crntValue + 1);
    }
    
  });

  pNodeDict.keys.forEach((elm) => console.log(elm));

  // wires.forEach((con, idx) => {
  //   wires.forEach((innnerCon, innerIdx) => {
  //     if (idx === innerIdx) {
  //       return;
  //     }
  //   });
  // });
};

// case 1.
const n = 9;
const wires = [
  [1, 3],
  [2, 3],
  [3, 4],
  [4, 5],
  [4, 6],
  [4, 7],
  [7, 8],
  [7, 9],
];
const result = 3;

// // case 2.
// const n =4
// const wires = 	[[1,2],[2,3],[3,4]]
// const result = 0

// // case 3.
// const n = 7
// const wires =	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
// const result = 1

console.log(solution(n, wires));
