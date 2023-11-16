from decimal2binario import decimal2binario
from table import symbols,comp,dest,jump

archivodestino = "./RectL.asm"
archivosalida = "RectL.hack"

with open(archivodestino) as file:
    i = 0
    for line in file:
        coment = line[slice(line.find("/"),-1)]
        line = line.replace(coment,"").strip()
        if(len(line) > 0):
            if(line[0] != "("):
                i += 1
            else:
                label = slice(line.find("(")+1,-1)
                symbols[line[label]] = decimal2binario(i)
        


with open(archivodestino) as file:
    memory = 16
    for line in file:
        coment = line[slice(line.find("/"),-1)]
        line = line.replace(coment,"").strip()
        if("@" in line):
            variable = line[slice(line.find("@")+1,len(line))]
            if(not (variable in symbols)):
                if(variable.isnumeric()):
                    symbols[variable] = decimal2binario(int(variable))
                else:
                    symbols[variable] = decimal2binario(memory)
                    memory += 1


with open(archivodestino) as file:
    hack = open(archivosalida,"x")
    for line in file:
        coment = line[slice(line.find("/"),len(line))]
        line = line.replace(coment,"").strip()
        if("@" in line):
            variable = line[slice(line.find("@")+1,len(line))]
            hack.write(symbols[variable]+"\n")
        if("=" in line):
            bin = "111"
            varcomp = line[slice(line.find("=")+1,len(line))]
            bin = bin + comp[varcomp]
            vardest = line[slice(0,line.find("="))]
            bin = bin + dest[vardest]
            bin = bin + jump["null"]
            hack.write(bin+"\n")
        if(";" in line):
            bin = "111"
            varcomp = line[slice(0,line.find(";"))]
            bin = bin + comp[varcomp]
            bin = bin + dest["null"]
            varjump = line[slice(line.find(";")+1,len(line))]
            bin = bin + jump[varjump]
            hack.write(bin+"\n")