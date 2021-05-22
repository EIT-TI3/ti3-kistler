from datetime import datetime

def check_time(table0, table1, i0, i1):
    '''
    Gibt
        -1  zurueck, wenn die Zeile i0 in table0 frueher ist 
            als die Zeile i1 in table1
         1  zurueck, wenn die Zeile i0 in table0 spaeter ist
            als die Zeile i1 in table1 
         0  zurueck, wenn die Zeile i0 in table0 zeitgleich ist 
            mit der Zeile i1 in table1
            
    Bezieht sich ein Index auf eine nicht existierende Zeile 
    (d.h. wenn er zu gross ist), wird die Zeile in der anderen Tabelle als 
    kleiner betrachtet.
    '''
    if i1>=len(table1['date']):
        if i0 >= len(table0['date']):
            # beide Indizes ueberschreiten den Bereich
            ergebnis = 0              
        else:
            # nur Index in table1 ueberschreitet den Bereich
            ergebnis = -1             
    elif i0 >= len(table0['date']):
        ergebnis=1
    else:
        timestamp0=datetime.strptime(table0['date'][i0] + ' '\
                                     + table0['time'][i0], '%d.%m.%Y %H:%M')
        timestamp1=datetime.strptime(table1['date'][i1] + ' '\
                                     + table1['time'][i1], '%d.%m.%Y %H:%M')
        ergebnis=int(timestamp0>timestamp1) - int(timestamp0<timestamp1)
    return ergebnis