from datetime import datetime,timedelta
import cv2
from datetime import date
import os
from PIL import Image
import cv2
import numpy as np
import cv2
import matplotlib.pyplot as plt
today = date.today()
intervalo = timedelta(30)
contorna=False

while True:
    #try:
        l=os.listdir("./static/imagens/")
        #comparando as datas pra limpar os arquivos
        data=date.today()
        if data>=today+intervalo:
            print("virou o dia")
            for b in l:
                destino="./static/imagens/"+b
                os.remove(destino)
            today=data
            # o laço for deleta os arquivos de um dia para o outro
        # o laço for verifica os pdfs
        for b in l:
            # Load image, convert to grayscale, and find 
            print(b)
            nome=b
            caminho="./static/imagens/"+b
            image = cv2.imread(caminho)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

            # Find contour and sort by contour area
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

            # Find bounding box and extract ROI
            for c in cnts:
                x,y,w,h = cv2.boundingRect(c)
                ROI = image[y:y+h+20, x:x+w+30]
                break
            cv2.imwrite('ROI.png',ROI)
            # abre a imagem colorida
            img_colorida = Image.open('ROI.png')
            # converte a imagem para o modo L (escala de cinza)
            img_escala_de_cinza = img_colorida.convert('L')
            # salva a nova imagem
            img_escala_de_cinza.save(caminho)
            imagem = cv2.imread(caminho)
            altura=imagem.shape[0]
            largura=imagem.shape[1]
            print ("Altura (height): %d pixels" % (imagem.shape[0]))
            print ("Largura (width): %d pixels" % (imagem.shape[1]))
            print ("Canais (channels): %d"      % (imagem.shape[2]))
            (b, g, r) = imagem[0, 0]
            print ("Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b) ) 
            i=0
            a=0
            Rant=r
            for i in range(altura):
                for a in range(largura):
                    (b,g,r)=imagem[i,a]
                    if r>=Rant+2:
                        imagem[i,a]=(0,0,0)
                    if r<=Rant-2:
                        imagem[i,a]=(0,0,0)
                    else:
                        imagem[i,a]=(255,255,255)
                    Rant=r
                a=0
            c= './static/imagens_feitas/'+nome
            cv2.imwrite(c,imagem)
            
            os.remove(caminho)
    

    #except Exception as e:
        #print("erro:",e)
        #contorna=True
        #break