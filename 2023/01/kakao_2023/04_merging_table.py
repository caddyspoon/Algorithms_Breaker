def update_cell(table, com):
    com = com[1:]
    if len(com) == 3:
        r, c, value = com
        r, c = int(r), int(c)
        target_cell = table[r][c]
        target_cell[0] = value
        
    elif len(com) == 2:
        v1, v2 = com
        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                if table[i][j][0] == v1:
                    table[i][j][0] = v2

    else:
        raise RuntimeError("UPDATE 매개변수 개수가 잘못 되었습니다.")

# 핵심 아이디어
# 리스트를 변수에 할당하면, 해당 리스트의 ID 값만 복사하므로 해당 ID 값을 부여하기 위해 값이 아닌 리스트를 변수에 할당
# 병합하며 자식 셀들은 부모가 되는 리스트를 바라보므로, 이후 부모의 값이 UPDATE될 때 자식 셀의 값도 업데이트 된다.
def merge_cell(table, com):
    r1, c1, r2, c2 = com[1:]
    r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
    
    
    if r1 == r2 and c1 == c2:
        return

    cell1 = table[r1][c1]
    cell2 = table[r2][c2]

    v1 = cell1[0]
    v2 = cell2[0]

    parent_cell = []
    child_id = 0

    if v2 and not v1:
        child_id = id(cell1)
        parent_cell = cell2
    else:
        child_id = id(cell2)
        parent_cell = cell1

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if id(table[i][j]) == child_id:
                table[i][j] = parent_cell

def unmerge_cell(table, com):
    r, c = com[1:]
    r, c = int(r), int(c)

    value = table[r][c][0]
    target_cell_id = id(table[r][c])

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            cell_id = id(table[i][j])

            if cell_id == target_cell_id:
                table[i][j] = [None]

    if value:
        table[r][c][0] = value
    
def print_cell(table, com):
    r, c = com[1:]
    r, c = int(r), int(c)

    if table[r][c][0]:
        return table[r][c][0]
    else:
        return 'EMPTY'

def solution(commands):
    answer = []
    
    # 리스트 자체를 값으로 만들어주기 위해 None이 아닌 [None]을 요소로 넣어준다.
    table = [[[None] for _ in range(51)] for _ in range(51)]    
    
    for raw_com in commands:
        com = raw_com.split(" ")
        command = com[0]
        
        if command == "UPDATE":
            update_cell(table, com)
        elif command == "MERGE":
            merge_cell(table, com)
        elif command == "UNMERGE":
            unmerge_cell(table, com)
        elif command == "PRINT":
            answer.append(print_cell(table, com))

    return answer

# id 확인을 위한 solution
# def update_cell(table, com):
#     com = com[1:]
#     if len(com) == 3:
#         r, c, value = com
#         r, c = int(r), int(c)
#         target_cell = table[r][c]

#         target_cell[0][0] = value
#     elif len(com) == 2:
#         v1, v2 = com
#         for i in range(1, len(table)):
#             for j in range(1, len(table[0])):
#                 if table[i][j][0][0] == v1:
#                     table[i][j][0][0] = v2

#     else:
#         raise RuntimeError("UPDATE 매개변수 개수가 잘못 되었습니다.")

# def merge_cell(table, com):
#     r1, c1, r2, c2 = com[1:]
#     r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
    
    
#     if r1 == r2 and c1 == c2:
#         return

#     cell1 = table[r1][c1]
#     cell2 = table[r2][c2]

#     v1 = cell1[0][0]
#     v2 = cell2[0][0]

#     parent_cell = []
#     parent_id = 0
#     child_id = 0

#     if v2 and not v1:
#         parent_id = cell2[1]
#         child_id = cell1[1]
#         parent_cell = cell2[0]
#     else:
#         parent_id = cell1[1]
#         child_id = cell2[1]
#         parent_cell = cell1[0]

#     for i in range(1, len(table)):
#         for j in range(1, len(table[0])):
#             if table[i][j][1] == child_id:
#                 table[i][j][1] = parent_id
#                 table[i][j][0] = parent_cell


# def unmerge_cell(table, com):
#     r, c = com[1:]
#     r, c = int(r), int(c)

#     value = table[r][c][0][0]
#     target_cell_id = table[r][c][1]

#     for i in range(1, len(table)):
#         for j in range(1, len(table[0])):
#             crnt_cell = table[i][j]
#             cell_id = crnt_cell[1]

#             if cell_id == target_cell_id:
#                 crnt_cell[0] = [None]
#                 crnt_cell[1] = id(crnt_cell[0])

#     if value:
#         table[r][c][0][0] = value
    
# def print_cell(table, com):
#     r, c = com[1:]
#     r, c = int(r), int(c)

#     if table[r][c][0][0]:
#         return table[r][c][0][0]
#     else:
#         return 'EMPTY'

# def solution(commands):
#     answer = []
    
#     table = [[[[None], None] for _ in range(51)] for _ in range(51)]
#     for i in range(len(table)):
#         for j in range(len(table[0])):
#             table[i][j][1] = id(table[i][j][0])
    
#     for raw_com in commands:
#         com = raw_com.split(" ")
#         command = com[0]
        
#         if command == "UPDATE":
#             update_cell(table, com)
#         elif command == "MERGE":
#             merge_cell(table, com)
#         elif command == "UNMERGE":
#             unmerge_cell(table, com)
#         elif command == "PRINT":
#             answer.append(print_cell(table, com))

#     return answer