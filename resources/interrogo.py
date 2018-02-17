#!/usr/bin/env python

population = ['Luca Rossi', 'Mario Biondi', 'Giacomo Leopardi']

import re, sys, shelve, random

INDICE, NOME, PRESENTE, CORRETTE, SBAGLIATE = range(5)
STUDENTI = 'studenti'

shelf = shelve.open('students.dat')
if STUDENTI not in shelf:
    print('Creazione struttura')
    shelf[STUDENTI] = { i : [i, v, True, 0, 0] for i, v in enumerate(population) }

studenti = shelf[STUDENTI]
presenti = [v for v in studenti.values() if v[PRESENTE]]
numChiamate = [v[CORRETTE]+v[SBAGLIATE] for v in presenti]
minChiamate = min(numChiamate)
interrogabili = [v for v in presenti if v[CORRETTE]+v[SBAGLIATE]==minChiamate]

args = sys.argv[1:]
if len(args)==0:
    print("USAGE: \n\tscegli\n\tassente\n\tpresente\n\tstatistica")
elif args[0]=='scegli':
    eletto = interrogabili[random.randint(0,len(interrogabili)-1)]
    print("L'eletto/a è: " + eletto[NOME])
    risposta = input('La sua risposta è... ')
    risposta = risposta=='ok'
    if risposta: eletto[CORRETTE] = eletto[CORRETTE] + 1
    else: eletto[SBAGLIATE] = eletto[SBAGLIATE] + 1
    studenti[eletto[INDICE]] = eletto
elif args[0]=='assente' or args[0]=='presente':
    presente = args[0]=='presente'
    chi = args[1]
    ricerca = [i for i,v in enumerate(population) if re.search(chi, v)]
    if len(ricerca)!=1: print('Trovati ' + len(ricerca) + ' elementi col nome fornito: ' + str(ricerca))
    else:
        print('Studente ' + studenti[ricerca[0]][NOME] + " impostato come " + ('presente' if presente else 'assente')) 
        studenti[ricerca[0]][PRESENTE] = presente
elif args[0]=="statistica":
    for s in studenti.values():
        print("{0}) {1} ({2}) - corrette={3}; sbagliate={4}".format(s[0], s[1], 'presente' if s[2] else 'assente', s[3], s[4] ))

shelf[STUDENTI] = studenti
shelf.close()