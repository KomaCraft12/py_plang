#PLANG 2.0
# PLANG OSZTÁLY

class Plang:
    def read_file(self,file_name):
        my_file = open(file_name,'r')
        file2 = []
        for sor in my_file:
            file2.append(sor)
        return file2
    def ha_feltetel(self,feltetel,variable):
        feltetel = feltetel.replace("ha", "")
        feltetel = feltetel.replace("akkor", "")
        feltetel = feltetel.replace("\n", "")
        feltetel = feltetel.replace("^", "**")
        for i in range(1,10):
            feltetel = feltetel.replace(str(i)+"|",str(i)+")")
        feltetel = feltetel.replace("|","abs(")
        feltetel = feltetel.replace("DIV","//")
        feltetel = feltetel.replace("MOD","%")

        for z in range(0, len(variable)):
            feltetel = feltetel.replace(variable[z][0], variable[z][1])
            feltetel = feltetel.replace("\n","")
        return eval(feltetel)
    def ciklus_feltetel(self,feltetel,variable):

        feltetel = feltetel.replace("ciklus", "")
        feltetel = feltetel.replace("amig", "")
        feltetel = feltetel.replace("\n", "")
        feltetel = feltetel.replace("^", "**")
        for i in range(1,10):
            feltetel = feltetel.replace(str(i)+"|",str(i)+")")
        feltetel = feltetel.replace("|","abs(")
        feltetel = feltetel.replace("DIV","//")
        feltetel = feltetel.replace("MOD","%")

        for z in range(0, len(variable)):
            feltetel = feltetel.replace(str(variable[z][0]), str(variable[z][1]))
            feltetel = feltetel.replace("\n","")
        return eval(feltetel)
    def muvelet(self,row,variable):

        for x in range(0, len(variable)):
            if variable[x][0] in row:
                row = row.replace(str(variable[x][0]), str(variable[x][1]))

        row = row.replace("\n", "")
        row = row.replace("^", "**")
        for i in range(1,10):
            row = row.replace(str(i)+"|",str(i)+")")
        row = row.replace("|","abs(")
        row = row.replace("DIV","//")
        row = row.replace("MOD","%")

        return int(eval(row))

    def plang_ki(self,row,variable):

        for x in range(0, len(variable)):
            if variable[x][0] in row:
                row = row.replace(str(variable[x][0]), str(variable[x][1]))

        row = row.replace("\n", "")
        row = row.replace("^", "**")
        for i in range(1,10):
            row = row.replace(str(i)+"|",str(i)+")")
        row = row.replace("|","abs(")
        row = row.replace("DIV","//")
        row = row.replace("MOD","%")

        return eval(row)

    def run(self,file):
        valtozok = []
        if len(file) > 1:
            if "program" not in file[0]:
                print('Nincs megadva a program')
                exit()
            else:
                name = file[0]
                name = name.replace("program","")
                name = name.replace("\n","")
                if name == "":
                    print("Program neve nem lehet üres!")
                    exit()

            if "valtozok" not in file[1]:
                print('Nincsenek változok definiálva!')
                exit()
        else:
            print("Üres fájl!")

        ha = 0
        kulonben = 0
        ciklus = 0
        ciklus_i = 0
        cfelt = ""
        global i
        i = 2
        while i < len(file):
            #print(ha)
            if ":=" in file[i] and ha == 0 and ciklus == 0:
                valtozo = file[i].split(" := ")
                #print("változó értékadás")

                seged = valtozo[1]
                seged = seged.replace("\n","")
                valtozo[1] = seged

                valtozok.append(valtozo)

                #print(valtozok)

            if "be:" in file[i]:
                be = str(file[i][4:])
                be = be.replace("\n","")
                inp = input()
                valtozo = [be,inp]
                #print(valtozo)
                valtozok.append(valtozo)
            if "ki:" in file[i]:
                ki = str(file[i][4:])
                print(self.plang_ki(ki,valtozok))
        # HA
            if "ha" in file[i] and "ha_vege" not in file[i]:
                feltetel = file[i]

                logikai = self.ha_feltetel(feltetel,valtozok)

                #print(logikai)

                if logikai == True:
                    ha = 1
                else:
                    ha = 2
                    kulonben = 1
                #print(ha)
            if "ha_vege" in file[i]:
                ha = 0
            if ha == 1 and kulonben == 0:
                if ":=" in file[i]:
                    valtozo = file[i].split(" := ")
                    van = 0
                    for y in range(len(valtozok)):
                        if(valtozok[y][0] == valtozo[0]):
                            valtozok[y][1] = valtozo[1]
                            van = 1
                            break
                    if van == 0:
                        valtozok.append(valtozo)

                if "ki:" in file[i]:
                    ki = str(file[i][4:])
                    print(self.plang_ki(ki,valtozok))
            if ha == 1 and kulonben == 0 and "kulonben" in file[i]:
                kulonben = -1
            if ha == 2 and kulonben == 1 and "kulonben" in file[i]:
                ha = 1
                kulonben = 0

        # CIKLUS
            #print("Ciklus: "+str(ciklus))
            #print("I: "+str(i))
            if "ciklus" in file[i] and "ciklus_vege" not in file[i]:
                ciklus_i = i
                ciklus = 1
                cfelt = file[i]
                #print(cfelt)
            if ciklus == 1:
                #print(self.ciklus_feltetel(cfelt,valtozok))
                if self.ciklus_feltetel(cfelt,valtozok):
                    if ":=" in file[i]:
                        valtozo = file[i].split(" := ")
                        ertek = self.muvelet(valtozo[1],valtozok)
                        #print(ertek)
                        for y in range(len(valtozok)):
                            if (valtozok[y][0] == valtozo[0]):
                                valtozok[y][1] = ertek
                        #print(valtozok)
                    if "ki:" in file[i]:
                        ki = str(file[i][4:])
                        print(self.plang_ki(ki,valtozok))
            if "ciklus_vege" in file[i]:
                if self.ciklus_feltetel(cfelt, valtozok):
                    i = ciklus_i-1
                else:
                    ciklus = 0
            i = i+1
#PLANG MEGHIVÁSA

plang = Plang()

#file = input('Kérem a fájl nevét: ')
file = "teszt.plang"
file = plang.read_file(file)
plang.run(file)
