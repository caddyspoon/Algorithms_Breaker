const solution = function(n, times) {
	let answer = 0;

	let left = 1
	let right = Math.max( ...times ) * n;

	while (left <= right) {
		// 대상이 되는 시간
		let midTime = Math.floor((left + right) / 2);

		let servedCustomers = 0;
		for (const elm of times) {
			servedCustomers += Math.floor(midTime / elm);
		}

		if (n > servedCustomers) {
			left = midTime + 1;
		} else if (n <= servedCustomers) {
			answer = midTime;
			right = midTime - 1;
		}
	};

	return answer;
};