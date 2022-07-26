const solution = (maps) => {
	let answer = -1;

	const queue = [[0, 0, 1]];

	const visited = new Array(maps.length).fill().map(() => new Array(maps[0].length).fill(false));
	visited[0][0] = true;

	const dx = [0, 1, 0, -1];
	const dy = [1, 0, -1, 0];

	let flag = false;
	while (queue.length && !flag) {
		const [p, q, d] = queue.shift();
		let depth = d;

		for (const idx of [0, 1, 2, 3]) {
			const nx = p + dx[idx];
			const ny = q + dy[idx];

			if (nx === maps.length - 1 && ny === maps[0].length - 1) {
				answer = depth + 1
				flag = true;
				break;
			}

			if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length) {
				if (!visited[nx][ny] && maps[nx][ny]) {
					queue.push([nx, ny, depth + 1]);
					visited[nx][ny] = true;
				}
			}
		}
	}

	return answer;
};