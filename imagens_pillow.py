from PIL import Image

imagem = Image.open('git_logo.png')

#exibir Imagem
#imagem.show()

#comverter o formato da imagem
imagem_rgb = imagem.convert("RGB")
imagem_rgb.save('git_logo.jpg')