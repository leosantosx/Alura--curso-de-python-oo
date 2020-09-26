from model import Filme, Serie, Playlist

vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
atlanta = Serie('atlanta', 2018, 2)
enola_holmes = Serie('Enola Holmes', 2020, 124)
enola_holmes.dar_likes()
enola_holmes.dar_likes()
enola_holmes.dar_likes()
enola_holmes.dar_likes()

lista_filmes_e_series = [vingadores, atlanta, enola_holmes]
playlist = Playlist('Minha Playlist', lista_filmes_e_series)
print(f'Tamanho da playlist: {len(playlist)}')

for programa in playlist:
    print(programa)
