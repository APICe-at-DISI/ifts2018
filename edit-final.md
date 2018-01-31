---
layout: default
---

# Prova d'esame

## Nome _______________________________________________________________________

## Cognome ____________________________________________________________________

## Sistemi informatici e loro gestione

Indicare, per ciascuna affermazione, se sia vera o falsa. Rispondere correttamente contribuisce con 0.2 punti al punteggio totale, rispondere in modo erroneo comporta una penalizzazione di 0.1 punti, mentre non rispondere non comporta alcuna penalità.

### Il sistema operativo e il file system

* Il sistema operativo espone la memoria virtuale della macchina sulla rete Internet
* I sistemi operativi moderni consentono l'esecuzione concorrente di più processi e la gestione della multiutenza
* Il file system ha una struttura ad albero (a grafo, se si considerano i link)
* Il file system si occupa anche di registrare metadati riguardanti i file

### Con riferimento ad Internet e al world wide web

* Internet è un sinonimo di World Wide Web
* Il servizio DNS si occupa di trasformare indirizzi macchina (MAC address) in indirizzi IP
* Oltre all'indirizzo IP, è necessaria la conoscenza della porta perché due processi possano comunicare via Internet
* Il world wide web fa uso di uso delle Uniform Resource Locator (URL) per indirizzare i documenti

### HTML

* È un linguaggio di programmazione
* È un protocollo di rete
* `<a href="pages/target.htm"> <img src="images/pluto.png"> </a> </img>` è una stringa HTML valida

### Con riferimento al modello relazionale, lo schema E/R, e il linguaggio SQL

* È possibile utilizzare SQL interrogare un database, ma non per crearlo e popolarlo.
* SQL è un linguaggio di programmazione compilato
* In un database relazionale, è possibile a volte inserire valori `NULL` in una chiave primaria
* È possibile avere degli schemi che non contengono alcuna istanza

## Programmazione

Indicare, per ciascuna affermazione, se sia vera o falsa. Rispondere correttamente contribuisce con 0.2 punti al punteggio totale, rispondere in modo erroneo comporta una penalizzazione di 0.1 punti, mentre non rispondere non comporta alcuna penalità.

### Con riferimento alla programmazione:

* Compilazione ed interpretazione sono sinonimi
* La compilazione è, in sostanza, un'operazione di traduzione
* L'interpretazione produce in output dei file eseguibili
* E' il solo aspetto rilevante nella cosiddetta "ingegneria del software"

### 2. Nella programmazione imperativa, con particolare riferimento al linguaggio JavaScript:
* Una variabile è un costrutto di controllo del flusso di un programma.
* Una espressione è costituita da una combinazione di operandi e operatori che, quando valutata, produce un valore.
* Il costrutto `if (a) {...} else {...}` consente di basare la scelta di un blocco di istruzioni da eseguire sul valore vero o falso di una espressione booleana `a`.
* I costrutti `for` e `while`, rispettivamente, definiscono una nuova funzione e la invocano.

### 3. Valuta l'output fornito dai seguenti listati di codice JavaScript:
{% highlight javascript %}
var a = 5;
var b = a + 3;
a = 0;
{% endhighlight %}
* A questo punto la variabile `b` conterrà il valore: `3`
{% highlight javascript %}
if(false){ console.log("A"); }
else if(true || false){ console.log("B"); }
else { console.log("C") }
{% endhighlight %}
* Verrà stampato a console la seguente stringa: `B`.
{% highlight javascript %}
var arr = [5,7,2];
arr[0] * arr.length
{% endhighlight %}
* Il valore dell'ultima espressione è: `15`
{% highlight javascript %}
var arr = [5,7,2,6,9];
for(var i = 0; i < arr.length; i++){
    if(arr[i] > 5 && arr[i] < 9) console.log(arr[i]);
}
{% endhighlight %}
* Verranno stampati a console i seguenti valori, nel seguente ordine: `7`, `6`.
{% highlight javascript %}
var rettangolo = {
    base: 2,
    altezza: 2,
    area: function(){ return this.base * this.altezza; }
};
rettangolo.altezza = 5;
rettangolo.area();
{% endhighlight %}
* Il risultato dell'ultima espressione è: `4`.


### 4. Con particolare riferimento al linguaggio JavaScript:
* Una funzione è un meccanismo che consente di astrarre una computazione rispetto al valore concreto di uno o più parametri; in altre parole, definisce la logica di produzione di un output a partire da zero o più input.
* Un oggetto incapsula sia stato (nella forma di proprietà) sia comportamento (nella forma di metodi).

## Mobile / XAMARIN

Vi verranno presentate tre domande a risposta multipla, di cui *una soltanto* corretta. Segnalare la risposta corretta fra quelle elencate. Ciascuna risposta corretta vale un punto. Omettere o sbagliare la risposta non dà alcun contributo al punteggio.

### 1. Che cosa s’intende per integrità referenziale

* A. Un sistema di regole che garantisce la validità delle relazioni tra i record delle tabelle correlate e che non vengano eliminati o modificati per errore i dati correlati.  
* B. Un sistema di regole che garantisce la validità delle relazioni tra i record delle tabelle non correlate  
* C. Un sistema di regole che attua la cancellazione di un insieme di records dalle tabelle  
* D. È una tipologia particolare di query  

### 2. La query `SELECT RAGSOC_CLIENTE , INDIRIZZO_CLIENTE FROM CLIENTE WHERE COD_CLI = 10` restituisce:

* A. La ragione sociale e l'indirizzo dei clienti del nostro database  
* B. La ragione sociale e l'indirizzo dei clienti del nostro database che hanno il codice cliente uguale 10.  
* C. Tutti i dati dei clienti del nostro database, escluso la ragione sociale e l’indirizzo  
* D. Tutti i dati dei clienti del nostro database  

### 3. Individuare la corretta affermazione sulla piattaforma XAMARIN

* A. Xmarin permette di realizzare applicazioni Android, iOS e UWP utilizzando il linguaggio C# 
* B. Xamarin Forms permette di rendere condivisa non solo la Business Logic, ma anche la User Interface di applicazioni mobile Android, iOS e UWP
* C. L'approccio MVVM (Model - View - ViewModel) non può essere utilizzato in Xamarin Forms 
* D. Non esiste un gestore delle dipendenze (per la tecnica della dependency injection) compatibile con Xamarin Forms
