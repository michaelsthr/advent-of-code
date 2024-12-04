import re


def find_xmax(mylist):
    # from left -> right and right -> left
    count = 0
    for line in mylist:
        xmas_list = re.findall(r"XMAS", line)
        rev_xmas_list = re.findall(r"SAMX", line)
        xmas_list.extend(rev_xmas_list)
        if xmas_list:
            count += len(xmas_list)
    return count


def transpose(mylist):
    transposed_list = [""] * len(mylist[0])
    for line in mylist:
        for idx, char in enumerate(line):
            transposed_list[idx] += char
    return transposed_list


def diag_to_list(mylist):
    list1 = [""] * len(mylist[0])
    i = 0
    for col, line in enumerate(mylist):
        for idx, char in enumerate(line):
            if idx + i < len(line):
                list1[idx + i] += char
        i += 1

    list2 = [""] * len(mylist[0])
    i = 0
    for col, line in enumerate(reversed(mylist)):
        for idx, char in enumerate(reversed(line)):
            if idx + i < len(line):
                list2[idx + i] += char
        i += 1
    combined_list = list1 + list2
    combined_list.pop()
    print(combined_list)
    return combined_list


with open("2024/temp/input4.txt") as f:
    mylist = f.read().splitlines()

transposed_text = transpose(mylist)

diag_list = diag_to_list(mylist)
mylist = mylist[::-1]
diag_list2 = diag_to_list(mylist)

xmas_count_1 = find_xmax(mylist)
xmas_count_2 = find_xmax(transposed_text)
xmas_count_3 = find_xmax(diag_list)
xmas_count_4 = find_xmax(diag_list2)

print(xmas_count_1)
print(xmas_count_2)
print(xmas_count_3)
print(xmas_count_4)
print("XMAS count:", xmas_count_1 + xmas_count_2 + xmas_count_3 + xmas_count_4)
