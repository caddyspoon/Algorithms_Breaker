const quickSort = function(arr, left, right) {
  if (left < right) {
    const pivot = hoarePartion(arr, left, right);
    quickSort(arr, left, pivot - 1);
    quickSort(arr, pivot + 1, right);
  }
};


const hoarePartion = function(arr, left, right) {
  let i = left;
  let j = right;
  let pivot = arr[left];

  while (i <= j) {
    while (i <= j && arr[i] <= pivot) {
      i += 1;
    }

    while (i <= j && arr[j] >= pivot) {
      j -= 1;
    }

    if (i < j) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  [arr[left], arr[j]] = [arr[j], arr[left]];
  return j;
};

const arr1 = [4, 5, 1, 2, 9, 8, 3, 6, 7];
const arr2 = [2, 2, 1, 1, 3];

const arr = arr1.slice();
quickSort(arr, 0, arr.length -1 );

console.log(arr);