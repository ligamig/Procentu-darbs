import requests
import json

atbilde = requests.get("https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json")

if (atbilde.status_code != 200):
    print("Kaut kas nav pareizi")

atbildeDict = json.loads(atbilde.text) #pārveido par dict

#1. uzd
def augstskolasLatvija(atbildeDict):
    latvijasAugstskolas = []
    for uni in atbildeDict:
        if uni["country"] == "Latvia":
            latvijasAugstskolas.append(uni)

    return latvijasAugstskolas
    #kopejaisAugstskoluSkaits = 0
latvijasAugstskolas = augstskolasLatvija(atbildeDict)

#print(f"Latvijā ir {len(latvijasAugstskolas)} augstskolas.")

#2. uzd 
#for uni in latvijasAugstskolas:
#    print(uni["name"])

#3. uzd
def augstskolasFrancija(atbildeDict):
    FrancijasAugstskolas = []
    for uni in atbildeDict:
        if uni["country"] == "France":
            FrancijasAugstskolas.append(uni)

    return FrancijasAugstskolas
francijasAugstskolas = augstskolasFrancija(atbildeDict)
print(f"Francijā ir {len(francijasAugstskolas)} augstskolas.")

#4. uzd
eu = sum(1 for uni in francijasAugstskolas if any(".eu" in domain for domain in uni["domains"]))
procenti = (eu / len(francijasAugstskolas)) * 100 if francijasAugstskolas else 0

print(f"No tām {eu} augstskolām ir mājaslapa ar .eu domēnu ({procenti:.2f}%)")

#5. uzd
parize = sum(1 for uni in francijasAugstskolas if "Paris" in uni ["name"])
print(f"No visām Francijas augstskolām, {parize} augstskolu nosaukumi satur vārdu 'Paris'.")

#6. uzd
https = sum(1 for uni in francijasAugstskolas if any(domain.startswith("https") for domain in uni ["web_pages"]))
procenti = (https / len(francijasAugstskolas)) * 100 if francijasAugstskolas else 0

print(f"No tām {https} augstskolām mājaslapas sākas ar https ({procenti:.2f}%)")

#7. uzdevums
eiropas_valstis = {
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria",
    "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
    "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
    "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
    "Turkey", "Ukraine", "United Kingdom", "Vatican City"
}

valstu_skaiti = {}

for uni in atbildeDict:
    valsts = uni["country"]
    if valsts in eiropas_valstis:
        if valsts in valstu_skaiti:
            valstu_skaiti[valsts] += 1
        else:
            valstu_skaiti[valsts] = 1

max_valsts = max(valstu_skaiti, key=valstu_skaiti.get)
max_skaits = valstu_skaiti[max_valsts]

print(f"Eiropas valsts ar visvairāk augstskolām ir {max_valsts} ar {max_skaits} augstskolām.")