from funkcije import *

film = open("Film.txt", encoding = "utf8").read().lower()
music = open("Music.txt", encoding = "utf8").read().lower()
games = open("Games.txt", encoding = "utf8").read().lower()

model_fmg = zagladi({"Film":(frek_distr(opojavnici(film))), "Music":(frek_distr(opojavnici(music))), "Games":(frek_distr(opojavnici(games)))})

film_test = open("Film_test.txt", encoding = "utf8")
music_test = open("Music_test.txt", encoding = "utf8")
games_test = open("Games_test.txt", encoding = "utf8")

tocni = 0
svi = 0.0

for red in film_test:
    red = red.lower()
    print(klasificiraj(opojavnici(red), model_fmg))
    svi+=1
    if klasificiraj(opojavnici(red), model_fmg) == "Film":
        tocni+=1
    
print("\n")
    
for red in music_test:
    red = red.lower()
    print(klasificiraj(opojavnici(red), model_fmg))
    svi+=1
    if klasificiraj(opojavnici(red), model_fmg) == "Music":
        tocni+=1  

print("\n")

for red in games_test:
    red = red.lower()
    print(klasificiraj(opojavnici(red), model_fmg))
    svi+=1
    if klasificiraj(opojavnici(red), model_fmg) == "Games":
        tocni+=1
        
print("\n")

tocnost = tocni/svi

print("Točnost: " + str(tocnost*100) + "%")

