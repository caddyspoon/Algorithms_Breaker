const refineMusicInfo = (musicStr) => {
	const [startTime, endTime, songName, chords] = musicStr.split(",");

	const convertedChords = makeStringToNote(chords);

	const l = convertedChords.length;

	const [startHour, startMin] = startTime.split(":");
	const [endHour, endMin] = endTime.split(":");

	const hourLength = +endHour - +startHour;
	const minLength = +endMin - +startMin;

	const totalMin = hourLength * 60 + minLength;

	let playedChords = [];

	if (l > totalMin) {
		playedChords = [...convertedChords.slice(0, totalMin)];
	} else {
		const mock = Math.floor(totalMin / l);
		const nameoji = totalMin % l;

		for (let i = 0; i < mock; i += 1) {
			playedChords = [...convertedChords, ...playedChords];
		}

		playedChords = [...playedChords, ...convertedChords.slice(0, nameoji)];
	}

	return [songName, playedChords, totalMin];
};

const makeStringToNote = (noteString) => {
	const noteStrArr = [...noteString];

	let chordsStr = [];

	while (noteStrArr.length) {
		const p = noteStrArr.pop();
		if (p === "#") {
			const q = noteStrArr.pop();
			chordsStr.push(`${q}#`);
		} else {
			chordsStr.push(p);
		}
	}

	return chordsStr.reverse();
};

const solution = (m, musicinfos) => {
	const answer = [];

	const musicInfo = musicinfos.reduce((accum, elm) => {
		const [songName, playedChords, totalMin] = refineMusicInfo(elm);

		accum[makeStringToNote(playedChords).join("-") + "-"] = {
			songName,
			totalMin,
		};

		return accum;
	}, {});

	const targetNote = makeStringToNote(m).join("-") + "-";

	console.log(musicInfo);

	for (const key in musicInfo) {
		if (key.includes(targetNote)) {
			const { songName, totalMin } = musicInfo[key];

			answer.push([totalMin, songName]);
		}
	}

	if (!answer.length) {
		return "(None)";
	}

	answer.sort((a, b) => {
		return b[0] - a[0];
	});

	return answer[0][1];
};

// const m = "ABCDEFG";
// const musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"];
// const answer = "HELLO";

const m = "ABC";
const musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"];
const answer = "WORLD";

console.log(solution(m, musicinfos));
