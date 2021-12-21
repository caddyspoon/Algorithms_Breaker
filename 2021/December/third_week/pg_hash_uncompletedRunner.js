// https://programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  const infoDict = {}
  
  for (let key of participant) {
      if (key in infoDict) {
          infoDict[key] += 1        
      } else {
          infoDict[key] = 1
      }
  }
  
  for (let key of completion) {
      infoDict[key] -= 1
      if (infoDict[key] === 0) {
          delete infoDict[key]
      }
  }
  
  const answer = Object.keys(infoDict)[0]
  
  return answer;
}


const inputExam = [
  {participant: ["leo", "kiki", "eden"], completion: ["eden", "kiki"], answer: "leo"},
  {participant: ["marina", "josipa", "nikola", "vinko", "filipa"], completion: ["josipa", "filipa", "marina", "nikola"], answer: "vinko"},
  {participant: ["mislav", "stanko", "mislav", "ana"], completion: ["stanko", "ana", "mislav"], answer: "mislav"},
]

for (const elm of inputExam) {
  const { participant, completion, answer } = elm

  if (solution(participant, completion) === answer) {
    console.log("Correct")
  }
  else {
    console.log("False")
  }
}
