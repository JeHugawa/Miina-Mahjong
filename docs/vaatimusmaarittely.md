# Vaatimusmäärittely

## sovelluksen yleiskuvaus

Miinakenttä Mahjong perustuu [Japanilaiseen Riichi mahjongiin](https://en.wikipedia.org/wiki/Japanese_mahjong).

Pelin alussa molemmat pelaajat nostavat 34 tiiltä. Sen jälkeen he tekevät yhden päästä valmiin käden 13 tiilestä. (valmis käsi mahjongissa on yksi pari ja 4 settiä, missä setti on joko kolme samaa tiiltä tai kolme peräkkäistä). Kun molemmat pelaajat ovat valmiit, alkavat he vuorotellen heittämään pois 21 jäljelläolevaa tiiltä. Pelaajat voivat julistaa voiton toisen pelaajan poisheittämistä tiilistä, mutta ei omistaan. Kierros päättyy kun jompikumpi julistaa voiton tai kun molemmat ovat heittäneet pois 17 tiiltä.

## Käyttäjät

Pelissä on kaksi Pelaajaa. Pelaajat voivat olla joko ihmisiä tai tekoälyjä. Todennäköisesti kannattaa ohjelma toteuttaa ensin kahdelle pelaajalle, ja sitten myöhemmin voidaan ajan salliessa toteuttaa simppeli tekoäly.

## Perustoiminnallisuus
- [x] Pelaajat saavat alussa tiilensä ja voivat valita kätensä
- [x] Pelaajat voivat vuorotellen heittää tiilen pois
- [ ] pelaajat voivat julistaa voiton
- [x] Käsien laillisuuden tarkistus
- [x] Graafinen käyttöliittymä pelille
