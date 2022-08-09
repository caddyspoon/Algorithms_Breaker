def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    def pprint(pan):
        for i in range(len(pan) -1, -1, -1):
            for j in range(len(pan[0])):
                print(pan[i][j], end = " ")
            print()
        print()

    # 최대 맵사이즈를 구해서 빈 공간에 맵 그리기
    mapSizeInfo = [float('inf'), float("inf") -1, -1]

    for dots in  rectangle:
        for idx in dots:
            if (idx < 2):
                if (mapSizeInfo[idx] > dots[idx]):
                    mapSizeInfo[idx] = dots[idx]
                else:
                    if (mapSizeInfo[idx] < dots[idx]):
                        mapSizeInfo[idx] = dots[idx]


    pan = [0 for _ in range(mapSizeInfo[2] + 2)] * (mapSizeInfo[3] + 2)

    # 각 도형의 테두리를 도형 숫자로 기입
    squareNo = 1

    for elm in rectangle:
        # option 1.
        # 가로선 그리기
        for i in range(elm[0], elm[2]):

            if (pan[elm[1]][i] == 0):
                pan[elm[1]][i] = squareNo
            else:
                pan[elm[1]][i] = [pan[elm[1]][i], squareNo]

            if (pan[elm[3]][i] == 0):
                pan[elm[3]][i] = squareNo
            else:
                pan[elm[3]][i] = [pan[elm[3]][i], squareNo]


        # 세로선 그리기
        for i in range(elm[1], elm[3]):
            if (pan[i][elm[0]] == 0):
                pan[i][elm[0]] = squareNo
                pan[i][elm[0]] = [pan[i][elm[0]], squareNo]

            if (pan[i][elm[2]] == 0):
                pan[i][elm[2]] = squareNo
            else:
                pan[i][elm[2]] = [pan[i][elm[2]], squareNo]

        squareNo += 1

    # 내부 다 지워버리기
    for elm in rectangle:
        for j in range(elm[1] + 1, elm[3]):
            for i in range(elm[0] + 1, elm[2]):
                pan[j][i] = 0
                pan[j][i] = 0

    print("BFS 전 지도")
    pprint(pan)

    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    # 테두리 만들기
    stack = []

    # 출발점 초기화
    for idx in [0, 1, 2, 3]:
        ny = characterY + dy[idx]
        nx = characterX + dx[idx]

        if (pan[ny][nx] != 0):
            stack.push([ny, nx, 1, pan[ny][nx], pan[characterY][characterX]])

    pan[itemY][itemX] = 'E'

    # 방문여부 확인 Arr
    visitedTrip = [0 for _ in range(mapSizeInfo[2] + 2)] * (mapSizeInfo[3] + 2)

    # 첫 위치 true
    visitedTrip[characterY][characterX] = True

    pan[characterY][characterX] = 'S'

    print("시작 전")
    pprint(pan)
    print(" ")

    while (stack):
        currentY, currentX, depth, currentSquare, prevSquare = stack.pop(0)

        for idx in [0, 1, 2, 3]:
            nx = currentX + dx[idx]
            ny = currentY + dy[idx]

            if 0 <= nx < len(visitedTrip[0]) and 0 <= ny < len(visitedTrip):
                if pan[ny][nx] == 'E':
                    print("종료")
                    pprint(pan)
                    print("The answer is :", depth + 1)
                    return depth + 1

            if not visitedTrip[ny][nx] and pan[ny][nx] != 0:
                print("currentSquare: ", currentSquare)
                print("prevSquare: ", prevSquare)
                print("현재 위치: ", ny, nx)

            # 교차점을 만났을 경우
            if len(pan[ny][nx]) > 1:
                print()
                print("교차점 접근")
                print("현재 교차점: ", pan[ny][nx])
                
                if pan[ny][nx] in currentSquare:
                    visitedTrip[ny][nx] = True

                    tempSqr = None
                    if pan[ny][nx][0] == currentSquare:
                        tempSqr = pan[ny][nx][1]
                    elif pan[ny][nx][1] == currentSquare:
                        tempSqr = pan[ny][nx][0]

                    print("교차 어레이", pan[nx][ny])
                    print("교차된 도형은: ", tempSqr)
                    stack.push([ny, nx, depth + 1, tempSqr, currentSquare])

                    # conosole에서 출력을 보기 위한 스트링 처리
                    pan[ny][nx] = 'V'
                    break

            # 일반 진행 경우
            if pan[ny][nx] == currentSquare:
                visitedTrip[ny][nx] = True
                stack.push([ny, nx, depth + 1, pan[ny][nx], currentSquare])

                pan[ny][nx] = 'V'
                break


        pprint(pan)
        print()

#  rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
#  characterX = 1
#  characterY = 3
#  itemX = 7
#  itemY = 8
#  result = 17

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
result = 11

#  rectangle = [[1,1,5,7]]
#  characterX = 1
#  characterY = 1
#  itemX = 4
#  itemY = 7
#  result = 9
#
#  rectangle = [[2,1,7,5],[6,4,10,10]]
#  characterX = 3
#  characterY = 1
#  itemX = 7
#  itemY = 10
#  result = 15
#
#  rectangle = [[2,2,5,5],[1,3,6,4],[3,1,4,6]]
#  characterX = 1
#  characterY = 4
#  itemX = 6
#  itemY = 3
#  result = 10

print(solution(rectangle, characterX, characterY, itemX, itemY) == result)