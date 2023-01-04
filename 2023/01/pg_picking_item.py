# 예쁘게 그려보기
def pp(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                print(board[i][j], end = " ")
            else:
                print(".", end = " ")
        print()
    print()

# 높이와 너비 구하기
def cal_wh(rectangle):
    h = 0
    w = 0
    # 보드의 높이와 너비 구하기
    for elm in rectangle:
        a, b, x, y = elm
        a *= 2
        b *= 2
        x *= 2
        y *= 2

        if h < y:
            h = y
        if w < x:
            w = x
    # 전체 보드 위에 테두리를 그리기 위해 추가
    return h + 2, w + 2

# 인덱스 유효 판별 함수
def isIn(x, y, h, w):
    if 0 <= x < h and 0 <= y < w:
        return True
    return False

# 사각형을 판위에 모두 그리기
def draw_board(rectangle, w, h):
    pan = [[0 for _ in range(w)] for _ in range(h)]

    # 보드에 사각형 그려주기
    for elm in rectangle:
        a, b, x, y = elm
        a *= 2
        b *= 2
        x *= 2
        y *= 2

        for i in range(a, x + 1):
            pan[b][i] += 1
            pan[y][i] += 1

        for j in range(b + 1, y):
            pan[j][a] += 1
            pan[j][x] += 1
    
    return pan


# 밖에서 윤곽선 그리기
def draw_line(pan):
    h = len(pan)
    w = len(pan[0])

    # 8방향
    ddx = [0, 1, 1, 1, 0, -1, -1, -1]
    ddy = [1, 1, 0, -1, -1, -1, 0, 1]

    init_stack = [[0, 0]]
    inner_visited = [[False for _ in range(w)] for _ in range(h)]
    outlines = [[0 for _ in range(w)] for _ in range(h)]
    total_cnt = 0

    while init_stack:
        p, q = init_stack.pop()

        for i in range(8):
            np = p + ddx[i]
            nq = q + ddy[i]

            if isIn(np, nq, h, w):

                if not inner_visited[np][nq]:
                    inner_visited[np][nq] = True
                    # 벽이면 그리고 넘어가기                
                    if pan[np][nq] > 0:
                        outlines[np][nq] = 1
                        total_cnt += 1
                    elif pan[np][nq] == 0:
                        init_stack.append([np, nq])
    
    return outlines, total_cnt


# 아이템 줍기
def picking_item(outlines, characterY, characterX, itemY, itemX):
    w = len(outlines[0])
    h = len(outlines)
    
    visited = [[False for _ in range(w)] for _ in range(h)]

    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    init_flag = False
    sx, sy = 0, 0

    # 시작점 표시
    outlines[characterY][characterX] = "S"

    # 시작 위치 찾기
    for i in range(4):
        nx = characterY + dx[i]
        ny = characterX + dy[i]
        if outlines[nx][ny]:
            if not init_flag:
                init_flag = True
                sx, sy = nx, ny
                break

    stack = [[sx, sy, 0]]
    visited[characterY][characterX] = True
    visited[sx][sy] = True

    while stack:
        p, q, steps = stack.pop()

        for i in range(4):
            np = p + dx[i]
            nq = q + dy[i]

            if outlines[np][nq] == "S":
                continue

            # 아이템을 주웠을 때
            if np == itemY and nq == itemX and not visited[np][nq]:
                # 출발점 한 칸 앞에서 시작했기 때문에 한 칸(두 배해서 + 2) 더해줌
                return steps + 2

            if not visited[np][nq] and outlines[np][nq] == 1:
                visited[np][nq] = True
                stack.append([np, nq, steps + 1])


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 그림을 두배로 늘리기 위해 2를 곱해준다.
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    # 최대 너비와 최대 높이를 구해준다.
    h, w = cal_wh(rectangle)

    # 주어진 너비와 높이 정보를 이용해서 사각형이 모두 그려진 판 그리기
    pan = draw_board(rectangle, w, h)

    # 맨 바깥쪽 테두리만 남겨준 보드를 그려준다.
    outlines, total_cnt = draw_line(pan)

    # 해당 그림 정보를 이용해 아이템 줍기
    target_step = picking_item(outlines, characterY, characterX, itemY, itemX)
    
    # 2배된 값을 축소
    target_step //= 2
    total_cnt //= 2

    return min(target_step, total_cnt - target_step)