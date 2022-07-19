const solution = record => {
  const answer = [];

  const enterStr = "님이 들어왔습니다.";
  const outStr = "님이 나갔습니다.";

  const idMap = {};

  record.forEach(rec => {
    const inputArr = rec.split(" ");
    if (inputArr[0] === "Enter" || inputArr[0] === "Change") {
      idMap[inputArr[1]] = inputArr[2];
    }
  });

  record.forEach(rec => {
    const inputArr = rec.split(" ");
    const userId = idMap[inputArr[1]];

    if (inputArr[0] === "Enter") {
      const inputStr = `${userId}${enterStr}`;
      answer.push(inputStr);
    } else if (inputArr[0] === "Leave") {
      const inputStr = `${userId}${outStr}`;
      answer.push(inputStr);
    }
  })

  return answer;
};