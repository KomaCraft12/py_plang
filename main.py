#PLANG 2.0
# PLANG OSZTÁLY

class Plang:
    def read_file(self,file_name):
        file = open(file_name,'r')
        file2 = []
        for sor in file:
            file2.append(sor)
        return file2
    def ha_feltetel(self,feltetel,variable):
        for z in range(0, len(variable)):
            feltetel = feltetel.replace(variable[z][0], variable[z][1])
            feltetel = feltetel.replace("\n","")
        return eval(feltetel)

    def plang_ki(self,row,variable):

        for x in range(0, len(variable)):
            if variable[x][0] in row:
                row = row.replace(variable[x][0], variable[x][1])
                row = row.replace("\n", "")
                row = row.replace("^", "**")
                for i in range(1,10):
                    row = row.replace(str(i)+"|",str(i)+")")
                row = row.replace("|","abs(")
                row = row.replace("DIV","//")
                row = row.replace("MOD","%")

        m = 0
        for elem in row:
            if elem in "+-*/":
                m += 1

        if m == 0:
            return str(row)
        else:
            return eval(row)

    def run(self,file):
        valtozok = []
        ki = ()
        if len(file) > 1:
            if "program" not in file[0]:
                print('Nincs megadva a program')
                exit()
            if "valtozok" not in file[1]:
                print('Nincsenek változok definiálva!')
                exit()
        else:
            print("Üres fájl!")

        ha = [0]
        for i in range(2,len(file)):
            #print(ha)
            if ":=" in file[i] and ha == "nem":
                valtozo = file[i].split(" := ")
                #print("változó értékadás")

                valtozok.append(valtozo)
                #print(valtozok)
            if "ki:" in file[i]:
                ki = str(file[i][4:])
                print(self.plang_ki(ki,valtozok))
            if "HA" in file[i] and "HA_VEGE" not in file[i]:
                feltetel = file[i]
                feltetel = feltetel.replace("HA","")
                feltetel = feltetel.replace("AKKOR","")
                feltetel = feltetel.replace("\n","")

                logikai = self.ha_feltetel(feltetel,valtozok)

                print(logikai)

                if logikai == True:
                    ha[0] = 1
                else:
                    ha[0] = 2
                print(ha)
            if "HA_VEGE":
                ha = "nem"
            if ha[0] == 1:
                print(1000)
                if ":=" in file[i]:
                    valtozo = file[i].split(" := ")
                    van = 0
                    for y in range(len(valtozok)):
                        if(valtozok[y][0] == valtozo[0]):
                            valtozok[y][1] = valtozo[1]
                            van = 1
                            break
                    print("Van: "+str(van))
                    if van == 0:
                        valtozok.append(valtozo)

                if "ki:" in file[i]:
                    ki = str(file[i][4:])
                    print(self.plang_ki(ki,valtozok))
            if ha == 2:
                #program
                ha = 0




#PLANG MEGHIVÁSA

plang = Plang()

file = input('Kérem a fájl nevét: ')
file = plang.read_file(file)
plang.run(file)
