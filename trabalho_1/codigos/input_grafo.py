
input = open("../as_graph.txt", "r")
n = 0

for line in input:
    #print(line)
    x = line.split(" ")
    try:
        x[1] = x[1].replace("\n", "")
    except:
        print(x[0])
        pass

    #print(y)

print("n = ", n)
print("x = ", x)
