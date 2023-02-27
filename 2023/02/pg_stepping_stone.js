const solution = (distance, rocks, n) => {
  rocks = rocks.sort((a, b) => a - b);

  let left = 1;
  let right = distance;

  const gapArr = rocks.reduce((prev, rock, idx) => {
    if (idx === 0) {
      prev.push(rock);
    } else {
      prev.push(rock - rocks[idx - 1]);
    }

    if (idx === rocks.length - 1) {
      prev.push(distance - rock);
    }

    return prev;
  }, []);

  while (left <= right) {
    let removedStone = 0;
    let middle = Math.floor((left + right) / 2);

    [...gapArr].reduce((prevGap, gap) => {
      prevGap += gap;
      if (prevGap > middle) {
        return 0;
      } else {
        removedStone += 1;
        return prevGap;
      }
    }, 0);

    if (removedStone > n) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
  }

  return left;
};

const distance = 25;
const rocks = [2, 14, 11, 21, 17];
const n = 2;

console.log(solution(distance, rocks, n));

// 이전 고생했던 코드
// const solution = (distance, rocks, n) => {
//   rocks = rocks.sort((a, b) => a - b);
//
//   const allCombis = [];
//   const visited = new Array(rocks.length).fill(false);
//
//   const combi = (
//     crntRocks = [],
//     crntIdx = 0,
//     pickN = 0,
//     visitArr = visited
//   ) => {
//     if (pickN === rocks.length - n) {
//       allCombis.push([...crntRocks]);
//       return;
//     }
//
//     for (let i = crntIdx; i < rocks.length; i++) {
//       if (!visitArr[i]) {
//         crntRocks.push(rocks[i]);
//         visitArr[i] = true;
//         combi(crntRocks, i + 1, pickN + 1, visitArr);
//
//         crntRocks.pop();
//         visitArr[i] = false;
//       }
//     }
//   };
//
//   combi();
//
//   let minStep = 0;
//   const l = allCombis[0].length;
//
//   //   allCombis.map((elm) => {
//   //     let crntMin = Infinity;
//   //     elm.map((innerElm, idx) => {
//   //       let crntStep;
//   //       if (idx == l - 1) {
//   //         crntStep = distance - innerElm;
//   //       } else if (idx === 0) {
//   //         crntStep = innerElm;
//   //       } else {
//   //         crntStep = elm[idx + 1] - innerElm;
//   //       }
//
//   //       if (crntStep < crntMin) {
//   //         crntMin = crntStep;
//   //       }
//   //     });
//
//   //     if (crntMin > minStep) {
//   //       minStep = crntMin;
//   //     }
//   //   });
//
//   return minStep;
// };
