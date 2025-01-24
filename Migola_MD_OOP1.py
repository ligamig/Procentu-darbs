#1. uzdevums
class turnirs:
    def __init__(self, nosaukums, cilvSkaits, grupuSkaits, sportaVeids,):
        self.nosaukums =  nosaukums
        self.cilvSkaits = cilvSkaits
        self.grupuSkaits = grupuSkaits
        self.sportaVeids = sportaVeids
        self.sponsori = []

    def SponsoruSaraksts(self, sponsori):
        self.sponsori.append(sponsori)
        
    def izvade(self):
        sponsors = "\n".join(self.sponsori)
        return (
            f"Šis ir {self.sportaVeids} turnīrs \"{self.nosaukums}\", kurā piedalās {self.cilvSkaits} cilvēki, {self.grupuSkaits} grupas. \n"
            f"Sponsori: \n{sponsors} "
        )

t1 = turnirs("Last Dab 2025", 18, 5, "Tortnite")
t1.SponsoruSaraksts("Adidaš")
t1.SponsoruSaraksts("Mike")
t1.SponsoruSaraksts("DolčeNKabana")
print(t1.izvade())

print("-----")

t2 = turnirs("Spray & pray", 20, 4, "Valoban")
t2.SponsoruSaraksts("Red Wool")
t2.SponsoruSaraksts("Bego")
t2.SponsoruSaraksts("Ronster")
print(t2.izvade())