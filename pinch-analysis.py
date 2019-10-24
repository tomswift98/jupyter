approachTemp = 15

streams = [
    ['H34',      155.17,    150.00,     87318.05],
    ['HT102',    123.69,    113.12,    419998.57],
    ['CT103',    153.02,    154.55,  -9786183.07],
    ['C19',      106.27,    196.56,    -16984.30],
    ['C32',       88.59,    150.00,    -23944.55],
    ['H13',      330.86,    100.00,     26976.28],
    ['H14',      330.86,     95.00,     11535.45]]

streams = [list(x) for x in zip(*streams)] # invert matrix

Ts_n = [''] * len(streams[1])
Tt_n = [''] * len(streams[1])

for i in range(0, len(streams[1])):
    if streams[1][i] > streams[2][i]:
        Ts_n[i] = streams[1][i] - approachTemp
        Tt_n[i] = streams[2][i] - approachTemp
    else:
        Ts_n[i] = streams[1][i]
        Tt_n[i] = streams[2][i]
    i+=1
    
tempList = []

for i in range(len(Ts_n)):
    if Ts_n[i] not in(tempList):
        tempList.append(Ts_n[i])

for i in range(len(Tt_n)):
    if Tt_n[i] not in(tempList):
        tempList.append(Tt_n[i])
            
tempList.sort(reverse=True)

print(tempList)

crossTable =  [[0] * len(tempList) ] * 4
crossTable[2] = [''] * len(tempList)
crossTable[0] = tempList
names = [''] * len(tempList)

for i in range(0, len(crossTable[1])):
    for j in range(0, len(streams[1])):
        
        #brooks was here
        cond1 = (Ts_n[j] > Tt_n[j]) and (Ts_n[j] >= tempList[i]) and (Tt_n[j] < tempList[i])
        cond2 = (Tt_n[j] > Ts_n[j]) and (Tt_n[j] >= tempList[i]) and (Ts_n[j] < tempList[i])
        
        if cond1 or cond2:
            crossTable[1][i] += streams[3][j]
            names[i] += streams[0][j] + ' '
            #print(crossTable[0][i], '\t', streams[0][j], '\t', Ts_n[j], ' \t', Tt_n[j], '  \t', i, j, '\t', cond1, cond2)
        j += 1
    i += 1
    
dT = [0] * len(tempList)
dH = [0] * len(tempList)
H  = [0] * len(tempList)
Hs = [0] * len(tempList)

for i in range(1, len(dT)):
    dT[i-1] = crossTable[0][i-1] - crossTable[0][i]
    i+=1
    
for i in range(0, len(dT)):
    dH[i] = crossTable[1][i] * dT[i] 
    i+=1

H[0] = 0
for i in range(0, len(dT)-1):
    H[i+1] = H[i] + dH[i]     

mindex = H.index(min(H))
    
print("Pinch Temperature: ", tempList[mindex])

Hs[mindex] = 0

for i in range(mindex-1, -1, -1):
    Hs[i] = Hs[i+1] - dH[i]
    
for i in range(mindex+1, len(Hs)):
    Hs[i] = Hs[i-1] + dH[i-1]
    
print("Minimum Hot Utility: ", Hs[0])
print("Minimum Hot Utility: ", Hs[-1])
