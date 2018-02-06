from PIL import Image
from numpy import*
img_arr=[
    [1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0],
    [0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0],
    [1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1],
    [1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0],
    [1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0],
    [1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0],
    [1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0],
    [1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0],

    ]

def mask_pixel:
    for i in range(20):
        for j in range(20):
            if not ((i<=8 and j<=8) or (i<=8 and j>=13) or (i>=13 and j<=8) or ((i==10 or i==12) and j==6) or (i==6 and (j==10 or j==12)))
                if not((i+j)mod3):
                    if(img_arr[i][j]==0):
                        img_arr[i][j]=1
                    else:
                        img_arr[i][j]=0
for i in range(21):
    for j in range(21):
        if(img_arr[i][j]==0):
            img_arr[i][j]=1
        else:
            img_arr[i][j]=0

img=Image.new('1',(21,21))
pixels=img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
            pixels[i,j]=img_arr[i][j]
img.save('Sout.png')
