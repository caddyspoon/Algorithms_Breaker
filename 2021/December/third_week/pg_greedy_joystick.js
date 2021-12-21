function aToZ(char) {
  return char.charCodeAt(0) - "A".charCodeAt(0)
}

function zToA(char) {
  return "Z".charCodeAt(0) - char.charCodeAt(0) + 1 
}


function solution(name) {
  let answer = 0;
  let arr = new Array(name.length).fill(1)
   
  let idx = 0
  for (let char of name) {
      const crntNum = Math.min(aToZ(char), zToA(char))
      if (crntNum > 0) {
          arr[idx] = 0            
      }
      answer += crntNum
      idx += 1        
  }

  arr[0] = 1  
  let minMoving = Infinity

  function journey(arr, n=0, crntIdx=0) {
    if (n >= minMoving) {
      return
    }

    let ret = arr.reduce((a, b) => a + b);
    if (ret === name.length) {
      if (n < minMoving) {
        minMoving = n
      }
      return
    }

    for (let i=0; i<2; i++) {
      if (i===0) {
        // 일단 왼쪽으로 이동해보자
        // 가장 오른쪽에 있는 친구의 IDX를 구해보자
        let crntMoving = 0
        let crntLoc = crntIdx
        while (true) {
          crntLoc -= 1
          if (crntLoc === -1) {
            crntLoc = name.length - 1
          }
          crntMoving += 1

          if (arr[crntLoc] === 0) {
            arr[crntLoc] = 1
            journey(arr, n + crntMoving, crntLoc)
            arr[crntLoc] = 0
            break;
          }
        }
      } else {
        // 좋아 이번엔 오른쪽으로 움직여 보자
        // 나와 가장 가까운 친구의 IDX를 구해보자
        let crntMoving = 0
        let crntLoc = crntIdx
        while (true) {
          crntLoc += 1
          if (crntLoc === name.length) {
            crntLoc = 0
          }
          crntMoving += 1

          if (arr[crntLoc] === 0) {
            arr[crntLoc] = 1
            journey(arr, n + crntMoving, crntLoc)
            arr[crntLoc] = 0
            break;
          }
        }
      }
    }
  }

  journey(arr)
  answer += minMoving

  return answer;
}


const inputExam = [
  {name: "JEROEN", answer: 56},
  {name: "JAN", answer: 23}
]

for (const elm of inputExam) {
  const {name, answer} = elm
  // const { name, return } = elm
  // const { name, return } = key

  if (solution(name) === answer) {
    console.log("Correct")
  }
  else {
    console.log("False")
  }
}

