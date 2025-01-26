class augi:
    def __init__(self, nosaukums, daudzums):
        self.nosaukums = nosaukums
        self.daudzums = daudzums
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami"

class augli(augi):
    def __init__(self, nosaukums, daudzums, seklas10g):
        super().__init__(nosaukums, daudzums)
        self.seklas10g = seklas10g
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.seklas10g} sēkas uz 10 gramiem"

class darzeni(augi):
    def __init__(self, nosaukums, daudzums, alergija):
        super().__init__(nosaukums, daudzums)
        self.alergija = alergija
    def __str__(self):
        alergijuIzraisisana = "alerģiju izraisa" if self.alergija else "alerģiju neizraisa"
        return f"{self.nosaukums}, {self.daudzums} grami, {alergijuIzraisisana}"

class pukes(augi):
    def __init__(self, nosaukums, daudzums, ziedi):
        super().__init__(nosaukums, daudzums)
        self.ziedi = ziedi
    def __str__(self):
        return f"{self.nosaukums}, {self.daudzums} grami, {self.ziedi} ziedi"
    
# auguSaraksts = []
# auguSaraksts.append(darzeni("Burkāni", 100, True))
# auguSaraksts.append(darzeni("Kartupeļi", 50, False))
# auguSaraksts.append(darzeni("Gurķi", 150, False))
# auguSaraksts.append(darzeni("Tomāti", 90, True))
# auguSaraksts.append(augli("Āboli", 30, 5))
# auguSaraksts.append(augli("Bumbieri", 50, 4))
# auguSaraksts.append(augli("Banāni", 40, 2))
# auguSaraksts.append(augli("Granātāboli", 60, 7))
# auguSaraksts.append(pukes("Dālijas", 700, 1))

# for Augi in auguSaraksts:
#     print(Augi)


class Recepte:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.auguSaraksts = []
        self.alergijuIzraisisana = False
        self.derigums = True

    def pievienot_augu(self, augi):
        self.auguSaraksts.append(augi)
    
    def kopejaisgramuSkaits(self):
        return sum(augi.daudzums for augi in self.auguSaraksts)
    
    def derigumaParbaude(self):
        for augi in self.auguSaraksts:
            if isinstance(augi, pukes):
                self.derigums = False
                break

    def alergijasParbaude(self):
        for augi in self.auguSaraksts:
            if isinstance(augi, darzeni) and augi.alergija:
                self.alergijuIzraisisana = True
                break

    def __str__(self):
        informacija = f"Recepte: {self.nosaukums}\n"
        for augi in self.auguSaraksts:
            informacija += f"*{augi}\n"
        informacija += ""###########\n"
        informacija += "Recepte "
        informacija += "izraisa alerģiju\n" if self.alergijuIzraisisana else "alerģiju neizraisa\n"
        informacija += "Recepte "
        informacija += "nederīga" if not self.derigums else "derīga"
        return informacija
    
auguSaraksts = []
auguSaraksts.append(darzeni("Burkāni", 100, True))
auguSaraksts.append(darzeni("Kartupeļi", 50, False))
auguSaraksts.append(darzeni("Gurķi", 150, False))
auguSaraksts.append(darzeni("Tomāti", 90, True))
auguSaraksts.append(augli("Āboli", 30, 5))
auguSaraksts.append(augli("Bumbieri", 50, 4))
auguSaraksts.append(augli("Banāni", 40, 2))
auguSaraksts.append(augli("Granātāboli", 60, 7))
auguSaraksts.append(pukes("Rozes", 500, 4))
auguSaraksts.append(pukes("Dālijas", 700, 1))

r1 = Recepte("Banānu suflē")
r1.pievienot_augu(auguSaraksts[4])
r1.pievienot_augu(auguSaraksts[2])
r1.pievienot_augu(auguSaraksts[6])
r1.derigumaParbaude()
r1.alergijasParbaude()

print(r1)
print("-------------------")

r2 = Recepte("Ratatouille")
r2.pievienot_augu(auguSaraksts[8])  # Rozes
r2.pievienot_augu(auguSaraksts[0])  # Burkāni
r2.derigumaParbaude()
r2.alergijasParbaude()
print(r2)