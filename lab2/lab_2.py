
# coding: utf-8

# In[2]:


# level_1 task_1

def addText(textToAdd, address):
    '''додає вкінець файлу за адресою address текст textToAdd '''
    
    
    rFile = open(address)
    text1 = rFile.read()
    rFile.close()
    
    text1+=textToAdd
    
    wFile = open(address,"w")
    wFile.write(text1)
    
addText("то Юра","E:\\programming\\python\\study\\labs\\aP\\lab2\\file1.txt" )


# In[3]:


# level_1 task_2

wText = '''
Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
Семя вечеря коло хати,
Вечірня зіронька встає,
Дочка вечерять подає,
А мати хоче научати,
Так соловейко не дає.
Поклала мати коло хати
Маленьких діточок своїх;
Сама заснула коло їх.
Затихло все, тілько дівчата
Та соловейко не затих.
'''
address = "E:\\programming\\python\\study\\labs\\aP\\lab2\\a.txt"
addressb1 = "E:\\programming\\python\\study\\labs\\aP\\lab2\\b1.txt"
addressb2 = "E:\\programming\\python\\study\\labs\\aP\\lab2\\b2.txt"

file1 = open(address,"w")
file1.write(wText)
file1.close()

file2 = open(address)
rText = file2.read()
file2.close()


linecount = 0

textB1 = ""
textB2 = ""

for i in range(len(rText)):
    
    if rText[i] == "\n":
        linecount+=1
    if linecount %2 == 0:
        textB1 += rText[i].upper()
    else:
        textB2 += rText[i].lower()


file1 = open(addressb1, "w")
file1.write(textB1)
file1.close()

file2 = open(addressb2, "w")
file2.write(textB2)
file2.close()


# In[117]:


# level_2 task_3

address = "E:\\programming\\python\\study\\labs\\aP\\lab2\\c.xml"
word = ""
# масив слів
wordArr = []

for i in range(len(wText)):
    
    if wText[i].isalnum():
        word += wText[i]
    else:
        if(word!=""):
            wordArr.append(word.lower())
            word = ""

print(wordArr)

uniqueWordArr = []
for i in range(len(wordArr)):
    if not uniqueWordArr.count(wordArr[i]):
        uniqueWordArr.append(wordArr[i])
        uniqueWordArr[i] += ": " + str(wordArr.count(wordArr[i]))
        

file = open(address, "w")
file.write("; ".join(uniqueWordArr))
file.close()



# In[148]:


# level_2 task_4
import re
import string


# створення масиву трьох останніх літер/букв слова
ends = re.findall(r"\w\w\w\b", wText)


# вирахування всіх закінчень з повтореннями, добавлення їх в масив
sameEnds = []
for i in range(len(ends)):
    sameEnds.append(re.findall(ends[i], " ".join(ends)))    
    
    
# визначення закінчень, котрі повторюються лишній раз, присвоєння їм []
for i in range(len(sameEnds)):
    
    for j in range(i+1,len(sameEnds)):
        if sameEnds[i] == sameEnds[j]:
            sameEnds[j] = []
        pass
    pass


# унікальні повторення закінченнь без лишніх повторень, новий масив без []
uSameEnds = []

for i in range(len(sameEnds)):
    if (sameEnds[i] != []):
        uSameEnds.append(sameEnds[i])


# масив кортежів(слово, рядок, номер)
word_tuple = ()

for i in range(len(uSameEnds)):
    tempEnd = uSameEnds[i][0]
    #print("[закінчення]:",tempEnd, end=" ")
    
    # кількість слів з однаковим закінченням temp end
    wordNum = (len(uSameEnds[i]))
    #print("[кількість]:", wordNum, end=" ")
    
    
    # масив зі слів до кожного закінчення
    wordArr = re.findall(r"\w*"+uSameEnds[i][0]+r"\b", wText)
    #print("[слова]:", wordArr, end = "\n")
    
    word_tuple += (tempEnd, wordNum, wordArr)
    
    #print(tempEnd, wordNum, wordArr, sep=", ", end="\n")
print(word_tuple)


# запис у xml
filename = "E:\\programming\\python\\study\\labs\\aP\\lab2\\c4.xml"

with open(filename, "wt") as fileobj:
    fileobj.write(str(word_tuple))
    


# In[ ]:


# level_2 task_4 UNRELEASED
   
   # номер рядка того слова
           # заміняю /n на 99 бо /n не входить в ".*"
   wText1 = re.sub(r"\n","99", wText)
   rowStr = re.findall(r".*"+wordArr[0], wText1.lower())
   for j in range(len(wordArr)):
       
       # знайти останнє входження слова, порахувати рядок і номер, обрізати стрічку пошуку до рядка з даним словом,
       # поки findall не буде False
       
           # обрізаю всю стрічку до потрібного слова(останнє входження)        
       # рахую кількість 99(\n) = к-к рядка
       rowNum = len(re.findall(r"99", str(rowStr).lower()))
           
       
       # міняю кінцеве слово на ""
       rowStr1 = re.sub(wordArr[j]+r"\S", "", str(rowStr))
       
       # обрізаю всю стрічку до потрібного слова(останнє входження)
       rowStr = re.findall(r".*"+wordArr[j], rowStr1)
       
   
       #print("[рядок]:", rowNum, end=" ")

                           
       #номер слова в рядку
           #пошук стрічки з заданим словом
       wordNumStr = re.findall(r"\n.*"+wordArr[j], wText)
           
           # кількість пробілів +1 = к-к слів
       wordNum = len(re.findall(r" ", str(wordNumStr)))+1
       
       
       temp_tuple = ()
       temp_tuple = wordArr[j], rowNum, wordNum
       word_tuple.append(temp_tuple)
       
       
       #print("[слово]:", wordNum)

