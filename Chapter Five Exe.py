with open("c.txt", "r") as country:
    z = country.read().splitlines()
    e = []
    f = []
    for i in z:
        if i.lower().startswith("a"):
            e.append(i)
        if i.lower().startswith("b"):
            f.append(i)

        with open("a.txt", "w") as a:
            for i in e:
                a.write(i+"\n")
        with open("b.txt", "w") as b:
            for q in f:
                b.write(q+"\n")

