const input = require('fs').readFileSync('14502_input.txt').toString().split('\n');

const caseNo = input.shift()
const dx = [0, 1, -1, 0]
const dy = [1, 0, 0, -1]


function solution() {

}

function dfs(arr, n, m) {
  const visited = [0] * n
}


for (let i = 0; i < caseNo; i += 1) {
  const [n, m] = input.shift().split(' ')
  
  const labInfo = []
  const visited = []
  const queue = []
  for (let i = 0; i < n; i += 1) {
    const tempArr = input.shift().split(' ')
    labInfo.push(tempArr)
    
    const tempVisitedArr = []
    for (let j = 0; j < m; j += 1) {
      tempVisitedArr.push(0)
    }
    visited.push(tempVisitedArr)
  }
  console.log('====================')
  console.log()

  let flag = 0
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (labInfo[i][j] == 0) {
        queue.push([i, j])
        flag = 1
        break
      }
    }
    if (flag) {
      break
    }
  }

}