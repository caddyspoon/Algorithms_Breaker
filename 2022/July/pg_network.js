const solution = function(n, computers) {
	let answer = 0;

	const visited = new Array(n).fill(false);

	for (const idx in computers) {
		if (!visited[idx]) {
			const info = computers[idx];
			const stack = [];

			// 현재 네트워크 정보를 통해 stack 만들기
			for (const jdx in info) {
				if (jdx === idx) {
					continue;
				}

				if (!visited[jdx] && info[jdx]) {
					stack.push(jdx);
				}
			}

			while (stack.length) {
				const computerIdx = stack.pop();
				const infoArr = computers[computerIdx]

				for (const infoIdx in infoArr) {
					if (computerIdx === infoIdx) {
						continue;
					}

					if (!visited[infoIdx] && infoArr[infoIdx]) {
						stack.push(infoIdx);
					}
				}

				visited[computerIdx] = true;
			}

			answer += 1;
			visited[idx] = true;
		}
	}

	return answer;
};