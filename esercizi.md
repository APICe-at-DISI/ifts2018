---
layout: default
---

# Sistemi informatici e loro gestione

## Prova d'esame

### Parte I: Esercizi

#### Terminale (12 punti)

Si supponga di operare sul seguente file system:

{% highlight bash %}
/
├── bin
├── boot
├── dev
├── etc
├── home
│   ├── user
│   │   ├── Downloads
│   │   ├── Desktop
│   │   │   ├── documento.txt
│   │   │   └── immagine.jpg
│   │   └── Pictures
│   └── gigi
├── lib
├── opt
├── proc
├── tmp
├── usr
└── var
{% endhighlight %}

Supponendo che il terminale punti a `/home/user/` e che sia loggato come utente `user`, scriva la sequenza di comandi necessari a:

0. Stampare su terminale il contenuto del file `documento.txt`
0. Stampare su terminale le righe del file `documento.txt` contenenti la parola `esame`
0. Creare la cartella `Documents` dentro `/home/user/`
0. Copiare il file `documento.txt` dentro la cartella menzionata al punto precedente
0. Creare un nuovo file di testo di nome `pluto.txt` dentro la cartella `Documents` che contenga la frase `lo zibetto mangia i croccantini`
0. Aggiungere al file del punto precedente una seconda linea di testo: `e fa indigestione`
0. Spostare il file `immagine.jpg` dentro la cartella `Pictures`


Al termine delle operazioni, il file system dovrà essere il seguente:

{% highlight bash %}
/
├── bin
├── boot
├── dev
├── etc
├── home
│   ├── user
│   │   ├── Documents
│   │   |   ├──  documento.txt
│   │   |   └──  pluto.txt
│   │   ├── Downloads
│   │   ├── Desktop
│   │   │   └──  documento.txt
│   │   └── Pictures
│   │       └── immagine.jpg
│   └── gigi
├── lib
├── opt
├── proc
├── tmp
├── usr
└── var
{% endhighlight %}

#### Routing (6 punti)

Si supponga di disporre della seguente tabella di routing:
{% highlight bash %}
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         137.204.107.254 0.0.0.0         UG    100    0        0 enp2s0
137.204.107.0   0.0.0.0         255.255.255.0   U     100    0        0 enp2s0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
{% endhighlight %}

Si determini il gateway (o, se non presente, si indichi "consegna diretta") per i seguenti indirizzi IP:
* `8.8.8.8`
* `192.168.1.1`
* `137.204.106.15`
* `137.204.107.124`
* `172.17.25.125`
* `8.8.4.4`
* `172.17.26.127`

#### HTML (12 punti)

Si realizzi una pagina web in puro HTML con le seguenti caratteristiche:

* Abbia come titolo "Esame IFTS"
* Contenga due paragrafi. Il testo del primo sia «Benvenuto».», il testo del secondo sia «Vai al sito IFTS»
* includa l'immagine `pluto.png` presente nella cartella `img` che si trova nella stessa posizione in cui è stato posizionato il file HTML
* La parola "Vai" sia un collegamento ipertestuale alla pagina `http://bit.ly/ifts2017`

#### Progettazione di un database (15 punti)

Si realizzi lo schema E/R e si indichino le tabelle e le chiavi primarie del database del circolo del tennis di Trivella di Predappio, sapendo che:
* dovranno essere memorizzati nome, cognome, e codice fiscale dei tesserati;
* dovranno essere memorizzati nome, cognome, e codice fiscale degli arbitri;
* dovranno essere memorizzati i campi da gioco disponibili;
* ciascun campo ha un fondo (cemento, erba, terra rossa);
* possono esserci più campi con lo stesso fondo;
* dovranno essere memorizzate le date degli incontri fra tesserati;
* ciascun incontro deve registrare il punteggio del primo giocatore ed il punteggio del secondo giocatore
* ciascun incontro si tiene su un campo;
* un tesserato gioca al massimo una partita ogni giorno.

#### Scrittura di query SQL (15 punti)

Con riferimento al database sopra realizzato, si scrivano le seguenti query SQL:
* L'elenco dei nomi dei giocatori, senza ripetizioni. (3 punti)
* L'elenco, in ordine alfabetico, dei cognomi degli arbitri che hanno diretto una partita su terreno con fondo in cemento nel 2015 (6 punti)
* Il numero medio di punti totalizzato dal giocatore sconfitto (6 punti)
  * A tal proposito, si ricorda che il giocatore sconfitto è quello che totalizza il punteggio più basso (ossia il *minimo*) fra i due, per cui dati tutti i punteggi, è necessario operare la media dei valori minimi.
