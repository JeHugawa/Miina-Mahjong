# miinakenttä Mahjong
miinakenttä Mahjong joka perustuu riichimahjongiin

# Pelin tarkoitus

Miinakenttä Mahjong perustuu [Japanilaiseen Riichi mahjongiin](https://en.wikipedia.org/wiki/Japanese_mahjong). Riichin sääntöjä ei kuitenkaan tarvitse osata, sillä Miinakenttä on kahden pelaajan muunnos missä on yksinkertaisemmat säännöt.
___

Pelin alussa molemmat pelaajat nostavat 34 tiiltä. Sen jälkeen he tekevät yhden päästä valmiin käden 13 tiilestä. (valmis käsi mahjongissa on yksi pari ja 4 settiä, missä setti on joko kolme samaa tiiltä tai kolme peräkkäistä). Kun molemmat pelaajat ovat valmiit, alkavat he vuorotellen heittämään pois 21 jäljelläolevaa tiiltä. Pelaajat voivat julistaa voiton toisen pelaajan poisheittämistä tiilistä, mutta ei omistaan. Kierros päättyy kun jompikumpi julistaa voiton tai kun molemmat ovat heittäneet pois 17 tiiltä.

## Dokumentaatio
- [Säännöt](./docs/saannot.md)
- [Käyttöohje](./docs/kayttoohje.md)
- [Työaikakirjanpito](./docs/tuntikirjanpito.md)
- [Changelog](./docs/changelog.md)
- [Määrittelydokumentti](./docs/vaatimusmaarittely.md)
- [Luokkakaavio](./docs/luokkakaavio.png)

## käyttöohjeet

Asenna projekti ajamalla:
```
poetry install
```

Voit ajaa projektin ajamalla:
```
poetry run invoke start
```
Voit ajaa UI version ajamalla:
```
poetry run invoke startui
```

## kehityskomennot

testit ajetaan komennolla:
```
poetry run invoke test
```
Testikattavuusraportin saa ajamalla:
```
poetry run invoke coverage-report
```
pylintin saa vastaavasti:
```
poetry run invoke pylint
```
# License

Mahjong tileset designed by Code Inferno www.codeinferno.com
