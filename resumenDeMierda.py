import datetime
import time
from collections import OrderedDict

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def resumenDelMes(mierdas: dict) -> str:
    mierdasDelMes = getMierdasDelMes(mierdas)
    refinedData = {}
    refinedData["goldenHour"] = max(set(mierdasDelMes["dumpHours"]), key = mierdasDelMes["dumpHours"].count)
    refinedData["goldenDay"] = max(set(mierdasDelMes["dumpDays"]), key = mierdasDelMes["dumpDays"].count)
    refinedData["goldenDayCont"] = mierdasDelMes["dumpDays"].count(refinedData["goldenDay"])
    refinedData["total"] = len(mierdasDelMes["dumpDays"])

    mainStats = {}
    for participante in mierdas.keys():
        mainStats[mierdasDelMes[participante]["nombre"]] = len(mierdasDelMes[participante]["cacas"])
    refinedData["mainStats"] = OrderedDict(reversed(list(dict(sorted(mainStats.items(), key=lambda item: item[1])).items())))

    return makeMessage(refinedData)

    

def getMierdasDelMes(mierdas: dict) -> dict:
    today = time.mktime(datetime.date.today().timetuple())
    oneMonthPrior = today - 2678400
    newMierdas = {}
    newMierdas["dumpDays"] = []
    newMierdas["dumpHours"] = []
    for participante in mierdas:
        newMierdas[participante] = {}
        newMierdas[participante]["cacas"] = []
        newMierdas[participante]["nombre"] = mierdas[participante]["nombre"]
        
        for mierda in mierdas[participante]["cacas"]:
            if mierda in range(int(oneMonthPrior), int(today)):
                newMierdas[participante]["cacas"].append(mierda)
                newMierdas["dumpDays"].append(datetime.date.fromtimestamp(mierda).day)
                newMierdas["dumpHours"].append(datetime.datetime.fromtimestamp(mierda).hour)
            
    return newMierdas

def makeMessage(data: dict) -> str:
    mainText = "El mes de {mes} se han creado {totalMierdas}\nEl dia mas productivo fue el {topDia} de {mes} con un total de {goldenDayCont}\nLa hora favorita para cagar ha sido a las {goldenHour}\n\nEl top este mes ha sido el siguiente:\n\n".format(mes = meses[datetime.date.today().month-2], totalMierdas = data["total"], topDia = data["goldenDay"], goldenDayCont = data["goldenDayCont"],  goldenHour = data["goldenHour"])
    for index,participante in enumerate(data["mainStats"]):
        print(participante)
        mainText += "{quien} con {cuanto} mierdas en {posicion}º posicion\n".format(quien = participante,  cuanto = data["mainStats"][participante], posicion = index + 1)
    mainText += "\nNos vemos el mes que viene!"
    return mainText