def uvecaj_za_jedan(broj):
    return broj + 1

def je_li_duljina_parna(iterabilni):
    return len(iterabilni)%2 == 0

def broj_samoglasnika(niz):
    rezultat = 0
    for znak in niz:
        if znak.lower() in "aeiou":
            rezultat+=1
    return rezultat

def frek_distr(sekvenca):
    rjecnik = {}
    for dogadjaj in sekvenca:
        rjecnik[dogadjaj] = rjecnik.get(dogadjaj, 0) + 1
    return rjecnik

def sortiraj_distr(rjecnik):
    return sorted(rjecnik.items(), key = lambda x:-x[1])

def opojavnici(niz):
    import re
    return re.findall(r'\w+', niz,re.UNICODE)

def vjer_distr(distr):
    broj_dogadjaja = sum(distr.values())
    for dogadjaj in distr:
        distr[dogadjaj] /= broj_dogadjaja
    return distr

def vjer_sekv(sekvenca, vjer_distr):
    from math import log
    vjerojatnost = 0
    for dogadjaj in sekvenca:
        if dogadjaj in vjer_distr:
            vjerojatnost+=log(vjer_distr[dogadjaj])
    return vjerojatnost

def zagladi(model):
    svi_dogadjaji = set()
    for klasa in model:
        for dogadjaj in model[klasa]:
            svi_dogadjaji.add(dogadjaj)
    for klasa in model:
        for dogadjaj in svi_dogadjaji:
            model[klasa][dogadjaj] = model[klasa].get(dogadjaj, 0) + 1
        model[klasa] = vjer_distr(model[klasa])
    return model

def klasificiraj(sekvenca, model):
    vjer = {}
    for klasa in model:
        vjer[klasa] = vjer_sekv(sekvenca, model[klasa])
    return sortiraj_distr(vjer)[0][0]


#####


if __name__ == "__main__":
    print(uvecaj_za_jedan(5))
    print(je_li_duljina_parna("Mamaaaaa"))
    print(broj_samoglasnika("The quick brown fox jumps over the lazy dog."))
    print(frek_distr("aaaaeeeaaaooooooaaaaa"))
    sortiraj_distr({"a":8, "x":135, "c":7})
    print(opojavnici("The quick brown fox jumps over the lazy dog."))
    print(vjer_distr(frek_distr("The quick brown fox jumps over the lazy dog.")))
    print(vjer_sekv("aeiouaaae", vjer_distr(frek_distr("The quick brown fox jumps over the lazy dog."))))
    m ={"m1":{"z":3,"p":8},"m2":{"8":17,"z":11}}
    print(zagladi(m))
    print(klasificiraj("zpppaz", m))
    print(klasificiraj("z8888zp", m))