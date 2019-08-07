import sys

def mapka(inp,in_min,in_max,out_min,out_max): #Function use in WIRING code for Arduinos, scale number on one scale to another
    return (inp - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#a = int(sys.argv[1]) #Could be accesed via cmd line arguments
a = int(input("Numberos: "))
e = int(input("exponencos: "))

for x in range(a ** e):
    b = list((map(int, str(x))))
    #print("Printim b: ", b) #For debug
    cc = [""] *  (len(b)//2)
        #print(c)
    i = 0
    while(i<(len(b)-1)):
        cc[i//2] = str(b[i]) + str(b[i+1])

        i += 2
        #print(cc," i ",i)
    char_arr = [""] * len(cc)
    jmeno = ''
    for l in range(len(cc)):
        char_arr[l] = chr(int(mapka(int(cc[l]), 0, 99, 65, 122)))

    #    print(char_arr)

    print("Jmeno: ", jmeno.join(char_arr), " |char_arr| ", char_arr, " |x| ", x, "|b len|", len(b))
#    print(list(b))
#    print(b[0])
