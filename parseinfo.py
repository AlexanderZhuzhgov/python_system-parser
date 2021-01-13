"""
Импортиурем библиотеки
selenium - библиотека для парсера сайтов,иммитируя некоторые действия пользователя
tkinter - библиотека для создания графического интерфейса
"""
from selenium import webdriver
from tkinter import *
"""
Открываем файл sysinfo для чтения информации из него.
Первый аргумент - название файла, второй аргумент - то, что мы делаем с файлом
в нашем случае мы его читаем, для этого предназначен аргумент r(сокращенно от read)
"""
information = open('sysinfo','r')
text = information.read()

"""
root = Tk() - Создание графического интерфейса
"""
root = Tk()
"""
Переменные для вывода в графический интерфейс
Если будет найдена цена для соответствующей комплектующей значение переменной
будет переопределено на его стоимость.
В случае ненахождения цены,будет выведен текст изначально хранившийся в переменных.
"""
ozunotprice = 'Не удалось определить цену'
ozunotpricedns = "Не удалось определить цену"
ozunotpricekatalog = "Не удалось определить цену"
ozunotpricemvideo = "Не удалось определить цену"
cpunotprice = "Не удалось определить цену"
cpunotpricedns = "Не удалось определить цену"
cpunotpricekatalog = "Не удалось определить цену"
cpunotpricemvideo = "Не удалось определиь цену"
gpunotprice = "Не удалось определить цену"
gpunotpricedns = "Не удалось определить цену"
gpunotpricekatalog = "Не удалось определить цену"
gpunotpricemvideo = "Не удалось определиь цену"
hddnotprice = "Не удалось определить цену"
hddnotpricedns = "Не удалось определить цену"
hddnotpricekatalog = "Не удалось определить цену"
hddnotpricemvideo = "Не удалось определиь цену"
"""

def ramprice() - функция отвечающая за подсчет стоимости оперативной памяти
Для начала,мы ищем в файле (sysinfo в котором мы вывели информацию о системе)
информацию о ОЗУ,данная информация находится на последней строчке, поэтому мы начинаемся поиск 
от слов <Обьем вашей оперативной памяти> и до конца файла, после того как функция находит
информацию о Оперативной памяти,функция начинает подсчет ее стоимости.
driver = webdriver.Chrome() - переменная отвечающая за работу с ОПРЕДЕЛЕННЫМ браузером
В нашем случае это Chrome
driver.get = ... работа браузера с определенным сайтом
price_elem = ... нахождение заранее обозначенного элемента в коде страницы,который задан 
переменной driver.get
try: отвечает за попытку найти price_elem,в случае ненахождения используется метод except:
который отвечает за ошибку
driver.close() - отвечает за закрытие окна браузера

"""

def ramprice():
    ramless = text.find('Ваша оперативная память:')
    ramless2 = text[ramless:]
    global ram
    ram = ramless2[25:]
    driver = webdriver.Chrome()
    driver.get("https://www.avito.ru/rossiya?q=" + ram)
    try:
        price_elem1 = driver.find_element_by_class_name("snippet-price-row")
        global ozunotprice
        ozunotprice = price_elem1.text
        print("Стоимость на Авито: " + price_elem1.text)
        driver.close()
    except:
        print("Не удалось определить стоимость на Авито")
        driver.close()
    driver2 = webdriver.Chrome()
    driver2.get("https://www.dns-shop.ru/search/?q= " + ram)
    try:
        price_elem2 = driver2.find_element_by_class_name("product-min-price__current")
        global ozunotpricedns
        ozunotpricedns = price_elem2.text
        print("Стоимсть в DNS:" + price_elem2.text + "\n")
        driver2.close()
    except:
        print("Не удалось определить стоимость в DNS")
        driver2.close()
    driver3 = webdriver.Chrome()
    driver3.get("https://www.e-katalog.ru/ek-list.php?katalog_=188&search_=" + ram)
    try:
        price_elem3 = driver3.find_element_by_class_name("model-price-range")
        global ozunotpricekatalog
        ozunotpricekatalog = price_elem3.text
        print("Стоимость в Е-Каталог:" + price_elem3.text)
        driver3.close()
    except:
        print("Не удалось определить стоимость в Е-Каталог")
        driver3.close()
    driver4 = webdriver.Chrome()
    driver4.get("https://www.mvideo.ru/product-list-page-cls?q=" + ram)
    try:
        price_elem4 = driver4.find_element_by_class_name("fl-product-tile-price__current")
        global ozunotpricemvideo
        ozunotpricemvideo = price_elem4.text
        print("Стоимость в МВИДЕО:" + price_elem4.text)
        driver4.close()
    except:
        print("Не удалось определить стоимость в МВИДЕО")
        driver4.close()
"""
def cpuprice() - функиция отвечающая за вывод стоимости процессора
Для начала мы ищем информацию в файле sysinfo о процессоре
Эта информация находится между строчками Ваш процессор и Ваша видеокарта
Поэтому мы выводим их соотношение
Далее функция как и в функции def ramrpice() парсит некоторые сайты и выводит с них информацию о стоимости.
"""
def cpuprice():
    cpuless = text.find('Ваш процессор:')
    cpuless2 = text.find('Ваша видеокарта')
    cpuless3 = text[cpuless:cpuless2]
    global cpu
    cpu = cpuless3[14:]
    print("Процессор: " + cpu)
    driver = webdriver.Chrome()
    driver.get("https://www.avito.ru/rossiya?q=" + cpu.replace(" ", ""))
    try:
        price_elem1 = driver.find_element_by_class_name("snippet-price-row")
        global cpunotprice
        cpunotprice = price_elem1.text
        print("Стоимость на Авито: " + price_elem1.text)
        driver.close()
    except:
        print("Не удалось определить стоимость на Авито")
        driver.close()
    driver2 = webdriver.Chrome()
    driver2.get("https://www.dns-shop.ru/search/?q=" + cpu)
    try:
        price_elem2 = driver2.find_element_by_class_name("product-min-price__current")
        global cpunotpricedns
        cpunotpricedns = price_elem2.text
        print("Стоимсть в DNS:" + price_elem2.text + "\n")
        driver2.close()
    except:
        print("Не удалось определить стоимость в DNS")
        driver2.close()
    driver3 = webdriver.Chrome()
    driver3.get("https://www.e-katalog.ru/ek-list.php?katalog_=186&search_=" + cpu)
    try:
        price_elem3 = driver3.find_element_by_class_name("model-price-range")
        global cpunotpricekatalog
        cpunotpricekatalog = price_elem3.text
        print("Стоимость в Е-Каталог:" + price_elem3.text)
        driver3.close()
    except:
        print("Не удалось определить стоимость в Е-Каталог")
        driver3.close()
    driver4 = webdriver.Chrome()
    driver4.get("https://www.mvideo.ru/product-list-page-cls?q=" + cpu)
    try:
        price_elem4 = driver4.find_element_by_class_name("fl-product-tile-price__current")
        global cpunotpricemvideo
        cpunotpricemvideo = price_elem4.text
        print("Стоимость в МВИДЕО:" + price_elem4.text)
        driver4.close()
    except:
        print("Не удалось определить стоимость в МВИДЕО")
        driver4.close()
"""
def gpuprice() - функция которая отвечает за вывод стоимости вашей видеокарты
Для начала фукция ищет информацию в файле sysinfo о вашей видеокарте
Данная информация находится между строчками Ваша видеокарта и Ваш жесткий диск
Поэтому для вывода название видеокарты, мы выводим соотношение строк Ваша видеокарта и Ваш жесткий диск
Далее происходит парсинг некоторых сайтов, и все остальное так же как и до этого
"""
def gpuprice():
    intr = 'Встроенна в процессор'
    gpuless = text.find('Ваша видеокарта:')
    gpuless2 = text.find('Ваш жесткий диск:')
    gpuless3 = text[gpuless:gpuless2]
    if intr in gpuless3:
        print("У вас интегрированная видеокарта в процессор")
    else:
        global gpu
        gpu = gpuless3[16:]
        print("Видеокарта: " + gpu)
        driver = webdriver.Chrome()
        driver.get("https://www.avito.ru/rossiya?q=" + gpu.replace(" ", ""))
        try:
            price_elem1 = driver.find_element_by_class_name("snippet-price-row")
            global gpunotprice
            gpunotprice = price_elem1.text
            print("Стоимость на Авито: " + price_elem1.text)
            driver.close()
        except:
            print("Не удалось определить стоимость на Авито")
            driver.close()
        driver2 = webdriver.Chrome()
        driver2.get("https://www.dns-shop.ru/search/?q=" + gpu.replace(" ", ""))
        try:
            price_elem2 = driver2.find_element_by_class_name("product-min-price__current")
            global gpunotpricedns
            gpunotpricedns = price_elem2.text
            print("Стоимсть в DNS:" + price_elem2.text + "\n")
            driver2.close()
        except:
            print("Не удалось определить стоимость в DNS")
            driver2.close()
        driver3 = webdriver.Chrome()
        driver3.get("https://www.e-katalog.ru/ek-list.php?katalog_=189&search_=" + gpu.replace(" ", ''))
        try:
            price_elem3 = driver3.find_element_by_class_name("model-price-range")
            global gpunotpricekatalog
            gpunotpricekatalog = price_elem3.text
            print("Стоимость в Е-Каталог:" + price_elem3.text)
            driver3.close()
        except:
            print("Не удалось определить стоимость в Е-Каталог")
            driver3.close()
        driver4 = webdriver.Chrome()
        driver4.get("https://www.mvideo.ru/product-list-page-cls?q=" + gpu.replace(" ", ''))
        try:
            price_elem4 = driver4.find_element_by_class_name("fl-product-tile-price__current")
            global gpunotpricemvideo
            gpunotpricemvideo = price_elem4.text
            print("Стоимость в МВИДЕО:" + price_elem4.text)
            driver4.close()
        except:
            print("Не удалось определить стоимость в МВИДЕО")
            driver4.close()
 
"""
def hddprice() - функция которая отвечает за вывод стоимости вашего жесткого диска
Для начала функция собирает информацию из файла sysinfo о вашей видеокарте
Данная информация находится между строчками Ваш жесктий диск и Обьем вашей оперативной памяти
Поэтому мы выводим их соотношение
Далее функция уже считает стоимость вашего жесткого диска используя парсинг некоторых сайтов
"""
def hddprice():
    hddless = text.find("Ваш жесткий диск:")
    hddless2 = text.find("Ваша оперативная память:")
    hddless3 = text[hddless:hddless2]
    global hdd
    hdd = hddless3[17:]
    print("Жесткий диск: " + hdd)
    driver = webdriver.Chrome()
    driver.get("https://www.avito.ru/rossiya?q=" + hdd.replace(" ",""))
    try:
            price_elem1 = driver.find_element_by_class_name("snippet-price-row")
            global hddnotprice
            hddnotprice = price_elem1.text
            print("Стоимость на Авито: " + price_elem1.text)
            driver.close()
    except:
            print("Не удалось определить стоимость на Авито")
            driver.close()
    driver2 = webdriver.Chrome()
    driver2.get("https://www.dns-shop.ru/search/?q=" + hdd)
    try:
            price_elem2 = driver2.find_element_by_class_name("product-min-price__current")
            global hddnotpricedns
            hddnotpricedns = price_elem2.text
            print("Стоимсть в DNS:" + price_elem2.text + "\n")
            driver2.close()
    except:
            print("Не удалось определить стоимость в DNS")
            driver2.close()
    driver3 = webdriver.Chrome()
    driver3.get("https://www.e-katalog.ru/ek-list.php?katalog_=189&search_=" + hdd)
    try:
            price_elem3 = driver3.find_element_by_class_name("model-price-range")
            global hddnotpricekatalog
            hddnotpricekatalog = price_elem3.text
            print("Стоимость в Е-Каталог:" + price_elem3.text)
            driver3.close()
    except:
            print("Не удалось определить стоимость в Е-Каталог")
            driver3.close()
    driver4 = webdriver.Chrome()
    driver4.get("https://www.mvideo.ru/product-list-page-cls?q=" + hdd)
    try:
            price_elem4 = driver4.find_element_by_class_name("fl-product-tile-price__current")
            global hddnotpricemvideo
            hddnotpricemvideo = price_elem4.text
            print("Стоимость в МВИДЕО:" + price_elem4.text)
            driver4.close()
    except:
            print("Не удалось определить стоимость в МВИДЕО")
            driver4.close()
"""
Строчки ramprice() hddprice() gpuprice() cpuprice()
Отвечают за вызов самих функций
"""
ramprice()
hddprice()
gpuprice()
cpuprice()
"""
Далее идет вывод информации полученной из функций в графический интерфейс
"""
"""
Сам вывод текста
"""
text = Text(width=60, height=20)
text.insert(INSERT,"Оперативная память:" + ram +"\n" "Цена на авито:" + ozunotprice + "\n" + "Цена в DNS:" + ozunotpricedns
+ "\n" + "Цена в Е-Каталог:" + ozunotpricekatalog + "\n" + "Цена в Мвидео:" + ozunotpricemvideo + '\n' + '\n' + "Жесткий диск:" + hdd + "\n" + "Цена на авито:" 
+ hddnotprice + "\n" + "Цена в DNS:" + hddnotpricedns + '\n' + "Цена в Е-Каталог:" + hddnotpricekatalog + "\n" + "Цена в Мвидео:" + hddnotpricemvideo + '\n'
+ '\n' "Видеокарта:" + gpu + "\n" + "Цена на авито:" + gpunotprice + "\n" + "Цена в DNS:" + gpunotpricedns
+ '\n' + "Цена в Е-Каталог:" + gpunotpricekatalog + "\n" + "Цена в Мвидео:" + gpunotpricemvideo + '\n'+ '\n' + "Процессор:" + cpu + "\n" + "Цена на авито:" + cpunotprice   + "\n" + "Цена в DNS:" + cpunotpricedns + '\n' + "Цена в Е-Каталог:" + cpunotpricekatalog + "\n" + "Цена в Мвидео:" + cpunotpricemvideo)
"""
Конечный вывод текста в граф.интерефейс
"""

text.pack(side=LEFT)

"""
scroll отвечает за прокрутку окна графеического интерфейса
"""
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y) 
text.config(yscrollcommand=scroll.set)
"""
Запуск графического интерфейса
""" 
root.mainloop()
