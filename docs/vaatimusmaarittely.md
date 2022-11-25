# Vaatimusmäärittely

## sovelluksen yleiskuvaus

Miinakenttä Mahjong perustuu [Japanilaiseen Riichi mahjongiin](https://en.wikipedia.org/wiki/Japanese_mahjong).

Pelin alussa molemmat pelaajat nostavat 34 tiiltä. Sen jälkeen he tekevät yhden päästä valmiin käden 13 tiilestä. (valmis käsi mahjongissa on yksi pari ja 4 settiä, missä setti on joko kolme samaa tiiltä tai kolme peräkkäistä). Kun molemmat pelaajat ovat valmiit, alkavat he vuorotellen heittämään pois 21 jäljelläolevaa tiiltä. Pelaajat voivat julistaa voiton toisen pelaajan poisheittämistä tiilistä, mutta ei omistaan. Kierros päättyy kun jompikumpi julistaa voiton tai kun molemmat ovat heittäneet pois 17 tiiltä.

## Käyttäjät

Pelissä on kaksi Pelaajaa. Pelaajat voivat olla joko ihmisiä tai tekoälyjä. Todennäköisesti kannattaa ohjelma toteuttaa ensin kahdelle pelaajalle, ja sitten myöhemmin voidaan ajan salliessa toteuttaa simppeli tekoäly.

## Perustoiminnallisuus
- Pelaajat saavat alussa tiilensä ja voivat valita kätensä
- Pelaajat voivat vuorotellen heittää tiilen pois
- pelaajat voivat julistaa voiton
- Käsien laillisuuden tarkistus
- Graafinen käyttöliittymä pelille

# jatkokehitus
- Peliin lisätään kertoimia ja niiden tarkistus
  - kertoimien hallitseminen (confi)tiedoston perusteella
  - kertoimien pisteenlasku
- Voittamiseen vähimmäis pisteraja
- minipisteet
- Dora ja Uradora
- Furiten-sääntö
