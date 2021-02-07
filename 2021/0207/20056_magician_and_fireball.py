import sys
sys.stdin = open('20056.txt', "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 좌표 값이 1~N을 벗어나는 체크해주는 함수
def is_out(x):
    if x < 1 or x > N:
        return True
    return False

# 넘어갔다면 1~N안으로 넣어줍니다!!
# 1과 N은 연결되어있으니까 N만큼 더해주거나 빼누는 과정을 반복하면 지금의 위치로 오겠죠 ^^
def relocation(x):
    if x < 1:
        while x < 1:
            x += N
        return x
    else:
        while x > N:
            x -= N
        return x

"""
첫째 줄에 N, M, K가 주어진다.
둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.
"""

for case in range(1, int(input())+1):
    N, M_raw, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M_raw)]

    T = 0

    # K번까지 시행!
    while T != K:
        # 현재 파이어볼의 위치를 넣어줄 딕셔너리
        crn_dict = {}

        # 원래 데이터가 제공되는 배열
        while arr:
            r, c, m, s, d = arr.pop()

            nr = r + dx[d] * s
            nc = c + dy[d] * s

            # 새로운 파이어볼의 위치가 1~N이 아니라면 확인 후 조정해서 넣어줍니다.
            if is_out(nr):
                nr = relocation(nr)
            if is_out(nc):
                nc = relocation(nc)

            # 현재 시행에서 둘로 나누어주기 전!
            # 전 비어있는 이중 리스트로 하나씩 넣어서 하기는 메모리 낭비고 귀찮아서
            # r_c를 키로 하는 딕셔너리를 만들어서 각 질량/속도/위치 정보를 넣어줬어요

            # 참고 사항이지만, 비어있는 리스트는 생성시 생각보다 많은 시간이 투자됩니다.
            # 주의하시길
            dkey = str(nr) + '_' + str(nc)

            # 키 오류가 안나는 try면 이미 다른 파이어볼이 존재하는 칸, 아니면 비어있는 칸이므로 except로 넣어줍니다.
            try:
                crn_dict[dkey].append([m, s, d])
            except:
                crn_dict[dkey] = [[m, s, d]]

        # 현 시행이 끝났으므로 딕셔너리를 검사해서 두 개 이상이 같은 칸에 존재하는 파이어볼을 찾아볼까요?
        for key in crn_dict:
            # 키값을 분해해서 다시 수치로 넣어주고요
            r, c = map(str, key.split('_'))
            r = int(r)
            c = int(c)
        
            # 두 개 이상 존재하는 파이어볼을 합쳐줍시다! >_<
            if len(crn_dict[key]) >= 2:
                nm = 0
                ns = 0
                # 해당 나머지는 홀수/짝수를 검사를 도와줄 친구에요
                nameoji = -1
                # 해당 플래그는 앞서 나온 방향이 홀수/짝수로 서로 다를 때 체크해주는 플래그에요!
                nd_flag = 0

                """
                질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
                속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
                합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                질량이 0인 파이어볼은 소멸되어 없어진다.
                """

                for cm, cs, cd in crn_dict[key]:
                    nm += cm
                    ns += cs

                    # 여태까지 모두 홀수 혹은 짝수였을 경우, 지금도 그런지 확인해줍니다.
                    if not nd_flag:
                        # 현재 방향을 2로 나눈 나머지 값이구요
                        cnameoji = cd % 2
                        # 나머지가 -1이면 첫 시행이니까 그냥 현재 나머지를 확인 나머지에 넣어주고
                        if nameoji == -1:
                            nameoji = cnameoji
                        # 그렇지 않으면, 현재 나머지가 지난 나머지와 같은지 확인!
                        else:
                            # 근데 나머지 값이 0과 1로 나와 다르다면
                            if cnameoji != nameoji:
                                # 짝수, 홀수가 혼합된 경우이므로 플래그 체크!
                                nd_flag = 1
                nm //= 5
                if nm:
                    ns //= len(crn_dict[key])
                    
                    for i in range(4):
                        nd = 2*i

                        if nd_flag:
                            nd += 1
                        # 모두 넣어줍니다.
                        arr.append([r, c, nm, ns, nd])
            else:
                # 얜 그냥 하나니까 넣어주는 얘구요
                arr.append([r, c, crn_dict[key][0][0], crn_dict[key][0][1], crn_dict[key][0][2]])
        T += 1

    answer = 0
    
    if arr:
        for elm in arr:
            answer += elm[2]

    print(f'#{case} {answer}')