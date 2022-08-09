const solution= function (rectangle, characterX, characterY, itemX, itemY) {
    // let answer = 0;

    const pprint = (pan) => {
        for (const i in pan) {
            console.log(pan[i].join("    "));
        }
        // for (let i = pan.length - 1 ; i >= 0; i -= 1) {
        //     for (let j = 0; j < pan[0].length; j += 1) {
        //         // console.log(pan[i][j])
        //         // process.stdout.write(pan[i][j]);
        //     }
        // }
        // process.stdout.write('\n');
    };


    // 최대 맵사이즈를 구해서 빈 공간에 맵 그리기
    let mapSizeInfo = [Infinity, Infinity, -1, -1];
    for (const dots of rectangle){
        for (const idx in dots) {
            if (idx < 2) {
                if (mapSizeInfo[idx] > dots[idx]) {
                    mapSizeInfo[idx] = dots[idx];
                }
            } else {
                if (mapSizeInfo[idx] < dots[idx]) {
                    mapSizeInfo[idx] = dots[idx];
                }
            }
        }
    }

    let pan = new Array(mapSizeInfo[3] + 2).fill(0).map(() => new Array(mapSizeInfo[2] + 2).fill(0));

    // 각 도형의 테두리를 도형 숫자로 기입
    let squareNo = 1;

    for (const elm of rectangle) {
        // // 가로선 그리기
        // for (let i = mapSizeInfo[0]; i < mapSizeInfo[2]; i++) {
        // 	pan[mapSizeInfo[1]][i] = 1;
        // 	pan[mapSizeInfo[3]][i] = 1;
        // }
        //
        // // 세로선 그리기
        // for (let i = mapSizeInfo[1]; i < mapSizeInfo[3]; i++) {
        // 	pan[i][mapSizeInfo[0]] = 1;
        // 	pan[i][mapSizeInfo[2]] = 1;
        // }

        // option 1.
        // 가로선 그리기
        for (let i = elm[0]; i <= elm[2]; i++) {

            // pan[elm[1]][i] = squareNo;
            // pan[elm[3]][i] = squareNo;

            if (pan[elm[1]][i] === 0) {
                pan[elm[1]][i] = squareNo;
            } else {
                // pan[elm[1]][i] = 'X'
                pan[elm[1]][i] = [pan[elm[1]][i], squareNo];
            }

            if (pan[elm[3]][i] === 0) {
                pan[elm[3]][i] = squareNo;
            } else {
                // pan[elm[3]][i] = 'X'
                pan[elm[3]][i] = [pan[elm[3]][i], squareNo];
            }
        }
        //
        // 세로선 그리기
        for (let i = elm[1] + 1; i < elm[3]; i++) {
        	// pan[i][elm[0]] = squareNo;
        	// pan[i][elm[2]] = squareNo;

            if (pan[i][elm[0]] === 0) {
                pan[i][elm[0]] = squareNo
            } else {
                // pan[i][elm[0]] = 'X'
                pan[i][elm[0]] = [pan[i][elm[0]], squareNo];
            }

            if (pan[i][elm[2]] === 0) {
                pan[i][elm[2]] = squareNo
            } else {
                // pan[i][elm[2]] = 'X'
                pan[i][elm[2]] = [pan[i][elm[2]], squareNo];
            }


        }

        squareNo += 1;
        // option 2. 전부 색칠해버리기
        // for (let j = elm[1]; j <= elm[3]; j++) {
        //     for (let i = elm[0]; i <= elm[2]; i++) {
        //         pan[j][i] = 1;
        //         pan[j][i] = 1;
        //     }}

    }

    // 내부 다 지워버리기
    for (const elm of rectangle) {
        for (let j = elm[1] + 1; j < elm[3]; j++) {
            for (let i = elm[0] + 1; i < elm[2]; i++) {
                pan[j][i] = 0;
                pan[j][i] = 0;
        }}
    }

    console.log("BFS 전 지도");
    pprint(pan);

    const dx = [1, 0, -1, 0, 1, 1, -1, -1];
    const dy = [0, 1, 0, -1, 1, -1, 1, -1];

    // // 테두리 만들기
    // const visited = new Array(mapSizeInfo[3] + 2).fill(0).map(() => new Array(mapSizeInfo[2] + 2).fill(false));
    const stack = [];
    //
    // const stack = [[0, 0]];
    // visited[0][0] = true;
    //
    // while (stack.length) {
    //     const [p, q] = stack.pop();
    //
    //     for (const i in [0, 1, 2, 3, 4, 5, 6, 7]) {
    //         const nx = p + dx[i];
    //         const ny = q + dy[i];
    //
    //         if (0 <= nx && nx < visited[0].length && 0 <= ny && ny < visited.length) {
    //             if (!visited[ny][nx]) {
    //                 if (pan[ny][nx] === 0 && i <4) {
    //                     visited[ny][nx] = true;
    //                     stack.push([nx, ny]);
    //                 } else if (pan[ny][nx] === 1) {
    //                     pan[ny][nx] = 2;
    //                 }
    //             }
    //         }
    //     }
    // }

    // for (const i in pan){
    // 	console.log(pan[i].join(' '));
    // }


    // Y좌표, X 좌표, 현재 도형, 과거 도형


    // stack.push([characterY, characterX, 0, pan[characterY][characterX], pan[characterY][characterX]]);

    // 출발점 초기화
    for (const idx in [0, 1, 2, 3]) {
        const ny = characterY + dy[idx];
        const nx = characterX + dx[idx];

        if (pan[ny][nx] !== 0) {
            stack.push([ny, nx, 1, pan[ny][nx], pan[characterY][characterX]]);
        }
    }

    pan[itemY][itemX] = 'E';

    // 방문여부 확인 Arr
    const visitedTrip = new Array(mapSizeInfo[3] + 2).fill(0).map(() => new Array(mapSizeInfo[2] + 2).fill(false));

    // 첫 위치 true
    visitedTrip[characterY][characterX] = true;

    pan[characterY][characterX] = 'S';

    console.log("시작 전")
    pprint(pan);
    console.log(" ")

    while (stack.length) {
        const [currentY, currentX, depth, currentSquare, prevSquare] = stack.shift();

        for (const idx in [0, 1, 2, 3]) {
            const nx = currentX + dx[idx];
            const ny = currentY + dy[idx];

            if (0 <= nx && nx < visitedTrip[0].length && 0 <= ny && ny < visitedTrip.length) {
                if (pan[ny][nx] === 'E') {
                    console.log("종료")
                    pprint(pan);

                    console.log("The answer is :", depth + 1)
                    return depth + 1
                }

                if (!visitedTrip[ny][nx] && pan[ny][nx] !== 0) {
                    console.log("currentSquare: ", currentSquare)
                    console.log("prevSquare: ", prevSquare)
                    console.log("현재 위치: ", ny, nx)

                    // 교차점을 만났을 경우
                    if (Array.isArray(pan[ny][nx])) {
                        console.log()
                        console.log("교차점 접근");
                        console.log("현재 교차점: ", pan[ny][nx])
                        if (pan[ny][nx].includes(currentSquare)) {
                            visitedTrip[ny][nx] = true;

                            // let tempSqr = pan[ny][nx][0] === currentSquare ? pan[ny][nx][1] : pan[ny][nx][0];
                            let tempSqr = NaN;
                            if (pan[ny][nx][0] === currentSquare) {
                                tempSqr = pan[ny][nx][1]
                            } else if (pan[ny][nx][1] === currentSquare) {
                                tempSqr = pan[ny][nx][0]
                            }

                            console.log("교차 어레이", pan[nx][ny])
                            console.log("교차된 도형은: ", tempSqr);
                            stack.push([ny, nx, depth + 1, tempSqr, currentSquare])

                            // conosole에서 출력을 보기 위한 스트링 처리
                            pan[ny][nx] = 'V'
                            break;
                        }
                    }

                    // 일반 진행 경우
                    if (pan[ny][nx] === currentSquare) {
                        visitedTrip[ny][nx] = true;

                        stack.push([ny, nx, depth + 1, pan[ny][nx], currentSquare])

                        pan[ny][nx] = 'V'
                        break;
                    }


                    // if (currentSquare === 'X' && prevSquare != pan[ny][nx] && pan[ny][nx] !== 'X') {
                    //     visitedTrip[ny][nx] = true;
                    //     stack.push([ny, nx, depth + 1, pan[ny][nx], currentSquare])
                    //
                    //     pan[ny][nx] = 'V'
                    //     break;
                    //
                    // // 일반 진행 경우
                    // } else if (1 <= currentSquare && currentSquare <= 4) {
                    //     if (pan[ny][nx] === currentSquare || pan[ny][nx] === 'X') {
                    //         visitedTrip[ny][nx] = true;
                    //
                    //         stack.push([ny, nx, depth + 1, pan[ny][nx], currentSquare])
                    //
                    //         pan[ny][nx] = 'V'
                    //         break;
                    //     }
                    // }
                }
            }
        }

        pprint(pan);
        console.log()
    }


    // // // 스타팅 포인트
    // for (const idx in [0, 1, 2, 3]) {
    // 	const sx = characterX + dx[idx];
    // 	const sy = characterY + dy[idx];
    //
    // 	if (pan[sy][sx] === 0) {
    // 		pan[sy][sx] = 'S';
    // 		// y좌표, x좌표, depth, 현재 방향, 방향이 꺾인 횟수
    // 		stack.push([sy, sx, 0, NaN, 0]);
    // 		break;
    // 	}
    // }
    // //
    // // // 엔드 포인트
    // for (const idx in [0, 1, 2, 3]) {
    // 	const sx = itemX + dx[idx];
    // 	const sy = itemY + dy[idx];
    //
    // 	if (pan[sy][sx] === 0) {
    // 		pan[sy][sx] = 'E'
    // 		break;
    // 	}
    // }


    // return answer;
}

// const rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]];
// const characterX = 1;
// const characterY = 3;
// const itemX = 7;
// const itemY = 8;
// const result = 17;

const rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]];
const characterX = 9;
const characterY = 7;
const itemX = 6;
const itemY = 1;
const result = 11;

// const rectangle = [[1,1,5,7]];
// const characterX = 1;
// const characterY = 1;
// const itemX = 4;
// const itemY = 7;
// const result = 9;
//
// const rectangle = [[2,1,7,5],[6,4,10,10]];
// const characterX = 3;
// const characterY = 1;
// const itemX = 7;
// const itemY = 10;
// const result = 15;
//
// const rectangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]];
// const characterX = 1;
// const characterY = 4;
// const itemX = 6;
// const itemY = 3;
// const result = 10;

console.log(solution(rectangle, characterX, characterY, itemX, itemY) === result);