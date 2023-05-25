import pyautogui
import time
from FunctionsSpotify import pesquisar_programa
from FunctionsSpotify import esperar_imagem_aparecer
from FunctionsSpotify import clicar_imagem_se_encontrada
from FunctionsSpotify import clicar_direito_se_encontrada
from FunctionsSpotify import rolar_barra_para_baixo
from FunctionsSpotify import pesquisar_musica
# Array de músicas


class Spotify:
    def __init__(self):
        self.musicas = [
            {'artista': 'Elvis Presley ', 'musica': 'unchained melody'},
            {'artista': 'Shakira ', 'musica': 'africa'},
            {'artista': 'Iron Maiden ', 'musica': 'wasted years'},
            {'artista': 'Bob Marley ', 'musica': 'is this love'},
            {'artista': 'rita lee ', 'musica': 'ovelha negra'},
            {'artista': 'Jorge Arag ', 'musica': 'identidade'},
            {'artista': 'beatles ', 'musica': 'let it be'},
            {'artista': 'eagles ', 'musica': 'hotel california'},
            {'artista': 'beegees ', 'musica': 'alive'},
            {'artista': 'pearl jam ', 'musica': 'even flow'},
        ]
    def abrir_spotify(self):
        pesquisar_programa('spot')
        clicar_imagem_se_encontrada('maximizar.png')
    
    def add_playlist(self):
        clicar_imagem_se_encontrada('addspt.png', 10)
        clicar_imagem_se_encontrada('novaplay.png',10)
        time.sleep(1)
        clicar_imagem_se_encontrada('nomePlay.png',10)
        pyautogui.write('Minha Playlist t2t')
        clicar_imagem_se_encontrada('salvarNomePlay.png',10)
        clicar_imagem_se_encontrada('nullPosNomearPlaylist.png', 2)

    def toques_p_baixo(self):
        pyautogui.press('down',presses=3)
        time.sleep(2)
    
    def apagar_playlist_enquanto_ouver(self):
        while True:
            if not esperar_imagem_aparecer('cliquedireitoplay.png', 10):
                break
        clicar_direito_se_encontrada('cliquedireitoplay.png', 10)
        clicar_imagem_se_encontrada('apagar.png',10)
        clicar_imagem_se_encontrada('apagaresquerdo.png',10)

    def criar_playlist(self):
                
        self.abrir_spotify()
        self.add_playlist()
        self.toques_p_baixo()
        
        for musica in self.musicas:
            time.sleep(1)
            clicar_imagem_se_encontrada('buscarArtistaMusica.png')
            pesquisar_musica(musica['artista'], musica['musica'])
            clicar_imagem_se_encontrada('incrementar.png', 5)
            time.sleep(1)
            pyautogui.press('down', presses=2)
            time.sleep(1)
            esperar_imagem_aparecer('addmusspt.png', 5)
            pyautogui.press('down', presses=2)
            clicar_imagem_se_encontrada('fecharpesqposadd.png')
            clicar_imagem_se_encontrada('addmusspt.png', 5)
            clicar_imagem_se_encontrada('fecharpesqposadd.png')
            
Spotify().apagar_playlist_enquanto_ouver()

        



# --------------------------------------------------

Spotify().criar_playlist()
# Spotify().apagar_playlist_enquanto_ouver()


'''# Add/Nomear playlist - tranformar em função
clicar_imagem_se_encontrada('addspt.png', 10)
clicar_imagem_se_encontrada('novaplay.png',10)
time.sleep(1)
clicar_imagem_se_encontrada('nomePlay.png',10)
pyautogui.write('Minha Playlist t2t')
clicar_imagem_se_encontrada('salvarNomePlay.png',10)
clicar_imagem_se_encontrada('nullPosNomearPlaylist.png', 2)

# Trasformar em função
pyautogui.press('down',presses=3)
time.sleep(2)'''

# ATÉ AQUI, TUDO CERTO
spotify = Spotify()



   
# Apagar Playlists enquanto ouver.
'''
while True:
    if not esperar_imagem_aparecer('cliquedireitoplay.png', 10):
        break
    clicar_direito_se_encontrada('cliquedireitoplay.png', 10)
    clicar_imagem_se_encontrada('apagar.png',10)
    clicar_imagem_se_encontrada('apagaresquerdo.png',10)

'''


