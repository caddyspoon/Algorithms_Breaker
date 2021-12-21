const n = 5;
const lost = [2, 4]; 
const reserve = [1, 3, 5];
const qAnswer = 5;

function solution(n, lost, reserve) {
  const uniforms = new Array(n).fill(1) 
  
  lost.forEach(i => uniforms[i-1] -= 1);
  reserve.forEach(i => uniforms[i-1] += 1)
  
  for (let i=0; i<n;  i++) {
    if (uniforms[i] >= 2) {
      if (i-1 >= 0 && uniforms[i-1] === 0) {
        uniforms[i-1] += 1
        uniforms[i] -= 1
        continue
      }
      if (i+1 < n && uniforms[i+1] === 0) {
        uniforms[i+1] += 1
        uniforms[i] -= 1
      }
    }
  }
  let answer = 0;
  uniforms.forEach(elm => {if (elm > 0) answer += 1})
  return answer;
}

solution(n, lost, reserve)