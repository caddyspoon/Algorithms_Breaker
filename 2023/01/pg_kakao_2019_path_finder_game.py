import sys
sys.setrecursionlimit(10 ** 3)

from collections import deque

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    node_deque_pre = deque()
    node_deque_post = deque()
    for node in nodeinfo:
        node_deque_pre.append(node)
        node_deque_post.append(node)

    pre_result = []

    def preorder(node_deque_pre):
        nonlocal pre_result

        parent_node = node_deque_pre.popleft()
        px, py, pv = parent_node

        pre_result.append(pv)

        left_arr = deque()
        right_arr = deque()

        while node_deque_pre:
            child_node = node_deque_pre.popleft()
            cx = child_node[0]

            if cx < px:
                left_arr.append(child_node)

            else:
                right_arr.append(child_node)

        if left_arr:
            preorder(left_arr)
        if right_arr:
            preorder(right_arr)

    post_result = deque()

    def postorder(node_deque_post):
        nonlocal post_result

        parent_node = node_deque_post.popleft()
        px, py, pv = parent_node

        post_result.appendleft(pv)

        left_arr = deque()
        right_arr = deque()

        while node_deque_post:
            child_node = node_deque_post.popleft()
            cx = child_node[0]

            if cx < px:
                left_arr.append(child_node)

            else:
                right_arr.append(child_node)

        if right_arr:
            postorder(right_arr)
        if left_arr:
            postorder(left_arr)


    preorder(node_deque_pre)
    postorder(node_deque_post)

    post_result_list = list(post_result)

    return [pre_result, post_result_list]