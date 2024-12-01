import re

def read_input() -> list[str]:
    filename = "input.txt"
    with open(filename) as f:
        input_text = f.readlines()
    return input_text

def split_list(list: list) -> tuple:
    left_values: list = []
    right_values: list = []

    for line in list:
        splitted_line = re.split(pattern=r"\s", string=line, maxsplit=1)
        left_values.append(splitted_line[0].strip())
        right_values.append(splitted_line[1].strip())
    
    if len(left_values) != len(right_values):
        raise Exception("Lists have different lenghts!")
    
    return left_values, right_values

def part_one():
    input_text = read_input()
    left_values, right_values = split_list(input_text)

    left_values.sort()
    right_values.sort()

    distances: int = 0

    for idx in range(len(left_values)):
        distance = int(right_values[idx]) - int(left_values[idx])
        distances += abs(distance)
        print(f"{int(right_values[idx])} - {int(left_values[idx])} = {abs(distance)}", flush=True)

    print(f"total distance between list: {distances}")

def part_two():
    input_text = read_input()
    left_values, right_values = split_list(input_text)

    similarity_score: int = 0

    for lvalue in left_values:
        counter: int = 0
        for rvalue in right_values:
            if int(lvalue) == int(rvalue):
                counter += 1
        similarity = counter * int(lvalue)
        similarity_score += similarity

    print(f"total similarity_score: {similarity_score}")

if __name__ == "__main__":
    part_two()
