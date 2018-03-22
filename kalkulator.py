def kalkulator(inp):
    chars = list(inp)

    def check_num(num):
        try:
            int(num)
            return True
        except:
            return False
    def get_indexes(l, e):
        indexes = []
        for i in range(len(l)):
            if l[i] == e:
                indexes.append(i)
        return indexes

    er_tall = [check_num(i) for i in chars]
    if not er_tall[0]:
        er_tall = [True] + er_tall
        chars = [0] + chars

    nums = []
    tegn = []
    for i in range(len(chars)):
        if er_tall[i]:
            if i > 0:
                if er_tall[i-1]:
                    nums[len(nums)-1] = int(str(nums[len(nums)-1]) + chars[i])
                else:
                    nums.append(int(chars[i]))
            else:
                nums.append(int(chars[i]))
        else:
            tegn.append(chars[i])

    pa = get_indexes(tegn, "(")
    po = get_indexes(tegn, ")")
    if not len(pa) == len(po):
        return "IKKE BRA PARANTES!!!"
    else:
         while len(pa) > 0:
             tegnene = [tegn[i] for i in range(pa[0] + 1, po[len(po)-1])]
             numrene = [nums[i] for i in range(pa[0], po[len(po)-1])]
             

    d = get_indexes(tegn, "/")
    while len(d) > 0:
        place = d[0]
        num1 = nums[place]
        num2 = nums[place+1]
        nums.pop(place)
        tegn.pop(d[0])
        nums[place] = num1 / num2
        d = get_indexes(tegn, "/")

    g = get_indexes(tegn, "*")
    while len(g) > 0:
        place = g[0]
        num1 = nums[place]
        num2 = nums[place+1]
        nums.pop(place)
        tegn.pop(g[0])
        nums[place] = num1 * num2
        g = get_indexes(tegn, "*")

    m = get_indexes(tegn, "-")
    while len(m) > 0:
        place = m[0]
        num1 = nums[place]
        num2 = nums[place+1]
        nums.pop(place)
        tegn.pop(m[0])
        nums[place] = num1 - num2
        m = get_indexes(tegn, "-")

    p = get_indexes(tegn, "+")
    while len(p) > 0:
        place = p[0]
        num1 = nums[place]
        num2 = nums[place+1]
        nums.pop(place)
        tegn.pop(p[0])
        nums[place] = num1 + num2
        p = get_indexes(tegn, "+")

print(kalkulator(input()))