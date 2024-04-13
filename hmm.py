h = {"a":0.2,"c":0.3,"g":0.3,"t":0.2,"h":0.5,"l":0.5}
l = {"a":0.3,"c":0.2,"g":0.2,"t":0.3,"l":0.6,"h":0.4}

startH = 0.5
startL = 0.5

pattern = "ggcactgaa"
     

hp = [0.5*h[pattern[0]]]
lp = [0.5*l[pattern[0]]]
     

for char in pattern[1:]:
    xh = h[char] * max(hp[-1]*h['h'] , lp[-1]*l['h'])
    xl = l[char] * max(hp[-1]*h['l'] , lp[-1]*l['l'])

    hp.append(xh)
    lp.append(xl)
     

print(hp, "\n", lp)
for i,j in zip(lp, hp):
    if i>=j:
        print("L", end='')
    else:
        print("H", end='')

#using log
h = {"a":-2.322,"c":-1.737,"g":-1.737,"t":-2.322,"h":-1,"l":-1}
l = {"a":-1.737,"c":-2.322,"g":-2.322,"t":-1.737,"l":-0.737,"h":-1.322}

startH = -1
startL = -1

pattern = "ggcactgaa"
     

hp = [startH + h[pattern[0]]]
lp = [startL + l[pattern[0]]]
     

for char in pattern[1:]:
    
    ha = h[char] + max(hp[-1] + h['h'], lp[-1] + l['h'])
    la = l[char] + max(hp[-1] + h['l'], lp[-1] + l['l'])

    hp.append(ha)
    lp.append(la)
     

for i,j in zip(hp, lp):

    if i>j:
        print("H", end = " ")
    else:
        print("L", end = " ")



#single layer perceptron
inst = [["mi",11,13],["mi",9,12],["mi",8.5,18],["mi",12,8],["mi",13,18],["a",18,5],["a",20,7.5]
     ,["a",16.5,6],["a",19,6.5],["a",12,9]]

w = [0.3, 0.6]
aplha = 0.0001 
     

w_next = []
while w!=w_next:
    w_next = w[:]
    for inp in inst:
        x = sum([i*j for i,j in zip(inp[1:], w)]) 
        print(f"--> x: {x}")

        if x > 0 and inp[0] != "mi":
            w = [round(i+ aplha*(-1)*j, 3) for i,j in zip(w, inp[1:])]
            print(f"Updated w: {w}")

        if x <0 and inp[0] != "a":
            w = [round(i+ aplha*(1)*j, 3) for i,j in zip(w, inp[1:])]
            print(f"Updated w: {w}")