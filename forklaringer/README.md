
# Overblikk
Det kan være vanskelig å få oversikt over alle elementene vi snakker om når vi skal lære å jobbe med web-applikasjoner. Hva gjelder selve tjenesten? Hva er verktøy vi bruker som støtte under arbeidet.

Her følger et forsøk på å gi et overblikk over elementene og deres bruksområder.

## Web-applikasjon

Med en web-applikasjon mener vi i dette kurset et [program](#program) som 
* setter sammen nettsider (med data fra [database](#database) og html-kode)
* lagrer data som bruker legger inn på nettsidene

Vi skal lage en web-applikasjon som heter Kvittr i dette kurset. Web-applikasjoner brukes ofte til å lage [interaktive](#interaktive) [nettsider](#nettsider).

Siden en web-applikasjon er et program, så må vi bruke et programmeringsspråk for å skrive våre kommandoer i, og [Python](#python) er språket vi skal bruke.

Men vi ønsker ikke å skrive all koden selv. Derfor bruker vi 
[biblioteker](#bibliotek). 

Et av bibliotekene vi bruker for å lage Kvittr er [Django](#django). Vi installerer Django ved hjelp av [Pip](#pip).

### Request
Request er bare en *forespørsel*. I forbindelse med dette kurset snakker vi om [http](#http)-forespørsler. Forespørselen sendes til en server ut fra hvilken adresse ([url](#url)) vi har skrevet i nettleserens adressefelt.

### Response
Response er bare et *svar*. Dette er svaret som sendes på en [request](#request) til vår nettleser fra en gitt server.

### Program
Med et program mener vi et sett med kommandoer som til sammen gjør noe på en datamaskin. Kommandoene er som oftest listet opp i én eller flere filer.

### Python
Python er for oss 2 ting, og det kan være litt forvirrende. Vi bør prøve å ha klart for oss forskjellen på disse 2 tingene som er:
* Et programmeringsspråk
* Et program som vi kjører med kommandoen `python`

Programmeringsspråket Python er et av mange språk som er laget for å skrive kommandoer som skal utføres av en datamaskin.

Programmet Python, som vi har fått installert på vår maskin gjennom Xcode eller Cygwin, er et program som leser filer med kode skrevet i språket python, og utfører kommandoene der.

### Bibliotek
Ferdige programmer som vi kobler inn i vårt eget [program](#program). De fleste bibliotekene vi bruker laster vi ned og installerer i vår [virtuelle omgivelse](#virtuelle omgivelse) med verktøyet [Pip](#pip) og kommandoen `pip install`.

### Pip
`pip` er et program vi bruker for å laste ned og installere python [biblioteker](#biblioteker)

### Terminal-programmer som Cygwin og iTerm2
Terminal-programmer gjør det mulig for oss å gi kommandoer til datamaskinen. Det vi skriver inn, det gjøres. Det vil si, med mindre vi har skrevet noe feil. Datamaskiner er ikke veldig smarte, så kommandoen må være skrevet på en helt bestemt måte. 

Når vi skriver kommandoer i en terminal skriver kommandoer i programmeringsspråket `bash`. Eksempler på slike kommandoer er:
```bash
$> ls
$> mkdir thedirectory
$> cd thedirectory
```

### Git
Git er et program som vi installerer og bruker på vår datamaskin for holde oversikt over utviklingen av et program. Git gjør dette ved å lagre "tilstanden" på et gitt tidspunkt. Vi må selv si fra til git når vi vil at "tilstanden" skal lagres. Dette gjør vi med kommandoen `git commit`.   

Git har støtte for å syncronisere code til servere og tjenester som er koblet til internett. Et eksempel på en slik tjeneste er [Github](#github). Vi kan hente kode fra Github med kommandoen `git pull` og "skyve" vår kode til Github med `git push`. 

### Github
Github er et nettsted hvor vi kan lagre kode. I tillegg til å lagre kode har github diverse funksjonalitet som gjør at det er lettere å holde oversikt og samarbeide om koding.

### Nettsider
Nettsider er det vi til et gitt tid ser i vår nettleser. I mange tilfeller er det bare innholdet i en html-fil. Når vi går til en [url](#url) så hentes det html-kode fra en web-server til vår maskin, og det vises 

### Interaktive
En nettside som lar som lar brukeren bidra med innhold på siden. Eksempler på interaksjon er:
* Klikk på "Like" (som øker antall likes og dermed endrer innholdet)
* Legge til kommentar
* Legge til bilde

### Url
En url er en unik ID for en nettside, det som bestemmer hva som skal vises i vår nettleser. En url er på formen:
```
protokoll://underdomene.domene.toppdomene:port/sti/side
```
* **protokoll**: F.eks http eller https. Vi har i dette kurset også blitt kjent med `ssh` som vi bruker for å clone, pulle og pushe til github.
* **domene**: Et domene er et et navn for en IP-adresse.
* **toppdomene**: Den delen som sier noe om land som ´.no´, samt noen andre som ´.com´, ´.org´ og ´.net´.
* **underdomene**: Et domene som er en del av et annet domene. F.eks ´intranett.bedriften.no`.
* **port**: Hvilken port requesten skal sendes til. Vanlige nettsider hentes fra port 80, sikre sider (https) hentes fra 443.

### Database

## Django
Django er et stort [Python](#python) [bibliotek](#bibliotek) som gir oss ferdigskrevet kode for mange av de vanlige tingene vi må gjøre når vi lager 
web-applikasjoner.

### Settings
Dette er innstillinger for en [Web-applikasjon](#web-applikasjon) laget med Django. Disse er lagret i en fil med navn `settings.py`.

### Models
Vi bruker begrepet *modeller* om [Python](#python)-klasser som viser en  

### Urls

### Views

### Templates

### Migrations
*Migrations* kan vi tenke på som "endringer i databasen". En endring kan være:
* en ny tabell
* en ny kolonne i en tabell
* sletting av en kolonne i en tabell
* osv.








