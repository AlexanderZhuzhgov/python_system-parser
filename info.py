#!/usr/bin/env python3.8
"""
Импортируем библиотеку os и библиотеку tkinter
Библиотека os работает с файлами системы
Библиотека tkinter отвечает за работу графического интерфейса
"""
import os
from tkinter import *
"""
lshw - файл создаваемый линуксом с информацией о комплектующих компьютера
Для получения информации о комплектующих мы должны вывести информацию данного файла и прочитать его
"""
pipe_hw = open('/home/moro/Downloads/Telegram Desktop/Мой lshw', 'r')
text = pipe_hw.read()

"""
sysinfo - список для последующего выведения информации в файл sysinfo
"""
sysinfo = []
 
"""
def getnamegpu() - данная функция предназначена для англоязычной системы и ищет информацию в файле lshw о видеокарте
Информация о видеокарте в данном файле лежит между строчками *-display и *-pnp
В строчке *-display есть подстрочка product которая отвечает за информацию о видеокарте
Поэтому, для выведения информации о видеокарте мы выводим отношение строчки product и следующей строчки
в данном случае это строчка vendor
После получения информации о видеокарте, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
""" 
def getnamegpu():
    gpu = text.find("  *-display")
    pnp = text.find("*-pnp")
    namegpuless = text.find("product", gpu, pnp)
    namegpuless2 = text.find("vendor", gpu, pnp)
    objectivegpu = text[namegpuless:namegpuless2]
    objectivegpu2 = objectivegpu[7:]
    left = objectivegpu2.find('[')
    right = objectivegpu2.find(']')
    word = "Integrated graphics"
    if word in objectivegpu:
        sysinfo.append('Ваша видеокарта:Встроенна в процессор' + '\n')
        return sysinfo
    else:
        sysinfo.append('Ваша видеокарта:' + objectivegpu2[left + 1:right] + '\n')
        return sysinfo
"""
def getnamecpu() - данная функция предназначена для англоязычной системы и ищет информацию в файле lshw о процессоре
Информация о процессоре лежит между строчками *-cpu и *-cache,в подстроке *-cpu <product>
Поэтому, для вывода информации о процессоре мы выводим отношение строки product и следующей строки, в нашем случае
это строка vendor
После получения информации о процессоре, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
"""

def getnamecpu():
    cpu = text.find("*-cpu")
    cache0 = text.find("  *-cache:0")
    namecpuless = text.find("product", cpu, cache0)
    namecpuless2 = text.find("vendor", cpu, cache0)
    objectivecpu = text[namecpuless:namecpuless2]
    sysinfo.append('Ваш процессор:' + objectivecpu[9:] + '\n')
    return sysinfo
"""
def getnamehdd() - данная функция предназначена для англоязычной системы и ищет информацию в файле lshw о жестком диске
Информация о жестком диске лежит между строчками *-disk и *-volume,в подстроке *-disk <product>
Поэтому, для вывода информации о процессоре мы выводим отношение строки product и следующей строки, в нашем случае
это строка physical id
Так же здесь собирается информация о размере жесткого диска
Она находится между строками size и capabilites
После получения информации о жестком диске, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
""" 
def getnamehdd():
    hdd = text.find("*-disk")
    volume0 = text.rfind("*-volume")
    namehddless = text.find("product", hdd, volume0)
    namehddless2 = text.find("physical id:", hdd, volume0)
    vendorhdd = text.find('vendor' , hdd, volume0)
    vendorhdd2 = text.find('physical id' , hdd, volume0)
    vendorofhdd = text[vendorhdd:vendorhdd2]
    objectivehdd = text[namehddless:namehddless2]
    sizehdd = text.find("size:", hdd, volume0)
    sizehdd2 = text.find("capabilities:", hdd, volume0)
    objectivehddsize = text[sizehdd:sizehdd2]
    left = objectivehddsize.find('(')
    right = objectivehddsize.find(')')
    sysinfo.append("Ваш жесткий диск:" + objectivehdd[7:] + objectivehddsize[left + 1:right] + '\n')
    return sysinfo


"""
def getnameram() - данная функция предназначена для англоязычной системы и ищет информацию в файле lshw о оперативной памяти
Информация о оперативной памяти лежит между строчками *-bank и *-memory,в подстроке *-bank <size>
Поэтому, для вывода информации о процессоре мы выводим отношение строки size и следующей строки, в нашем случае
это строка *-bank
После получения информации о оперативной памяти, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
"""
def getnameram():
    ram = text.find("*-bank:0")
    bank = text.find("*-pci")
    memory = text.find("*-memory")
    memorysize = text.find("size", memory)
    objectiveramsize = text[memorysize:ram]
    nameramless = text.find("product:", ram, bank)
    nameramless2 = text.find("vendor:", ram, bank)
    objectiveram = text[nameramless:nameramless2]
    ddrless = text.find("description", ram, bank)
    ddrless2 = text.find("product",ram, bank)
    ddr = text[ddrless:ddrless2]
    ddr2 = "SODIMM DDR2"
    ddr3 = "SODIMM DDR3"
    ddr4 = "SODIMM DDR4"
    if ddr2 in ddr:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[5:].replace("i","") + "SO-DIMM DDR2")
        return sysinfo
    if ddr3 in ddr:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[5:].replace("i","") + "SO-DIMM DDR3")
        return sysinfo
    if ddr4 in ddr:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[5:].replace("i","") + "SO-DIMM DDR4")
        return sysinfo
 
"""def getnamegpurus() - данная функция предназначена для русскоязычной системы и ищет информацию в файле lshw о видеокарте
Информация о видеокарте в данном файле лежит между строчками *-display и *-pnp
В строчке *-display есть подстрочка продукт которая отвечает за информацию о видеокарте
Поэтому, для выведения информации о видеокарте мы выводим отношение строчки продукт и следующей строчки
в данном случае это строчка производитель
После получения информации о видеокарте, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
"""
def getnamegpurus():
    word = 'Integrated Graphics'
    gpu = text.find("  *-display")
    pnp = text.find("  *-pnp")
    namegpuless = text.find("продукт:", gpu, pnp)
    namegpuless2 = text.find("производитель:", gpu, pnp)
    objectivegpu = text[namegpuless:namegpuless2]
    if word in objectivegpu:
        sysinfo.append('Ваша видеокарта встроенна в процессор' + '\n')
        return sysinfo
    else:
        sysinfo.append('Ваша видеокарта:' + objectivegpu[9:] + '\n')
        return sysinfo
 
"""
def getnamecpurus() - данная функция предназначена для русскоязычной системы и ищет информацию в файле lshw о процессоре
Информация о процессоре лежит между строчками *-cpu и *-cache,в подстроке *-cpu <продукт>
Поэтому, для вывода информации о процессоре мы выводим отношение строки продукт и следующей строки, в нашем случае
это строка производитель
После получения информации о процессоре, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
""" 
def getnamecpurus():
    cpu = text.find("*-cpu")
    cache0 = text.find("  *-cache:0")
    namecpuless = text.find("продукт:", cpu, cache0)
    namecpuless2 = text.find("производитель", cpu, cache0)
    objectivecpu = text[namecpuless:namecpuless2]
    sysinfo.append('Ваш процессор:' + objectivecpu[9:] + '\n')
    return sysinfo
 
"""
def getnamehddrus() - данная функция предназначена для русскоязычной системы и ищет информацию в файле lshw о жестком диске
Информация о жестком диске лежит между строчками *-disk и *-volume,в подстроке *-disk <продукт>
Поэтому, для вывода информации о процессоре мы выводим отношение строки продукт и следующей строки, в нашем случае
это строка производитель
Так же здесь собирается информация о размере жесткого диска
Она находится между строками размер и возможности
После получения информации о жестком диске, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
""" 
def getnamehddrus():
    hdd = text.find("*-disk")
    volume0 = text.rfind("*-volume")
    namehddless = text.find("продукт:", hdd, volume0)
    namehddless2 = text.find("производитель:", hdd, volume0)
    vendorhdd = text.find("производитель:", hdd, volume0)
    vendorhdd2 = text.find("физический ID:", hdd, volume0)
    vendorofhdd = text[vendorhdd:vendorhdd2]
    objectivehdd = text[namehddless:namehddless2]
    sizehdd = text.find("размер:", hdd, volume0)
    sizehdd2 = text.find("возможности:", hdd, volume0)
    objectivehddsize = text[sizehdd:sizehdd2]
    left = objectivehddsize.find('(')
    right = objectivehddsize.find(')')
    sysinfo.append("Ваш жесткий диск:" + vendorofhdd[14:] +objectivehddsize[left + 1:right].replace('i','') + '\n')
    return sysinfo


"""
def getnameramrus() - данная функция предназначена для русскоязычной системы и ищет информацию в файле lshw о оперативной памяти
Информация о оперативной памяти лежит между строчками *-bank и *-memory,в подстроке *-bank <размер>
Поэтому, для вывода информации о процессоре мы выводим отношение строки размер и следующей строки, в нашем случае
это строка *-bank
После получения информации о оперативной памяти, записываем ее в наш список
Тоесть sysinfo.append(здесь ваша информация)
И возвращаем информацию с помощью метода return
"""
def getnameramrus():
    ram = text.find("*-cpu")
    memory = text.find("*-memory")
    memorytype = text.find("*-bank:0")
    memorytype2 = text.find("*-bank:1")
    memorytype3 = text.find("описание:",memorytype,memorytype2)
    memorytype4 = text.find("продукт:",memorytype,memorytype2)
    memorytype5 = text[memorytype3:memorytype4]
    memorysize = text.find("размер:", memory)
    objectiveramsize = text[memorysize:ram]
    sodimmddr2 = 'SO-DIMM DDR2'
    sodimmddr3 = 'SO-DIMM DDR3'
    sodimmddr4 = 'SO-DIMM DDR4'
    if sodimmddr2 in memorytype5:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[7:].replace("i","") + sodimmddr2)
        return sysinfo
    if sodimmddr3 in memorytype5:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[7:].replace("i","") + sodimmddr3)
        return sysinfo
    if sodimmddr4 in memorytype5:
        sysinfo.append("Ваша оперативная память:" + objectiveramsize[7:].replace("i","") + sodimmddr4)
        return sysinfo

        
"""
def sysrussian()  - функция отвечает за вызов всех остальных функций
предназначенных для русскоязычной системы
root.destroy() вызывает закрытие графического интерфейса при нажатии на кнопку
""" 
def sysrussian():
    getnamegpurus()
    getnamecpurus()
    getnamehddrus()
    getnameramrus()
    root.destroy()
 

"""
def sysenglish()  - функция отвечает за вызов всех остальных функций
предназначенных для англоязычной системы
root.destroy() вызывает закрытие графического интерфейса при нажатии на кнопку
""" 
def sysenglish():
    getnamecpu()
    getnamegpu()
    getnamehdd()
    getnameram()
    root.destroy()
 
 
 
 


"""
root = Tk() создание графического интерфейса
"""
root = Tk() 
"""
root.title - название окна графического интерфейса
"""
root.title("sysinfo")
"""
root.geometry - размер окна графического интерфейса
"""
root.geometry("500x100")
"""
btn = Button(...) - создание кнопки,все ее параметры,цвет и т.д
и вызов функции для русскоязычной системы
"""
btn = Button(text='Язык системы - русский',background="#555",foreground="#ccc",padx="20",pady="8",font="16",command=sysrussian)
"""
создание кнопки
"""
btn.pack()
"""
btn2 = Button(...) - создание кнопки,все ее параметры,цвет и т.д
и вызов функции для англоязычной системы
"""
btn2 = Button(text='Язык системы - английский',background="#555",foreground="#ccc",padx="20",pady="8",font="16",command=sysenglish)
"""
создание второй кнопки
"""
btn2.pack()
"""
запуск самого графического интерфейса
"""
root.mainloop()
"""
Открытие файла sysinfo
Далее - записывание в него списка sysinfo заранее созданного
После записи в него информацию,файл закрывается
"""
filetext = open('sysinfo', 'w')
filetext.writelines(sysinfo)
filetext.close()
