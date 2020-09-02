from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime

url = requests.get("https://www.ojogodobicho.com/deu_no_poste.htm").text

soup = BeautifulSoup(url, "lxml")

table = soup.find("table", {
    "class": "twelve"
})

th = table.findAll("th")
td = table.findAll("td")

os.system('clear') or None

lstNumeroBicho = [["1","Avestruz"],
["2","Aguia"],
["3","Burro"],
["4","Borboleta"],
["5","Cachorro"],
["6","Cabra"],
["7","Carneiro"],
["8","Camelo"],
["9","Cobra"],
["10","Coelho"],
["11","Cavalo"],
["12","Elefante"],
["13","Galo"],
["14","Gato"],
["15","Jacaré"],
["16","Leão"],
["17","Macaco"],
["18","Porco"],
["19","Pavão"],
["20","Peru"],
["21","Touro"],
["22","Tigre"],
["23","Urso"],
["24","Veado"],
["25","Vaca"]]

for f in lstNumeroBicho:
    print(f[0], " - ", f[1])

lstResultado = ["PTM","PT","PTV","PTN","COR"]

for r in range(0, len(lstResultado)):
    for t in th:
        if lstResultado[r] == t.getText():
            print(f"#Resultado {lstResultado[r]} ", datetime.now().strftime("%d/%m/%Y %H:%M"))

            if lstResultado[r] == "PTM":
                for res in range(0, len(td)):
                    if td[res].get("title") != "0":
                        if res == 1:
                            print(f"{td[res].getText()}")
                        if res == 7:
                            print(f"{td[res].getText()}")
                        if res == 13:
                            print(f"{td[res].getText()}")
                        if res == 19:
                            print(f"{td[res].getText()}")
                        if res == 25:
                            print(f"{td[res].getText()}")
                        if res == 31:
                            print(f"{td[res].getText()}")
                        if res == 37:
                            print(f"{td[res].getText()}")

            if lstResultado[r] == "PT":
                for res in range(0, len(td)):
                    if td[res].get("title") != "0":
                        if res == 2:
                            print(f"{td[res].getText()}")
                        if res == 8:
                            print(f"{td[res].getText()}")
                        if res == 14:
                            print(f"{td[res].getText()}")
                        if res == 20:
                            print(f"{td[res].getText()}")
                        if res == 26:
                            print(f"{td[res].getText()}")
                        if res == 32:
                            print(f"{td[res].getText()}")
                        if res == 38:
                            print(f"{td[res].getText()}")

            if lstResultado[r] == "PTV":
                for res in range(0, len(td)):
                    if td[res].get("title") != "0":
                        if res == 3:
                            print(f"{td[res].getText()}")
                        if res == 9:
                            print(f"{td[res].getText()}")
                        if res == 15:
                            print(f"{td[res].getText()}")
                        if res == 21:
                            print(f"{td[res].getText()}")
                        if res == 27:
                            print(f"{td[res].getText()}")
                        if res == 33:
                            print(f"{td[res].getText()}")
                        if res == 39:
                            print(f"{td[res].getText()}")

            if lstResultado[r] == "PTN":
                for res in range(0, len(td)):
                    if td[res].get("title") != "0":
                        if res == 4:
                            print(f"{td[res].getText()}")
                        if res == 10:
                            print(f"{td[res].getText()}")
                        if res == 16:
                            print(f"{td[res].getText()}")
                        if res == 22:
                            print(f"{td[res].getText()}")
                        if res == 28:
                            print(f"{td[res].getText()}")
                        if res == 34:
                            print(f"{td[res].getText()}")
                        if res == 40:
                            print(f"{td[res].getText()}")

            if lstResultado[r] == "COR":
                for res in range(0, len(td)):
                    if td[res].get("title") != "0":
                        if res == 5:
                            print(f"{td[res].getText()}")
                        if res == 11:
                            print(f"{td[res].getText()}")
                        if res == 17:
                            print(f"{td[res].getText()}")
                        if res == 23:
                            print(f"{td[res].getText()}")
                        if res == 29:
                            print(f"{td[res].getText()}")
                        if res == 35:
                            print(f"{td[res].getText()}")
                        if res == 41:
                            print(f"{td[res].getText()}")
