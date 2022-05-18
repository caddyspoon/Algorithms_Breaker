function solution(clothes) {
  let answer = 1;
  
  const dict = {};
  for (const elm of clothes) {
    if (!(elm[1] in dict)) {
      dict[elm[1]] = 1;
    } else {
      dict[elm[1]] += 1;
    }
  }

  for (const elm in dict) {
    answer *= dict[elm] + 1;
  }
    
  

//   const comb = (n, arr = infoArr, p = 0, nextIdx = 0, picked = []) => {
//     if (n === p) {
//       let currValue = 1;
//       for (const elm of picked) {
//         currValue *= infoArr[elm];
//       }
//       answer += currValue;
//       return;
//     }

//     for (let i = nextIdx; i < arr.length; i++) {
//       if (i - p > arr.length - 1) {
//         return;
//       }
        
//       const newPicked = [ ...picked, i ];
//       comb(n, arr, p + 1, i + 1, newPicked);
      
//     }
//   }

//   for (let i = 1; i < infoArr.length + 1; i++) {
//     comb(i);
//   }

  return answer - 1;
}

// const clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]];
// const answer = 5;

const clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]];
const answer = 3;

// const clothes = [["동그란_안경", "얼굴"], ["검정_선글라스", "얼굴"], ["파란색_티셔츠", "상의"], ["빨간색_티셔츠", "상의"], ["청바지", "하의"], ["면바지", "하의"], ["겉옷", "코트"]];

console.log(solution(clothes) === answer);