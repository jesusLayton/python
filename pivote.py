v_hueco = [1 << i for i in reversed(range(8))]

code = str(input())
traduccion = ""
while True:
    code = str(input()).strip()

    if code == "___________":
        if len(traduccion) > 0:
            print(traduccion)
        break

        # remove tape
    code = code[1:6] + code[7:-1]
    val = sum([v_hueco[i] for i, ch in enumerate(code) if ch == "o"])

    if val == 10 or val == 13:
        if len(traduccion) > 0:
            print(traduccion)
            traduccion = ""
        else:
            print()

    else:
        traduccion += chr(val)

