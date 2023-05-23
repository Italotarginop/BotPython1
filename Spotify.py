import pyautogui
import time
from FunctionsSpotify import pesquisar_programa
from FunctionsSpotify import esperar_imagem_aparecer
from FunctionsSpotify import clicar_imagem_se_encontrada
from FunctionsSpotify import clicar_direito_se_encontrada
from FunctionsSpotify import rolar_barra_para_baixo
from FunctionsSpotify import pesquisar_musica
# Array de músicas
musicas = [
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

# --------------------------------------------------
# --------------------------------------------------

# Cadeia de + musica no spotify
pesquisar_programa('spot')
clicar_imagem_se_encontrada('maximizar.png')
#clicar_imagem_se_encontrada('sptEntrar.png', 10)

# Add/Nomear playlist
clicar_imagem_se_encontrada('addspt.png', 10)
clicar_imagem_se_encontrada('novaplay.png',10)
time.sleep(1)
clicar_imagem_se_encontrada('nomePlay.png',10)
pyautogui.write('Minha Playlist t2t')
clicar_imagem_se_encontrada('salvarNomePlay.png',10)
clicar_imagem_se_encontrada('nullPosNomearPlaylist.png', 2)

pyautogui.press('down',presses=3)
time.sleep(2)
# ATÉ AQUI, TUDO CERTO
#percorrendo array de musicas
for musica in musicas:
    time.sleep(1)
    clicar_imagem_se_encontrada('buscarArtistaMusica.png')
    pesquisar_musica(musica['artista'], musica['musica'])
    clicar_imagem_se_encontrada('incrementar.png', 5)
    time.sleep(1)
    pyautogui.press('down', presses=2)
    time.sleep(1)
    if not esperar_imagem_aparecer('addmusspt.png', 5):
        pyautogui.press('down', presses=2)
    else:
        clicar_imagem_se_encontrada('addmusspt.png', 5)

    clicar_imagem_se_encontrada('clickmeio.png', 2)
    clicar_imagem_se_encontrada('incrementar.png', 5)
    time.sleep(1)
    time.sleep(1)
    pyautogui.press('down', presses=2)
    time.sleep(1)
    clicar_imagem_se_encontrada('fecharpesqposadd.png',10)
    pyautogui.press('pageup')
   
# Apagar Playlists
while True:
    if not esperar_imagem_aparecer('cliquedireitoplay.png', 10):
        break
    clicar_direito_se_encontrada('cliquedireitoplay.png', 10)
    clicar_imagem_se_encontrada('apagar.png',10)
    clicar_imagem_se_encontrada('apagaresquerdo.png',10)




