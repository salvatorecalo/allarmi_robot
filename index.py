from csv import reader
from operator import itemgetter

def main():
    elenco = leggi_file("allarmi.csv")
    print(elenco)
    elenco_ordinato_severita_decrescente = ordina_allarmi_crescenti(elenco)
    print("Robot \t Allarme")
    for Robot in elenco_ordinato_severita_decrescente:
        print(f"per il robot {Robot['id_robot']} si sono verificati {Robot['severity']} allarmi")

    robot_con_severita_piu_elevata = livello_massimo_criticita(elenco)
    print("Il livello massimo di severità 10 è stato raggiunto dai seguenti robot: ")
    for robot in robot_con_severita_piu_elevata:
        print(robot)
"""
@function leggi_file: funzione che legge il file sul quale iterare
@params file_name: nome del file
"""
def leggi_file(file_name):
    try:
        inFIle = open(file_name, "r", encoding="utf-8")
        try:
            lista = []
            lettore = reader(inFIle)
            prima = True
            for riga in lettore:
                if prima:
                    prima = False
                else:
                    campi = riga[0].split(";")
                    fk_id_robot = campi[0]
                    severity = campi[1]
                    alarm_text = campi[2]
                    record = {
                        "id_robot": fk_id_robot,
                        "severity": severity,
                        "alarm_text": alarm_text
                    }
                    lista.append(record)
            return lista
        except Exception as message:
            exit(str(message))
    except FileNotFoundError:
        exit("Non è stato possibile accedere al file, controlla e riprova!")

"""
@function ordina_allarmi_crescenti: funzione che ordina gli id dei robot
                                    in ordine crescente in base al grado di severity
@params elenco: elenco sul quale iterare
"""
def ordina_allarmi_crescenti(elenco):
    elencoOrdinato = sorted(elenco, key=itemgetter("severity"), reverse=True)
    return elencoOrdinato

"""
@function livello_massimo_criticita: funzione che rileva quale robot ha riscontrato il livello massimo di criticità
@params elenco: elenco sul quale iterare
"""
def livello_massimo_criticita(elenco):
    massimo = 0
    lista = []
    for robot in elenco:
        if int(robot["severity"]) > massimo:
            massimo = int(robot["severity"])
    for robot in elenco:
        if int(robot["severity"]) == massimo:
            lista.append(robot["id_robot"])
    return lista
main()