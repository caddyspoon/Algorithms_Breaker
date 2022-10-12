const solution = (s) => {
  const wordsObj = {
      zero: 0,
      one: 1,
      two: 2,
      three: 3,
      four: 4,
      five: 5,
      six: 6,
      seven: 7,
      eight: 8,
      nine: 9
  };
  
  let tempWords = "";
  let answerString = "";
  
  [...s].map(elm => {
      if ("0".charAt() <= elm.charAt() && elm.charAt() <= "9".charAt()) {
          answerString += elm;
      } else {
          tempWords += elm;

          if (tempWords in wordsObj) {
              answerString += String(wordsObj[tempWords]);
              tempWords = "";
          }
      }
  })
  
  return Number(answerString);
}