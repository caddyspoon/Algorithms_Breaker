function solution(lines) {
  let answer = 0;

  const times = [];

  lines.forEach(line => {
    const timeStamp = new Date(line.split(" ").slice(0, 2).join(" "));
    const spendToms = Number(line.split(" ")[2].slice(0, -1)) * 1000;

    times.push([new Date(timeStamp - spendToms + 1), timeStamp]);
  })
    
  for (let i = 0; i < times.length; i++) {
    let cnt = 0;
      
    let startTime = times[i][1];

    let endTime = new Date(times[i][1].getTime());
    endTime = endTime.setSeconds(endTime.getSeconds() + 1);  

    for (let j = i; j < times.length; j++) {
      if (times[j][0] < endTime && times[j][1] >= startTime) {
        cnt += 1;
      }
    }

    if (cnt > answer) {
      answer = cnt;
    }
  }

  return answer;
}