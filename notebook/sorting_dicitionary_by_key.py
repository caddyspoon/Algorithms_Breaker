# 키의 값이 작은 순서대로 딕셔너리를 정렬하기
target_dict = {
    5: "five",
    3: "three",
    4: "four",
    1: "one",
    2: "two"
}
before_sorting = id(target_dict)

target_dict = dict(sorted(target_dict.items()))
print(target_dict)

after_sorting = id(target_dict)
print(before_sorting, after_sorting)

# 키가 정렬된 딕셔너리는 다른 딕셔너리이다.
print(before_sorting == after_sorting)