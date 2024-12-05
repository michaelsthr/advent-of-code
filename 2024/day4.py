import re


def count_xmax(mylist, regx1=r"XMAS", regx2=r"SAMX"):
    # from left -> right
    # from right -> left
    count = 0
    for line in mylist:
        xmas_list = re.findall(regx1, line)
        rev_xmas_list = re.findall(regx2, line)
        xmas_list.extend(rev_xmas_list)
        if xmas_list:
            count += len(xmas_list)
    return count


def transpose(mylist):
    # Switch row with col
    transposed_list = [""] * len(mylist[0])
    for line in mylist:
        for idx, char in enumerate(line):
            transposed_list[idx] += char
    return transposed_list


def transpose_by_diag(mylist):
    list1 = [""] * len(mylist[0])
    list2 = list1.copy()
    i = 0
    # one half
    for line in mylist:
        for idx, char in enumerate(line):
            if idx + i < len(line):
                list1[idx + i] += char
        i += 1
    # next half
    i = 0
    for line in reversed(mylist):
        for idx, char in enumerate(reversed(line)):
            if idx + i < len(line):
                list2[idx + i] += char
        i += 1
    combined_list = list1 + list2
    combined_list.pop()
    return combined_list


def search_by_shape(matrix):
    # Would actually be a far better solution for part1 aswell
    # Therefore the transpose stuff is not needed

    # X1 X2
    #   A
    # X3 X4
    max_count = 0
    for x in range(1, len(matrix) - 1, 1):
        for y in range(1, len(matrix[x]) - 1, 1):
            if matrix[x][y] == "A":
                x1 = matrix[x - 1][y - 1]
                x2 = matrix[x + 1][y - 1]
                x3 = matrix[x - 1][y + 1]
                x4 = matrix[x + 1][y + 1]
                count1 = count_xmax([x1 + "A" + x4], regx1=r"MAS", regx2=r"SAM")
                count2 = count_xmax([x2 + "A" + x3], regx1=r"MAS", regx2=r"SAM")
                if count1 > 0 and count2 > 0:
                    max_count += 1
    return max_count


if __name__ == "__main__":
    with open("2024/temp/input4.txt") as f:
        mylist = f.read().splitlines()

    count_by_shape = search_by_shape(mylist)

    transposed_text = transpose(mylist)
    diag_list = transpose_by_diag(mylist)
    diag_list2 = transpose_by_diag(mylist[::-1])

    print(
        "XMAS count:",
        count_xmax(mylist)
        + count_xmax(transposed_text)
        + count_xmax(diag_list)
        + count_xmax(diag_list2),
    )
    print("XMAS count by shape:", count_by_shape)
