from PIL import Image
from PIL.ExifTags import TAGS


caminho_imagem = "kaua_iamge.jpg"

img  = Image.open(caminho_imagem)

exif_data = img.getexif()
if exif_data:
    for tag_id,valor in exif_data.items():
        tag = TAGS.get(tag_id,tag_id)
        print(f"{tag:25}: {valor}")
else:
    print("SEM METADADOS EXIF😢")        