const solution = (begin, target, words) => {
  const isSibling = (aWord, bWord) => {
    let difCnt = 0;
    for (let i = 0; i < aWord.length; i += 1) {
      if (aWord[i] !== bWord[i]) {
        difCnt += 1;
        if (difCnt > 1) {
          return false;
        }
      }
    }

    return true;
  };

  let minCnt = Infinity;
  const dfs = (statWord = begin, wordsArr = words, cnt = 0) => {
    if (!wordsArr.length || statWord === target) {
      if (statWord === target && cnt < minCnt) {
        minCnt = cnt;
      }
      return;
    }

    for (let i = 0; i < wordsArr.length; i += 1) {
      if (isSibling(statWord, wordsArr[i])) {
        const _wordsArr = [...wordsArr];
        _wordsArr.splice(i, 1);
        dfs(wordsArr[i], _wordsArr, cnt + 1);
      }
    }
  };

  dfs();
  return minCnt === Infinity ? 0 : minCnt;
};
