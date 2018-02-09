from PIL import Image
from numpy import*
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def mask_pixel(arr):
    for i in range(21):
        for j in range(21):
            if not ((i<=8 and j<=8) or (i<=8 and j>=13) or (i>=13 and j<=8) or ((i==10 or i==12) and j==6) or (i==6 and (j==10 or j==12))):
                if not((i+j)%3):
                    #print('(i,j)=',i,j)
                    if(arr[i][j]==0):
                        arr[i][j]=1
                    else:
                        arr[i][j]=0

format_info= {'l':['111011111000100', '111001011110011', '111110110101010', '111100010011101', '110011000101111', '110001100011000', '110110001000001', '110100101110110' ],
              'm':['101010000010010', '	101000100100101', '101111001111100', '101101101001011', '100010111111001', '100000011001110', '100111110010111', '100101010100000'],
              'q':['011010101011111', '011000001101000', '011111100110001', '	011101000000110', '010010010110100', '010000110000011', '010111011011010', '010101111101101'],
              'h':['001011010001001', '001001110111110', '001110011100111', '001100111010000', '000011101100010', '000001001010101', '000110100001100', '000100000111011']
              }

def fillFormatInfo(arr, formatString):
    k=0
    for j in range(6):
        arr[8][j]=(int)(formatString[k])
        arr[20-j][8]= (int)(formatString[k])
        k+=1
    arr[8][7]=arr[14][8]=(int)(formatString[k])
    k+=1
    arr[8][8]=arr[8][13]= (int)(formatString[k])
    k+=1
    arr[7][8]=arr[8][14]= (int)(formatString[k])
    k+=1
    for i in range(6):
        arr[5-i][8]=(int)(formatString[k])
        arr[8][i+15]= (int)(formatString[k])
        k+=1
    
    

com_arr=[
    [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],
    [1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1],
    [0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0],
    [1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1],
    [1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0],
    [1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1],
    [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0],
    [1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0],
    [1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0],
    [1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0],
    [1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0],

    ]



def neg_mat(arr):
    for i in range(21):
        for j in range(21):
            if(arr[i][j]==0):
                arr[i][j]=1
            else:
                arr[i][j]=0




encodedWords=[32, 91, 11, 120, 209, 114, 220, 77, 67, 64, 236, 17, 236, 17, 236, 17, 196,  35,  39,  119,  235, 215,  231,  226,  93,  23]
encodedWords= list(map(lambda x:'{0:08b}'.format(x), encodedWords))


def move_up_n(i,j,word):
    k=0
    flag=False
    if i==8 and j==12:
        flag=True
    while k<=7:
        if flag and k==4:
            i-=1
        com_arr[i][j]=(int)(word[k])
        k+=1
        com_arr[i][j-1]=(int)(word[k])
        k+=1
        i-=1

def move_down_n(i,j,word):
    k=0
    flag=False
    if i==4 and j==10:
        flag=True
    while k<=7:
        if flag and k==4:
            i+=1
        com_arr[i][j]=(int)(word[k])
        k+=1
        com_arr[i][j-1]=(int)(word[k])
        k+=1
        i+=1

print('#for words 1,2 and 3- Move Up')
i=20
for k in range(3):
    move_up_n(i,20,encodedWords[k])
    i-=4

print('#for words 4,5 and 6- Move Down')
i=9
for k in range(3,6):
    move_down_n(i,18,encodedWords[k])
    i+=4


print('#for words 7,8 and 9- Move Up')
i=20
for k in range(6,9):
    move_up_n(i,16,encodedWords[k])
    i-=4

print('#for words 10,11 and 12- Down')
i=9
for k in range(9,12):
    move_down_n(i,14,encodedWords[k])
    i+=4

print('#for words 13,14, 15, 16 and 17- Move Up')
i=20
for k in range(12,17):
    if(k==16):
        i=3
    move_up_n(i,12,encodedWords[k])
    i-=4
    
print('#for words 18,19,20,21,22 - Down')
i=0
for k in range(17,22):
    if(k==19):
        i=9
    move_down_n(i,10,encodedWords[k])
    i+=4

print('#for word 23')
move_up_n(12,8,encodedWords[22])

print('#for word 24')
move_down_n(9,5,encodedWords[23])

print('#for word 25')
move_up_n(12,3,encodedWords[24])

print('#for word 26')
move_down_n(9,1,encodedWords[25])



print('comMatrix')
print(com_arr)

fillFormatInfo(com_arr, format_info['m'][3])


mask_pixel(com_arr)

neg_mat(com_arr)

plt.imsave('C:\\Users\\HARIHARAN\\Desktop\\format_img.png', np.array(com_arr).reshape(21, 21), cmap=cm.gray)
