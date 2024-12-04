import re

def count_xmax(mylist):
    # from left -> right 
    # from right -> left
    count = 0
    for line in mylist:
        xmas_list = re.findall(r"XMAS", line)
        rev_xmas_list = re.findall(r"SAMX", line)
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

if __name__ == "__main__":
    with open("2024/temp/input4.txt") as f:
        mylist = f.read().splitlines()

    transposed_text = transpose(mylist)
    diag_list = transpose_by_diag(mylist)
    diag_list2 = transpose_by_diag(mylist[::-1])

    print("XMAS count:", count_xmax(mylist) + count_xmax(transposed_text) + count_xmax(diag_list) + count_xmax(diag_list2))
