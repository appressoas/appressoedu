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
    $> pip install virtualenv
    $> virtualenv virtualenvironments/django-oblig
    $> source virtualenvironments/django-oblig/bin/activate
    (django-oblig)$> ls
        djangoprojects      virtualenvironments
    (django-oblig)$> cd djangoprojects/
    (django-oblig)djangoprojects $> ls
        kvittr
    (django-oblig)djangoprojects $> git clone git@github.com:apparator/django-oblig.git
        Cloning into 'django-oblig'...
    (django-oblig)djangoprojects $> cd django-oblig/
    (django-oblig)django-oblig $> ls
        README.md    myprojectname
    (django-oblig)django-oblig $> pip install Django
        Successfully installed Django
        Cleaning up...
```

## Django tutorial

* https://docs.djangoproject.com/en/1.7/intro/tutorial01/
* https://docs.djangoproject.com/en/1.7/intro/tutorial02/
* https://docs.djangoproject.com/en/1.7/intro/tutorial03/