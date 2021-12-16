from random import sample  # Tuodaa random moduulista luokka sample
import string  # Tuodaan string moduuli merkkijonojen erottelua varten


def luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkki: bool):

    tulostus = ''  # Lopullinen tulostettava muoto siistittynä
    kirjaimet = string.ascii_lowercase  # ASCII-kirjaimet lowercase
    numerot1 = string.digits  # numerot 0-9
    erikoismerkit = string.punctuation  # Erikoismerkit
    salasana = ''  # Tänne tallennetaan sample-metodin rakentama salasana

    if numerot and erikoismerkki:  # Jos molemmat parametrinä saadut argumentit True, otetaan kaikki merkit mukaan
        kaikki = kirjaimet + numerot1 + erikoismerkit
        salasana = sample(kaikki, pituus)

    if numerot and not erikoismerkki:  # Pelkästään numerot ja kirjaimet
        kaikki = kirjaimet + numerot1
        salasana = sample(kaikki, pituus)

    if erikoismerkki and not numerot:  # Pelkästään kirjaimet ja erikoismerkit
        kaikki = kirjaimet + erikoismerkit
        salasana = sample(kaikki, pituus)

    if not erikoismerkki and not numerot:  # Pelkästään kirjaimet
        salasana = sample(kirjaimet, pituus)

    for i in salasana:  # Siistitään tulostusmuoto
        tulostus += i

    return tulostus


def kayttoliittyma():
    numerot = False
    erikoismerkki = False
    
    pituus = int(input('Anna salasanan pituus: '))

    kaytetaanko_numeroita = input('Käytetäänkö numeroita? (K/E) ')
    if kaytetaanko_numeroita.lower() == 'k':
        numerot = True
    
    kaytetaanko_merkkeja = input('Käytetäänkö erikoismerkkejä? (K/E) ')
    if kaytetaanko_merkkeja.lower() == 'k':
        erikoismerkki = True
    
    print(luo_hyva_salasana(pituus, numerot, erikoismerkki))
    


if __name__ == '__main__':
    pass
kayttoliittyma()

