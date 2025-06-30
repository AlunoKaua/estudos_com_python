from PIL import Image
from PIL.ExifTags import TAGS
import os

try:
    for raiz, subpastas, arquivos in os.walk(r"C:\Users\kaua.goncalves\Pictures"):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".jpg"):
                caminho = os.path.join(raiz, arquivo)
                imagem = Image.open(caminho)
                metadados = imagem.getexif()
                
                if metadados:
                    print(f"\n{'='*100}\nMETADADOS DE {caminho}\n{'='*100}")
                    for tag_id, valor in metadados.items():
                        tag = TAGS.get(tag_id, tag_id)
                        print(f"{tag:25}: {valor}")
                else:
                    print(f"\nNENHUM METADADO EM: {caminho}")

except Exception as erro:
    print(f"ERRO: {erro}")

finally:
    print("VARREDURA FINALIZADA. SE NÃO APARECEU NADA, NÃO TEM METADADOS OU AS IMAGENS NÃO FORAM ENCONTRADAS.")
