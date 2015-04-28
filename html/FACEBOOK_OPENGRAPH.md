# Open Graph

## Få deling på Facebook til å virke bra

Vi husker at vi brukte `head` taggen i html for å gi beskjeder til nettleseren. I denne
plasserer vi også beskjeder til Facebook dersom vi ønsker å kontrollere hva som blir vist 
i delingen. Vi bruker da Facebooks _Open Graph_.

Vi har en nettside, f.eks `http://kvittr.no/meldinger/111` og hvis noen deler denne på
facebook så ønsker vi at teksten skal være sånn og sånn, bildet skal være det vi selv velger osv.
Da legger vi inn følgende i `head` på nettsiden:

```html
    <meta property="og:title" content="Ny Kvittr-melding!" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="kvittr.no" />
    <meta property="og:description" content="Bla bla bla. Dette er meldingsteksten." />
    <meta property="og:url" content="http://kvittr.no/meldinger/111" />
    <meta property="og:image" content="http://kvittr.no/images/r243.png" />
    <meta property="og:image:secure_url" content="http://kvittr.no/images/r243.png" />
```

Det som er viktig å få med seg om dette nå er bare at vi kan gi beskjeder til Facebook om hvordan 
noe som deles fra vår nettside skal presenteres.

## Få deling på Twitter til å virke bra

For å kontrollere deling til Facebook bruker vi _Twitter Cards_. Dette er omtrent det samme som facebook. Les mer om dette her: https://dev.twitter.com/cards/overview


