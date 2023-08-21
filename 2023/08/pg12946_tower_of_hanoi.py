def solution(n):
    answer = []

    def move_disk(init, target):
        answer.append([init, target])

    def do_hanoi(init, target, n, via):
        if n == 1:
            move_disk(init, target)
        else:
            do_hanoi(init, via, n - 1, target)
            move_disk(init, target)
            do_hanoi(via, target, n - 1, init)

    do_hanoi(1, 3, n, 2)

    return answer