def read_input():
    return input()

def checker(inp_str):
    flag = 0
    for i in list(inp_str):
        if flag == 0:
            if i == "C":
                flag = 1
        if flag == 1:
            if i == "F":
                flag = 2

    if flag == 2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    checker(read_input())
