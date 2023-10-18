def solution(triangle):
    l = len(triangle)

    dp = [[] for _ in range(l)]
    dp[0].append(triangle[0][0])

    def make_pyramid(floor=1):
        if floor == l:
            return

        dp[floor] = [0] * (floor + 1)

        for idx, crnt_value in enumerate(dp[floor - 1]):
            next_node_origin_value_left = dp[floor][idx]
            next_node_origin_value_right = dp[floor][idx + 1]

            # 왼쪽 값 채우기
            dp[floor][idx] = max(next_node_origin_value_left,
                                 crnt_value + triangle[floor][idx])
            # 오른쪽 값 채우기
            dp[floor][idx + 1] = max(next_node_origin_value_right,
                                     crnt_value + triangle[floor][idx + 1])

        make_pyramid(floor + 1)

    make_pyramid()

    return max(dp[l-1])