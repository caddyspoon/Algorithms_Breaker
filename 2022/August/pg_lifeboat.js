const solution = (people, limit) => {
  let answer = 0;
  
  const maxSorted = people.sort((a, b) => {return a - b});

  let backStand = maxSorted.length - 1;
  for (idx in maxSorted) {
    if (idx > backStand) {
      break;
    }

    const curPerson = maxSorted[idx];
    answer += 1;

    for (let i = backStand; i > idx; i--) {
      const partner = maxSorted[i];
      backStand -= 1;
        
      if (curPerson + partner > limit) {
        answer += 1;
      } else {
        break;
      }
    }
  }

  return answer;
}

const people = [[70, 50, 80, 50], [70, 80, 50]];
const limit = [100, 100];
const result = [3, 3];

for (i of [0, 1]) {
  console.log(solution(people[i], limit[i]) === result[i]);
}