---
layout: default
---

# Sistemi informatici e loro gestione

## Prova d'esame

### Parte II: Domande

Vi verranno presentate dieci blocchi di quattro domande ciascuno, cui potete rispondere "vero" o "falso" scrivendo rispettivamente "V" o "F" di fianco alla domanda.
Il punteggio della prova è la somma dei punteggi dei blocchi.
Il punteggio di un blocco è la somma dei punteggi delle domande che lo compongono, con un aggiustamento: valori negativi sono riportati a zero (ciascun blocco può portare da 0 a 8 punti).
Ciascuna domanda vale 2 punti se indovinata, 0 punti se omessa, e -1 punto se errata.

#### 1. Con riferimento ai linguaggi di programmazione:

* Compilazione ed interpretazione sono sinonimi
* La compilazione è l'operazione con cui viene tradotto il codice sorgente da un linguaggio ad un altro
* L'interpretazione produce in output dei file eseguibili
* Perché un programma possa funzionare su un dato computer, è necessario che il processore sia costruito in maniera tale da poter eseguire il codice sorgente del linguaggio in cui il programma è scritto

#### 2. Il sistema operativo

* Fa da intermediario fra la parte fisica della macchina (hardware) e le applicazioni vere e proprie
* È composto da un insieme di driver che interagiscono fra loro tramite uno scheduler
* Consente l'esecuzione concorrente di più processi
* Gestisce la multiutenza

#### 3. Il file system

* Rappresenta il sistema adottato per gestire i file sulla memoria RAM del computer in modo persistente
* In ambiente Unix, è usato anche per il mapping dei dispositivi
* Ha una struttura ad albero (a grafo, se si considerano i link)
* Si occupa anche di registrare metadati riguardanti i file

#### 4. Il terminale

* Consente di interagire tramite comandi testuali con il sistema operativo
* È utilizzato solo in ambiente Unix
* Consente di collegare lo standard input di un processo allo standard output di un altro processo
* Può interpretare più comandi inseriti in un solo file, di fatto creando un vero e proprio programma

#### 5. Il comando `cat documento.txt | grep filosofia >> mydoc.txt`

* Se `mydoc.txt` non è presente sul file system, lancia un errore
* Se `mydoc.txt` è già presente sul file system, lo sovrascrive
* Usa il carattere `|` per collegare lo standard input di `cat` allo standard output del file `mydoc.txt`
* Prende il contenuto del file `documento.txt`, ne filtra solo le linee che contengono la parola `filosofia`, quindi stampa il risultato in standard output

#### 6. Con riferimento alle reti

* Il modello ISO/OSI ha un'architettura a strati
* La comunicazione fra due strati diversi prende il nome di protocollo, la comunicazione fra strati uguali su diversi nodi di rete prende il nome di interfaccia
* Lo strato 2 si occupa delle caratteristiche fisiche del mezzo di trasmissione
* Dovendo collocare il protocollo IP nel modello ISO/OSI, sarebbe corretto inserirlo nello strato 3

#### 7. La rete Internet

* Internet è basata sul modello ISO/OSI
* La differenza principale fra UDP e TCP è che il primo è connection-oriented
* Il servizio DNS si occupa della risoluzione di nomi in indirizzi IP
* Perché due processi possano comunicare via Internet, è sufficiente la conoscenza degli indirizzi IP delle macchine host.

#### 8. Il world wide web

* Rappresenta una rete che interconnette più computer
* Fa uso delle Uniform Resource Locator (URL) per indirizzare i documenti
* È un sinonimo di Internet
* È un linguaggio interpretato

#### 9. HTML

* È un linguaggio di markup
* È un linguaggio di programmazione
* Specifica in modo univoco e non ambiguo la formattazione di una pagina web
* `<a href="pages/target.htm"> <img src="images/pluto.png"> </a> </img>` è una stringa HTML valida

#### 9. Con riferimento al modello relazionale, lo schema E/R, e il linguaggio SQL

* È possibile utilizzare SQL sia per creare e popolare un database che per interrogarlo
* SQL è un linguaggio di programmazione interpretato
* In un database relazionale, non è possibile inserire valori `NULL` in una chiave primaria
* È possibile avere degli schemi che non contengono alcuna istanza
