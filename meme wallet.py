import eel
import os
import uuid

memes = []

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + '\web'
x = list(os.walk(dir_path))
for file in x[0][2]:
    if (file.endswith('.jpg') or file.endswith('.png')) and (file != 'previousArrow.jpg' and file != 'nextArrow.jpg'):
        #meme = dir_path +"\ "[0] +str(file)
        #print(file)
        meme = str(file)
        memes.append(meme)
        #print(meme)
#print(len(memes))
#print(memes[0])
#f = open(str(memes[0]))

@eel.expose
def otherMeme(next):
    global index
    if next == 1 and index < len(memesTags) - 1:
        index = index + 1
        eel.changeMeme(memesTags[index][0])
        updateTags(memesTags[index])
    elif next == 0 and index > 0:
        index = index - 1
        eel.changeMeme(memesTags[index][0])
        updateTags(memesTags[index])

f =  open('memes.txt','r')
j = 0
memesTags = []
for i in f:
    x = i[0:-1].split(' ')
    #print('x =',x)
    memesTags.append(x)
    #print(memesTags[j])
    #j = j + 1
#memesTags[0].remove('meme1tag1')
#print(memesTags)
#f.truncate(0)
f.close()

#if len(memesTags) == 0:
#    print("memes.txt is empty")
#    f2 = open('memes2.txt', 'r')
#    for i in f2:
#        x = i[0:-1].split(' ')
        # print('x =',x)
#        memesTags.append(x)
    #f2.truncate(0)
#    f2.close()


for i in memesTags:
    if i[0] not in memes:
        memesTags.remove(i)

for i in memes:
    j = 0
    while j < len(memesTags) and memesTags[j][0] != i:
        j = j + 1
    if j == len(memesTags):
        #print(dir_path+'\ '[0]+i, dir_path+'\ '[0]+str(uuid.uuid1())+'.'+i[-3:len(i)])
        print("I found that",i,"is not in the memes list, so I will index it now.")
        id = str(uuid.uuid4())
        os.rename(dir_path+'\ '[0]+i, dir_path+'\ '[0]+id+'.'+i[-3:len(i)])
        memesTags.append([id+'.'+i[-3:len(i)]])
        #newMemes.append([id+'.'+i[-3:len(i)]])


#print(memesTags)
index = 0
#print(memesTags[index][0])
#x = input()


@eel.expose
def addTagBackend(x):
    global index
    global memesTags
    if x != '':
        tag = x.lower()
        if tag not in memesTags[index]:
            memesTags[index].append(tag)
            #print("index =",index)
            #print(tag)
            eel.addTagFrontend(tag)


@eel.expose
def deleteTagBackend(x):
    global index
    global memesTags
    memesTags[index].remove(x)
    #print("Tag",x,"has been removed from",memesTags[index][0])
    #print(memesTags,"[",index,"] = ",memesTags[index],sep='')

@eel.expose
def updateTags(x):
    global index
    for i in range(1,len(x)):
        eel.addTagFrontend(x[i])

@eel.expose
def searchPython(x):
    #print(x,"is of type",type(x))
    x = x.split()
    #print(x,"is of type",type(x))
    foundMemes = []
    for i in memesTags:
        j = 1
        foundTags = []
        while j < len(i):
            for k in x:
                if i[j] == k:
                    foundTags.append(k)
            j = j + 1
        if len(foundTags) == len(x):
            foundMemes.append(i)
    for i in foundMemes:
        eel.addMeme(i)
@eel.expose
def start():
    eel.changeMeme(memesTags[index][0])
    updateTags(memesTags[index])

check = 0
@eel.expose
def PythonCheck():
    global check
    check = 1
    #print("check is now",check)

def close_callback(route, websockets):
    global check
    #print("check is now", check)
    global memesTags
    #print(route)
    if not websockets and check == 0:
        #print("OUT")
        f = open('memes.txt', 'w')
        f.truncate(0)
        memesTags2 = []
        for i in memesTags:
            memesTags2.append(" ".join(i) + '\n')
        f.writelines(memesTags2)
        f.close()
        exit()
    else:
        check = 0

#print(dir_path)
eel.init(dir_path)
#print("I will now ask JS to show image",memesTags[index][0])

#eel.draw(f)

eel.start('search.html',size = (698,407),block=True,close_callback=close_callback)
#print("Yo")
