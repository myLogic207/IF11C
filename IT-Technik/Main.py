def printAllStatus():
    counter = 1
    for pos in parkplatz:
        match pos:
            case 0:
                print("Parkplatz", counter, "ist Frei")
            case 1:
                print("Parkplatz", counter, "ist Belegt")
            case 1:
                print("Parkplatz", counter, "ist Reserviert")
        counter+=1

def range(input, floor, roof):
    return (input >= floor and input <= roof)

def changeStaus():
    iParkplatzNr = int(input("Zum bearbeiten nummer eingeben:(1-10)"))
    iStatus = int(input("Neuen Wert zuweisen:(0-2)"))
    while True:
        if range(iParkplatzNr, 1, 10) and range(iStatus, 0,2):
            parkplatz[iParkplatzNr-1] = iStatus
            print("Parkplatz", iParkplatzNr, "hat nun den status", iStatus)
            break
        else:
            print("Eingabe abgebrochen/ungültig")

parkplatz = [0, 0, 1, 0, 1, 1, 2, 1, 0, 2]
while True:
    print("----- Starting PISS - Parkinglot Information Service Script -----")
    printAllStatus()
    change = bool(input("Want to change a Space (0/1)?"))
    if change:
        changeStaus()
    print("--------------------------------")


