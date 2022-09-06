const solution = (number, k) => {   
  let stack = [];
  
  for (num of number) {    
    if (stack.at(-1) === 9) {
      stack.push(num);
      continue;
    }
      
    if (stack.at(-1) < num) {
      while (k > 0 && stack.at(-1) < num && stack.length) {
        stack.pop();
        k -= 1;
      }
    }

    stack.push(num);
  };

  if (k > 0) {
    stack = stack.slice(0, stack.length - k)
  }

  return stack.join("");
}


const number = "4177252841";
const k =	4;	
const result = "775841";

console.log(solution(number, k));