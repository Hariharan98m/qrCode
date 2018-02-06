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




com_arr=[
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



def neg_mat(arr):
    for i in range(21):
        for j in range(21):
            if(arr[i][j]==0):
                arr[i][j]=1
            else:
                arr[i][j]=0




encodedWords=[32, 65, 205, 69, 41, 220, 46, 128, 236, 42, 159, 74, 221, 244, 169, 239, 150, 138, 70, 237, 85, 224, 96, 74, 219, 61]
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


mask_pixel(com_arr)

neg_mat(com_arr)

plt.imsave('C:\\Users\\HARIHARAN\\Desktop\\hari_img.png', np.array(com_arr).reshape(21, 21), cmap=cm.gray)
