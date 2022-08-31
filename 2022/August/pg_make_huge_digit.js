const solution = (number, k) => {

  let changed = true;
  let modiNum = [...number]

  while (k > 0 && changed) {
    changed = false;
    let acumIdx = 1;
  
    for (let i = 1; i < modiNum.length; i++) {
      const prevNo = modiNum[i-1];
      const curNo = modiNum[i];
  
      if (Number(prevNo) < Number(curNo)) {
        // 잘라주는 뭔가를 한다.
        modiNum = [...modiNum.slice(acumIdx)]
        console.log("I cut it! ", modiNum)
        changed = true;
      }
  
      acumIdx += 1;
      if (acumIdx > k) {
        break;
      }
      // 그렇지 않으면 누적 합계를 증가, k보다 작을 때까지만
    };
  }

  
};

const number = "4177252841";
const k =	4;	
const result = "775841";

console.log(solution(number, k));