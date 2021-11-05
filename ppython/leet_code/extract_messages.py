with open("output.txt") as ip, open("output1.txt", "w") as op:
    for ln in ip:
        # print(ln)
        if "//" not in ln:
            op.write(ln)
            continue
        msg_name = ln.split("//")[1].strip()
        op.write(msg_name + "\n")
