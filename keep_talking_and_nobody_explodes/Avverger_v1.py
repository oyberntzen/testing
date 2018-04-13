class Avverger:
    def __init__(self, serie_nummer, lyste_indikatorer, batterier, parallellport):
        self.ser = serie_nummer
        self.ind = lyste_indikatorer
        self.bat = batterier
        self.par = parallellport

    def ledninger(self, ledninger):
        if len(ledninger) == 3:
            if not "roed" in ledninger:
                return 2
            elif ledninger[2] == "hvit":
                return 3
            elif len(indekser(ledninger, "blaa")) > 1:
                return indekser(ledninger, "blaa")[len(indekser(ledninger, "blaa")) - 1] + 1
            else:
                return 3
        elif len(ledninger) == 4:
            if len(indekser(ledninger, "roed")) > 1 and \
                not int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2):
                return indekser(ledninger, "roed")[len(indekser(ledninger, "roed")) - 1] + 1
            elif (ledninger[3] == "gul" and \
                not "roed" in ledninger) or \
                len(indekser(ledninger, "blaa")) == 1:
                return 1
            elif len(indekser(ledninger, "gul")) > 1:
                return 4
            else:
                return 2
        elif len(ledninger) == 5:
            if ledninger[4] == "svart" and \
                not int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2):
                return 4
            elif len(indekser(ledninger, "roed")) == 1 and \
                len(indekser(ledninger, "gul")) > 1:
                return 1
            elif len(indekser(ledninger, "svart")) == 0:
                return 2
            else:
                return 1
        elif len(ledninger) == 6:
            if len(indekser(ledninger, "gul")) == 0 and \
                not int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2):
                return 3
            elif len(indekser(ledninger, "gul")) == 1 and \
                len(indekser(ledninger, "hvit")) > 1:
                return 4
            elif len(indekser(ledninger, "roed")) == 0:
                return 6
            else:
                return 4

    def knapp(self, tekst, farge):
        """False: trykk og slipp kjapt. True: trykk og gjoer slipping"""
        if tekst == "Abort" and farge == "blaa":
            return True
        elif self.bat > 1 and tekst == "Detonate":
            return False
        elif farge == "hvit" and "CAR" in self.ind:
            return True
        elif (self.bat > 2 and "FRK" in self.ind) or \
            (farge == "roed" and tekst == "Hold"):
            return False
        return True

    def symboler(self, tegn):
        """0:Ϙ, 1:ƛ, 2:Ѭ, 3:ϗ, 4:Ͽ, 5:Ѧ, 6:Ӭ, 7:Ҩ, 8:☆, 9:¿, 10:©, 11:Ѽ, 12:Җ, 13:Ԇ, 14:ƀ, 15:б, 16:¶, ټ:17, l8:Ͼ, 19:Ѯ, 20:★, 21:Ψ, 22:҂, 23:æ, 24:Ҋ, 25:Ω, 26:Ϟ"""
        rekker = [[0, 5, 1, 26, 2, 3, 4], 
                  [6, 0, 4, 7, 8, 3, 9], 
                  [10, 11, 7, 12, 13, 1, 17], 
                  [15, 16, 14, 2, 12, 9, 17], 
                  [21, 17, 14, 18, 16, 19, 20],
                  [15, 6, 22, 23, 21, 24, 25]]

        rekke = 0
        for i in range(len(rekker)):
            riktig = True
            for j in tegn:
                if not j in rekker[i]:
                    riktig = False
                    break
            if riktig:
                rekke = i
                break
        
        rekkefoelge = []
        for j in range(4):
            rekord = 0
            for i in range(len(tegn)):
                if indekser(rekker[rekke], tegn[i])[0] < indekser(rekker[rekke], tegn[rekord])[0]:
                    rekord = i
            rekkefoelge.append(tegn[rekord])
            tegn.pop(rekord)
        return rekkefoelge

    def simon_sier(self, farge, feil):
        tabell = { True : {
                0 : { "roed" : "blaa", "blaa" : "roed", "groenn" : "gul", "gul" : "groenn" },
                1 : { "roed" : "gul", "blaa" : "groenn", "groenn" : "blaa", "gul" : "roed" },
                2 : { "roed" : "groenn", "blaa" : "roed", "groenn" : "gul", "gul" : "blaa" }
            }, False: {
                0 : { "roed" : "blaa", "blaa" : "gul", "groenn" : "groenn", "gul" : "roed" },
                1 : { "roed" : "roed", "blaa" : "blaa", "groenn" : "gul", "gul" : "groenn" },
                2 : { "roed" : "gul", "blaa" : "groenn", "groenn" : "blaa", "gul" : "roed" }
                }}

        vokaler = "AEIOUY"
        har = False
        for i in self.ser:
            if i in vokaler:
                har = True
                break
        return tabell[har][feil][farge]

    def hvem_er_paa_foerst(self, skjerm, knapper):
        """oppe til venstre: 0, midten til venstre: 1, nede til venstre: 2, oppe til høyre: 3, midten til høyre: 4, nede til høyre: 5"""
        tabell = { "YES" : 1, "FIRST" : 3, "DISPLAY" : 5, "OKAY" : 3, "SAYS" : 5, "NOTHING" : 1, 
                  "" : 2, "BLANK" : 4, "NO" : 5, "LED" : 1, "LEAD" : 5, "READ" : 4,
                  "RED" : 4, "REED" : 2, "LEED" : 2, "HOLD ON" : 5, "YOU" : 4, "YOU ARE" : 5,
                  "YOUR" : 4, "YOU'RE" : 4, "UR" : 0, "THERE" : 5, "THEY'RE" : 2, "THEIR" : 4,
                  "THEY ARE" : 1, "SEE" : 5, "C" : 3, "CEE" : 5 }
        maal = knapper[tabell[skjerm]]
        
        ord = { 
            "READY" : ["YES", "OKAY", "WHAT", "MIDDLE", "LEFT", "PRESS", "RIGHT", "BLANK", "READY"],
            "FIRST" : ["LEFT", "OKAY", "YES", "MIDDLE", "NO", "RIGHT", "NOTHING", "UHHH", "WAIT", "READY", "BLANK", "WHAT", "PRESS", "FIRST"],
            "NO" : ["BLANK", "UHHH", "WAIT", "FIRST", "WHAT", "READY", "RIGHT", "YES", "NOTHING", "LEFT", "PRESS", "OKAY", "NO"],
            "BLANK" : ["WAIT", "RIGHT", "OKAY", "MIDDLE", "BLANK"],
            "NOTHING" : ["UHHH", "RIGHT", "OKAY", "MIDDLE", "YES", "BLANK", "NO", "PRESS", "LEFT", "WHAT", "WAIT", "FIRST", "NOTHING"],
            "YES" : ["OKAY", "RIGHT", "UHHH", "MIDDLE", "FIRST", "WHAT", "PRESS", "READY", "NOTHING", "YES"],
            "WHAT" : ["UHHH", "WHAT"],
            "UHHH" : ["READY", "NOTHING", "LEFT", "WHAT", "OKAY", "YES", "RIGHT", "NO", "PRESS", "BLANK", "UHHH"],
            "LEFT" : ["RIGHT", "LEFT"],
            "RIGHT" : ["YES", "NOTHING", "READY", "PRESS", "NO", "WAIT", "WHAT", "RIGHT"],
            "MIDDLE" : ["BLANK", "READY", "OKAY", "WHAT", "NOTHING", "PRESS", "NO", "WAIT", "LEFT", "MIDDLE"],
            "OKAY" : ["MIDDLE", "NO", "FIRST", "YES", "UHHH", "NOTHING", "WAIT", "OKAY"],
            "WAIT" : ["UHHH", "NO", "BLANK", "OKAY", "YES", "LEFT", "FIRST", "PRESS", "WHAT", "WAIT"],
            "PRESS" : ["RIGHT", "MIDDLE", "YES", "READY", "PRESS"],
            "YOU" : ["SURE", "YOU ARE", "YOUR", "YOU'RE", "NEXT", "UH HUH", "UR", "HOLD", "WHAT?"", ""YOU"],
            "YOU ARE" : ["YOUR", "NEXT", "LIKE", "UH HUH", "WHAT?", "DONE", "UH UH", "HOLD", "YOU", "U", "YOU'RE", "SURE", "UR", "YOU ARE"],
            "YOUR" : ["UH UH", "YOU ARE", "UH HUH", "YOUR"],
            "YOU'RE" : ["YOU", "YOU'RE"],
            "UR" : ["DONE", "U", "UR"],
            "U" : ["UH HUH", "SURE", "NEXT", "WHAT?", "YOU'RE", "UR", "UH UH", "DONE", "U"],
            "UH HUH" : ["UH HUH"],
            "UH UH" : ["UR", "U", "YOU ARE", "YOU'RE", "NEXT", "UH UH"],
            "WHAT?" : ["YOU", "HOLD", "YOU'RE", "YOUR", "U", "DONE", "UH UH", "LIKE", "YOU ARE", "UH HUH", "UR", "NEXT", "WHAT?"],
            "DONE" : ["SURE", "UH HUH", "NEXT", "WHAT?", "YOUR", "UR", "YOU'RE", "HOLD", "LIKE", "YOU", "U", "YOU ARE", "UH UH", "DONE"],
            "NEXT" : ["WHAT?", "UH HUH", "UH UH", "YOUR", "HOLD", "SURE", "NEXT"],
            "HOLD" : ["YOU ARE", "U", "DONE", "UH UH", "YOU", "UR", "SURE", "WHAT?", "YOU'RE", "NEXT", "HOLD"],
            "SURE" : ["YOU ARE", "DONE", "LIKE", "YOU'RE", "YOU", "HOLD", "UH HUH", "UR", "SURE"],
            "LIKE" : ["YOU'RE", "NEXT", "U", "UR", "HOLD", "DONE", "UH UH", "WHAT?", "UH HUH", "YOU", "LIKE"]
            }
        liste = ord[maal]

        for i in liste:
            for j in knapper:
                if j == i:
                    return j
    def hukommelse(self, steg, skjerm, knapper, trekk = None):
        if not trekk:
            trekk = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]

        stegene = {
            1 : {
                1 : [knapper[1], 1],
                2 : [knapper[1], 1],
                3 : [knapper[2], 2],
                4 : [knapper[3], 3]
                },
            2 : {
                1 : [4, indekser(knapper, 4)[0]],
                2 : [knapper[trekk[0][1]], trekk[0][1]],
                3 : [knapper[0], 0],
                4 : [knapper[trekk[0][1]], trekk[0][1]]
                },
            3 : {
                1 : [trekk[1][0], indekser(knapper, trekk[1][0])[0]],
                2 : [trekk[0][0], indekser(knapper, trekk[0][0])[0]],
                3 : [knapper[2], 2],
                4 : [4, indekser(knapper, 4)[0]]
                },
            4 : {
                1 : [knapper[trekk[0][1]], trekk[0][1]],
                2 : [knapper[0], 0],
                3 : [knapper[trekk[1][1]], trekk[1][1]],
                4 : [knapper[trekk[1][1]], trekk[1][1]]
                },
            5 : {
                1 : [trekk[0][0], indekser(knapper, trekk[0][0])[0]],
                2 : [trekk[1][0], indekser(knapper, trekk[1][0])[0]],
                3 : [trekk[3][0], indekser(knapper, trekk[3][0])[0]],
                4 : [trekk[2][0], indekser(knapper, trekk[2][0])[0]]
                }
            }
        trekk[steg - 1] = stegene[steg][skjerm]
        return trekk

    def morse_kode(self, kode):
        ord = {
            ".-" : "a",
            "-..." : "b",
            "-.-." : "c",
            "-.." : "d",
            "." : "e",
            "..-." : "f",
            "--." : "g",
            "...." : "h",
            ".." : "i",
            ".---" : "j",
            "-.-" : "k",
            ".-.." : "l",
            "--" : "m",
            "-." : "n",
            "---" : "o",
            ".--." : "p",
            "--.-" : "q",
            ".-." : "r",
            "..." : "s",
            "-" : "t",
            "..-" : "u",
            "..._" : "v",
            ".--" : "w",
            "-..-" : "x",
            "-.--" : "y",
            "--.." : "z"
            }

        splittet = kode.split(" ")
        resultat = ""
        for i in splittet:
            resultat += ord[i]
        
        frekvens = {
            "shell" : 3.505,
            "halls" : 3.515,
            "slick" : 3.522,
            "trick" : 3.532,
            "boxes" : 3.535,
            "leaks" : 3.542,
            "strobe" : 3.545,
            "bistro" : 3.552,
            "flick" : 3.555,
            "bombs" : 3.565,
            "break" : 3.572,
            "brick" : 3.575,
            "steak" : 3.582,
            "sting" : 3.592,
            "vector" : 3.595,
            "beats" : 3.600
            }
        return frekvens[resultat]

    def kompliserte_ledninger(self, roed, blaa, stjerne, lampe):
        regler = {
            False : {
                False : { 
                    False : { 
                        False : True, 
                        True : False }, 
                    True : { 
                        False : True, 
                        True : self.bat > 1 } },
                True : { 
                    False : { 
                        False : int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2),
                        True : self.par },
                    True : {
                        False : False,
                        True : self.par } } },
            True : {
                False : {
                    False : {
                        False : int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2),
                        True : self.bat > 1 },
                    True : {
                        False : True,
                        True : self.bat > 1 } },
                True : {
                    False : {
                        False : int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2),
                        True : int(self.ser[len(self.ser) - 1]) / 2 == int(int(self.ser[len(self.ser) - 1]) / 2) },
                    True : {
                        False : self.par,
                        True : False } } } }

        return regler[roed][blaa][stjerne][lampe]

    def lednings_sekvenser(self, farge, bokstav, trekk = None):
        if not trekk:
            trekk = [0, 0, 0]

        regler = {
            "roed" : {
                0 : bokstav == "C",
                1 : bokstav == "B",
                2 : bokstav == "A",
                3 : bokstav in ["A", "C"],
                4 : bokstav == "B",
                5 : bokstav in ["A", "C"],
                6 : True,
                7 : bokstav in ["A", "B"],
                8 : bokstav == "B"
                },
            "blaa" : {
                0 : bokstav == "B",
                1 : bokstav in ["A", "C"],
                2 : bokstav == "B",
                3 : bokstav == "A",
                4 : bokstav == "B",
                5 : bokstav in ["B", "C"],
                6 : bokstav == "C",
                7 : bokstav in ["A", "C"],
                8 : bokstav == "A"
                },
            "svart" : {
                0 : True,
                1 : bokstav in ["A", "C"],
                2 : bokstav == "B",
                3 : bokstav in ["A", "C"],
                4 : bokstav == "B",
                5 : bokstav in ["B", "C"],
                6 : bokstav in ["A", "B"],
                7 : bokstav == "C",
                8 : bokstav == "C"
                }
            }

        if farge == "roed":
            trekk[0] += 1
            return regler[farge][trekk[0] - 1], trekk
        elif farge == "blaa":
            trekk[1] += 1
            return regler[farge][trekk[1] - 1], trekk
        elif farge == "svart":
            trekk[2] += 1
            return regler[farge][trekk[2] - 1], trekk
        return None

    def labyrint(self, sirkelx, sirkely, spillerx, spillery, maalx, maaly):
        if (sirkelx == 1 and sirkely == 2) or (sirkelx == 6 and sirkely == 3):
            l = 0
        elif (sirkelx == 2 and sirkely == 4) or (sirkelx == 5 and sirkely == 2):
            l = 1
        elif (sirkelx == 4 and sirkely == 4) or (sirkelx == 6 and sirkely == 4):
            l = 2
        elif (sirkelx == 1 and sirkely == 1) or (sirkelx == 1 and sirkely == 4):
            l = 3
        elif (sirkelx == 4 and sirkely == 6) or (sirkelx == 5 and sirkely == 3):
            l = 4
        elif (sirkelx == 5 and sirkely == 1) or (sirkelx == 3 and sirkely == 5):
            l = 5
        elif (sirkelx == 2 and sirkely == 1) or (sirkelx == 2 and sirkely == 6):
            l = 6
        elif (sirkelx == 4 and sirkely == 1) or (sirkelx == 3 and sirkely == 4):
            l = 7
        elif (sirkelx == 1 and sirkely == 5) or (sirkelx == 3 and sirkely == 2):
            l = 8
        else:
            return
        labyrinter = [
               [#P1 V P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 1
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 2
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 3
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 4
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 6
                ],
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 1
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 2
                [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 3
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 4
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], #punkt 1
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], #vegger
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], #punkt 2
                [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], #vegger
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], #punkt 3
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #vegger
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], #punkt 4
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], #punkt 5
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #punkt 1
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], #punkt 2
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 3
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 4
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 1
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #punkt 2
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 3
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0], #punkt 4
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 1
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #vegger
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], #punkt 2
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #vegger
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], #punkt 3
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0], #punkt 4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #vegger
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], #punkt 5
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0], #vegger
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 1
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 2
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 3
                [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], #vegger
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], #punkt 4
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], #punkt 1
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 2
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], #punkt 3
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #punkt 4
                [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1], #vegger
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], #punkt 5
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1], #vegger
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 6
                ], 
               [#P1 V  P2 V  P3 V  P4 V  P5 V  P6
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #punkt 1
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], #vegger
                [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0], #punkt 2
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], #vegger
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], #punkt 3
                [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0], #vegger
                [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 4
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], #vegger
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0], #punkt 5
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #vegger
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], #punkt 6
                ]]
        lab = labyrinter[l]
        lab[(maaly - 1) * 2][(maalx - 1) * 2] = 2
        er, trekk = soek(spillerx - 1, spillery - 1, lab)
        trekk.reverse()
        return trekk

    def passord(self, rad1, rad2, rad3):
        ord = {
            "a" : { "b" : {"o" : "about"}, "f" : {"t" : "after"}, "g" : {"a" : "again"} },
            "b" : { "e" : { "l" : "below" } },
            "c" : { "o" : { "u" : "could" } },
            "e" : { "v" : { "v" : "every" } },
            "f" : { "i" : { "r" : "first" }, "o" : { "u" : "found" } },
            "g" : { "r" : { "e" : "great" } },
            "h" : { "o" : { "u" : "house" } },
            "l" : { "a" : { "r" : "large" }, "e" : { "a" : "learn"} },
            "n" : { "e" : { "v" : "never" } },
            "o" : { "t" : { "h" : "other" } },
            "p" : { "l" : { "a" : ["plant", "place"] }, "o" : { "i" : "point" } },
            "r" : { "i" : { "g" : "right" } },
            "s" : { "m" : { "a" : "small" }, "o" : { "u" : "sound" }, "p" : { "e" : "spell" }, "t" : { "i" : "still", "l" : "study" } },
            "t" : { "h" : { "e" : ["their", "there", "these"], "i" : ["thing", "think"], "r" : "three" } },
            "w": { "a" : { "t" : "water" }, "h" : { "e" : "where", "i" : "which" }, "o" : { "r" : "world", "u" : "would" }, "r" : { "i" : "write" } }
            }
        
        noekler = [*ord]
        for i in noekler:
            if i in rad1:
                noekler.remove(i)
        for i in noekler:
            del ord[i]
        
        for i in ord:
            ny = ord[i]
            noekler = [*ny]
            for j in noekler:
                if j in rad2:
                    noekler.remove(j)
            for j in noekler:
                del ny[j]
        
        for i in ord:
            for j in ord[i]:
                ny = ord[i][j]
                noekler = [*ny]
                for k in noekler:
                    if k in rad3:
                        noekler.remove(k)
                for k in noekler:
                    del ny[k]
        ny = dict(ord)
        res = []
        for i in ord:
            if ord[i] == {}:
                del ny[i]
            else:
                for j in ord[i]:
                    if ord[i][j] == {}:
                        del ny[i][j]
                    else:
                        for k in ord[i][j]:
                            res.append(ord[i][j][k])
        return res

    def knotter(self, antall, lampe1, lampe2):
        """lampe1 = nederst til venstre, lampe2 = øverst nest lengst til høyre"""
        if antall == 3:
            return "venstre"
        elif antall == 5 and lampe1:
            return "venstre"
        elif antall == 5:
            return "ned"
        elif antall == 7 and lampe2:
            return "opp"
        elif antall == 7:
            return "høyre"
        elif antall == 8 and lampe2:
            return "opp"
        elif antall == 8:
            return "ned"
        elif antall == 9:
            return "høyre"

def indekser(liste, maal):
    tot = []
    for i in range(len(liste)):
        if liste[i] == maal:
            tot.append(i)
    return tot

def slipping(stripe):
    if stripe == "blaa":
        return 4
    elif stripe == "gul":
        return 5
    else:
        return 1

def soek(x, y, lab):
    if lab[y * 2][x * 2] == 2:
        return True, []
    elif lab[y * 2][x * 2] == 1:
        return False, []

    lab[y * 2][x * 2] = 1

    if x < 5:
        if lab[y * 2][x * 2 + 1] == 0:
            er, ny_trekk = soek(x + 1, y, lab)
            if er:
                return True, ny_trekk + ["høyre"]
    if y < 5: 
        if lab[y * 2 + 1][x * 2] == 0:
            er, ny_trekk = soek(x, y + 1, lab)
            if er:
                return True, ny_trekk + ["ned"]
    if x > 0:
        if lab[y * 2][x * 2 - 1] == 0:
            er, ny_trekk = soek(x - 1, y, lab)
            if er:
                return True, ny_trekk + ["venstre"]
    if y > 0:
        if lab[y * 2 - 1][x * 2] == 0:
            er, ny_trekk = soek(x, y - 1, lab)
            if er:
                return True, ny_trekk + ["opp"]
    return False, []

def spill():
    ser = input("Skriv inn serienummeret på bomben: ")
    ind = oversett("Skriv inn opplyste indikatorer og skriv 'Ferdig' når du er ferdig: ", ["FRK", "CAR"], {}, True, ["f", "Ferdig", "ferdig"])
    bat = oversett("Skriv inn antall batterier er det på bomben: ", ["num"], {})
    par = oversett("Har bomben en parallellport (JA / NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True, "NEI" : False, "nei" : False})
    a = Avverger(ser, ind, bat, par)

    while True:
        print("\nModuler: ledninger(L), knappen(K), symboler(S), farger(F), ord(O), tall(T), morsekode(M), kompliserte ledninger(KL), ledningsskvenser(LS), labyrint(LB), passord(P), knotter(KT).")
        mod = input("Skriv inn modulen du vil løse og skriv 'Ferdig' når du har løst bomben: ")

        if mod == "Ferdig" or mod == "f":
            break

        if mod == "ledninger" or mod == "L":
            led = []
            num = 0
            ant = int(input("\nHvor mange ledninger er det: "))
            while num < ant:
                print("\nFarger: rød(R), hvit(H), blå(B), gul(G)")
                far = oversett("Hvilken farge har den " + str(num + 1) + ". ledningen: ", ["rød", "hvit", "blå", "gul", "svart", "R", "H", "B", "G", "S"], {"rød" : "roed", "R" : "roed", "H" : "hvit", "blå" : "blaa", "B" : "blaa", "G" : "gul", "S" : "svart"})
                led.append(far)
                num += 1
            print("\nKutt den " + str(a.ledninger(led)) + ". ledningen.")

        if mod == "knappen" or mod == "K":
            tek = oversett("\nHva står det på knappen: ", ["Abort", "Detonate", "Hold", "Press", "Release"], {})
            print("\nFarger: rød(R), hvit(H), blå(B), gul(G), grønn(GR), svart(S)")
            far = oversett("Hva er fargen på knappen: ", ["rød", "hvit", "blå", "gul", "grønn", "svart", "R", "H", "B", "G", "GØ", "S"], {"rød" : "roed", "R" : "roed", "H" : "hvit", "blå" : "blaa", "B" : "blaa", "G" : "gul", "grønn" : "groenn", "GØ" : "groenn", "S" : "svart"})
            if a.knapp(tek, far):
                stri = oversett("\nHold inne knappen. Hvilken farge er stripen på siden: ", ["rød", "hvit", "blå", "gul", "grønn", "svart", "R", "H", "B", "G", "GR", "S"], {"rød" : "roed", "R" : "roed", "H" : "hvit", "blå" : "blaa", "B" : "blaa", "G" : "gul", "grønn" : "groenn", "GR" : "groenn", "S" : "svart"})
                print("Slipp knappen når det er", slipping(stri), "på stoppeklokken.")
            else:
                print("\nTrykk knappen og slipp den med en gang.")

        if mod == "symboler" or mod == "S":
            symboler = ["Ϙ", "ƛ", "Ѭ", "ϗ", "Ͽ", "Ѧ", "Ӭ", "Ҩ", "☆(tom stjerne)", "¿", "©", "Ѽ", "Җ", "Ԇ", "ƀ", "б", "¶", "ټ(smilefjes)", "Ͼ", "Ѯ", "★(fylt stjerne)", "Ψ", "҂", "æ", "Ҋ", "Ω", "Ϟ"]
            print("\nSymboler: 0:Ϙ, 1:ƛ, 2:Ѭ, 3:ϗ, 4:Ͽ, 5:Ѧ, 6:Ӭ, 7:Ҩ, 8:☆(tom stjerne), 9:¿, 10:©, 11:Ѽ, 12:Җ, 13:Ԇ, 14:ƀ, 15:б, 16:¶, ټ:17(smilefjes), l8:Ͼ, 19:Ѯ, 20:★(fylt stjerne), 21:Ψ, 22:҂, 23:æ, 24:Ҋ, 25:Ω, 26:Ϟ")
            num = 0
            sym = []
            while num < 4:
                sym.append(int(oversett("Skriv inn det " + str(num + 1) + ". symbolet: ", [str(i) for i in range(26)], {})))
                num += 1
            svar = a.symboler(sym)
            print("\nTrykk på symbolene i denne rekkefølgen: " + symboler[svar[0]] + ", " + symboler[svar[1]] + ", " + symboler[svar[2]] + ", " + symboler[svar[3]])

        if mod == "farger" or mod == "F":
            trykk = []
            print("\nFarger: rød(R), blå(B), grønn(GR), gul(G)\n")
            while True:
                far = oversett("\nHva er den " + str(len(trykk) + 1) + ". fargen i sekvensen og skriv 'Ferdig' når modulen er løst: ", ["rød", "blå", "grønn", "gul", "R", "B", "GR", "G", "Ferdig", "f"], {"rød" : "roed", "R" : "roed", "blå" : "blaa", "B" : "blaa", "grønn" : "groenn", "GR" : "groenn", "G" : "gul", "Ferdig" : True, "f" : True})
                
                if far == True:
                    break

                trykk.append(a.simon_sier(far, int(oversett("Hvor mange feil har du gjort: ", [str(i) for i in range(3)], {}))))
                pr = trykk[0]
                temp = trykk.copy()
                temp.pop(0)
                for i in temp:
                    pr += ", " + i
                print("Trykk på:", pr)

        if mod == "ord" or mod == "O":
            for i in range(6):
                skj = input("\nHva står det øverst på modulen: ")
                ord = ["READY", "FIRST", "NO", "BLANK", "NOTHING", "YES", "WHAT", "UHHH", "LEFT", "RIGHT", "MIDDLE", "OKAY", "WAIT", "PRESS", "YOU", "YOU ARE", "YOUR", "YOU'RE", "UR", "U", "UH HUH", "UH UH", "WHAT?", "DONE", "NEXT", "HOLD", "SURE", "LIKE"]
                kna = [
                    oversett("Hva står det øverst til venstre: ", ord, {}),
                    oversett("Hva står det i midten til venstre: ", ord, {}),
                    oversett("Hva står det nederst til venstre: ", ord, {}),
                    oversett("Hva står det øverst til høyre: ", ord, {}),
                    oversett("Hva står det i midten til høyre: ", ord, {}),
                    oversett("Hva står det nederst til høyre: ", ord, {})]
                print("\nTrykk på knappen:", a.hvem_er_paa_foerst(skj, kna))

        if mod == "tall" or mod == "T":
            ste = 1
            tre = None
            while ste < 6:
                skj = int(oversett("\nHva står øverst på modulen: ", [str(i + 1) for i in range(4)], {}))
                kna = []
                tall = [str(i + 1) for i in range(4)]
                kna.append(int(oversett("Hva står det på den første knappen: ", tall, {})))
                tall.remove(str(kna[0]))
                kna.append(int(oversett("Hva står det på den andre knappen: ", tall, {})))
                tall.remove(str(kna[1]))
                kna.append(int(oversett("Hva står det på den tredje knappen: ", tall, {})))
                tall.remove(str(kna[2]))
                kna.append(int(oversett("Hva står det på den fjerde knappen: ", tall, {})))
                tre = a.hukommelse(ste, skj, kna, tre)
                print("Trykk på:", tre[ste - 1][0])
                ste += 1

        if mod == "labyrint" or mod == "LB":
            sx = int(oversett("\nHva er x-posisjonen til den ene sirkelen: ", [str(i + 1) for i in range(6)], {}))
            sy = int(oversett("Hva er y-posisjonen til den ene sirkelen: ", [str(i + 1) for i in range(6)], {}))

            spx = int(oversett("\nHva er x-posisjonen til spilleren: ", [str(i + 1) for i in range(6)], {}))
            spy = int(oversett("Hva er y-posisjonen til spilleren: ", [str(i + 1) for i in range(6)], {}))

            mx = int(oversett("\nHva er x-posisjonen til målet: ", [str(i + 1) for i in range(6)], {}))
            my = int(oversett("Hva er y-posisjonen til målet: ", [str(i + 1) for i in range(6)], {}))

            print("\nGjør disse trekkene:", a.labyrint(sx, sy, spx, spy, mx, my))

        if mod == "morsekode" or mod == "M":
            print("\nEksempel: --.. -. ..- .")
            mor = oversett("Skriv inn morsekoden: ", [".", "-", " ", "cha"], {})
            print("\nLøsningen er:", a.morse_kode(mor))

        if mod == "kompliserte ledninger" or mod == "KL":
            for i in range(6):
                bl = oversett("\nHar ledningen " + str(i + 1) + ". noe blått(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True,  "NEI" : False, "nei" : False})
                ro = oversett("Har ledningen " + str(i + 1) + ". noe rødt(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True,  "NEI" : False, "nei" : False})
                st = oversett("Har ledningen " + str(i + 1) + ". en stjerne(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True,  "NEI" : False, "nei" : False})
                la = oversett("Har ledningen " + str(i + 1) + ". en lysende lampe(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True,  "NEI" : False, "nei" : False})

                if a.kompliserte_ledninger(ro, bl, st, la):
                    print("\nKutt ledningen")
                else:
                    print("\nIkke kutt ledningen")

        if mod == "ledningssekvenser" or mod == "LS":
            num = 0
            tel = None
            while num < 18:
                print("\nFarger: rød(R), blå(B), svart(S)")
                far = oversett("Hvilken farge har ledning nummer " + str(num + 1) + ".: ", ["rød", "blå", "svart", "R", "B", "S"], {"rød" : "roed", "R" : "roed", "blå" : "blaa", "B" : "blaa", "S" : "svart"})
                bok = input("Hvilken bokstav går ledning nummer " + str(num + 1) + ". til: ")

                kutt, tel = a.lednings_sekvenser(far, bok, tel)

                if kutt:
                    print("\nKutt ledningen")
                else:
                    print("\nIkke kutt ledningen")

                num += 1

        if mod == "passord" or mod == "P":
            print("\nEksempel: HNOIFSZ")
            rad1 = list(oversett("Hva er alle bokstavene i første rad: ", ["str"], {}))
            rad2 = list(oversett("Hva er alle bokstavene i andre rad: ", ["str"], {}))
            rad3 = list(oversett("Hva er alle bokstavene i tredje rad: ", ["str"], {}))

            print("Passordet er en av disse:", a.passord(rad1, rad2, rad3))

        if mod == "knotter" or mod == "KT":
            ant = int(input("\nHvor mange lamper lyser: "))
            l1 = oversett("Lyser lampen nederst til venstre(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True, "NEI" : False, "nei" : False})
            l2 = oversett("Lyser lampen øverst nest lengst til høyre(JA/NEI): ", ["JA", "ja", "NEI", "nei"], {"JA" : True, "ja" : True, "NEI" : False, "nei" : False})

            print("Svaret er:", a.knotter(ant, l1, l2))

def oversett(tekst, forventet, over, loop = False, stopp = []):
    inp = ""
    char = False
    if "cha" in forventet:
        char = True
        forventet.remove("cha")

    if loop:
        alle = []
        while not inp in stopp:
            inp = input(tekst)
            if not inp == "":
                if inp in forventet:
                    alle.append(inp)

        for i in range(len(alle)):
            if alle[i] in over:
                alle[i] = over[alle[i]]

        return alle

    else:
        while not inp in forventet:
            inp = input(tekst)
            if not inp == "":
                if "num" in forventet:
                    if inp.isdigit():
                        inp = int(inp)
                        break
                if "str" in forventet:
                    if inp.isalpha():
                        break

                if char:
                    br = True
                    for i in inp:
                        if not i in forventet:
                            br = False
                    if br:
                        break

    if inp in over:
        inp = over[inp]

    return inp

spill()