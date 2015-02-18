# Obligatorisk innlevering

Dette er den obligatoriske innleveringen i kurset ITM30614 våren 2015. Besvarelsen skal leveres senest *fredag 6. mars*. Du skal lage en enkel django-applikasjon ved å gå gjennom alle punktene i "part 1", "part 2" og "part 3" av den offisielle Django-tutorialen. Kataloger og filer du lager når du går gjennom tutorial-en skal legges i et repository på github. Repositoriet skal være offentlig. 


## Virtual environent og mappestruktur

Du må bruke et _virtual environment_ når du jobber med django-tutorialen. For at det skal være enkelt å holde oversikt over hvor du har dine django-prosjekter og den tilhørende virtuelle omgivelsen anbefales følgende katalogstruktur:

    ├── itm30614code
    │   ├── djangoprojects
    │   │   ├── django-oblig (et github repository)
    │   │   └── kvittr (et github repository)
    │   └── virtualenvironments
    │       ├── django-oblig (virtual env for djangoprosjektet "django-oblig")
    │       └── kvittr (env for "kvittr")

Husk at du ikke selv skal røre noe inne i katalogen `virtualenvironments`, det er verktøyet `virtualenv` som skal ha kontroll i denne.

### Hvordan bruke `virtualenv`?

Antar at du først har laget repositoriet `django-oblig` for obligen på github.

```bash
# Installer virtualenv fra python cheese shop med pip
$> pip install virtualenv
# Lag en virtuall omgivelse med navn django-oblig
$> virtualenv virtualenvironments/django-oblig
# Aktiver omgivelsen (deaktiver den med kommandoen "deactivate")
$> source virtualenvironments/django-oblig/bin/activate
# Legg merke til at vårt "prompt" nå er endret for å vise at vi er i en virtuell omgivelse
(django-oblig)$> ls
    djangoprojects      virtualenvironments
(django-oblig)$> cd djangoprojects/
(django-oblig)djangoprojects $> ls
    kvittr
# Hent github repositoriet du har laget, og skal bruke for oblig
(django-oblig)djangoprojects $> git clone git@github.com:apparator/django-oblig.git
    Cloning into 'django-oblig'...
(django-oblig)djangoprojects $> cd django-oblig/
# Legg merke til at repositoriet og den virtuelle omgivelsen har samme navn (anbefales)
(django-oblig)django-oblig $> ls
    README.md    myprojectname
# Installer Django, i den virtuelle omgivelsen
(django-oblig)django-oblig $> pip install Django
    Successfully installed Django
```

Med disse kommandoene skal du ha det du trenger for å starte med å gå gjennom del 1, 2 og 3 av django-tutorialen.

## Django tutorial

* https://docs.djangoproject.com/en/1.7/intro/tutorial01/
* https://docs.djangoproject.com/en/1.7/intro/tutorial02/
* https://docs.djangoproject.com/en/1.7/intro/tutorial03/

## Om bruk av git underveis i arbeidet med obligen

Husk å:
* gjøre mange commits
* beskrive kort og/men godt hva du har gjort siden sist du commitet

Her følger eksempler på bruk av git mens du jobber med oppgaven:

```bash
# For å se hva som er endret siden sist:
$> git status
# De filene git status viser som "modified" eller "new" legger du neste commit med:
$> git add
# Legg til et nytt punkt i historikken (tidslinjen til prosjektet)
$> git commit
# Send endringene du har gjort til github
$> git push
# Hent nye endringer fra github (ikke så aktuelt i arbeid med oblig), men gjør det allikevel :-)
$> git pull
```

Hvis det er editoren vim som starter når du kjører kommandoen `git commit` kan det være litt uvant å komme seg videre. For å lagre og lukke vim trykk ´Esc´, skriv `:wq` (vises nede til høyre) og klikk `Enter`. For å få ´nano` til å starte i stedet for `vim` ved `git commit` kjør følgende kommando:

    git config --global core.editor "nano"


## Til slutt litt om

Det kan bli gjort endringer i denne teksten dersom vi får tilbakemeldinger på at mer informasjon ønskes. 

Dere vil få nærmere beskjed om hvordan besvarelsen skal leveres.









