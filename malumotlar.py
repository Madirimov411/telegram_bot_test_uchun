
#Dasturlash tillari
dasturlash_tillari = [
    (1, 'Python'),
    (2, 'JavaScript'),
    (3, 'Java'),
    (4, 'C++'),
    (5, 'C#'),
    (6, 'Go'),
    (7, 'Swift'),
    (8, 'Kotlin'),
    (9, 'Ruby'),
    (10, 'PHP'),
    (11, 'TypeScript'),
    (12, 'Rust'),
    (13, 'Dart'),
    (14, 'Scala'),
    (15, 'Perl')
]


data_list = [
    (1, 'Python','python','https://img.ixbt.site/live/topics/preview/00/04/43/61/4c83e99030.jpg'),
    (2, 'JavaScript','java_script','https://blog.enterprisedna.co/wp-content/uploads/2024/04/Javascript-Content-Article.png'),
    (3, 'Java','java','https://infostart.ru/upload/iblock/f54/f548efe1cf81eeab4473aa8b403a7204.png'),
    (4, 'C++','c_plus_plus','https://overclockers.ru/st/legacy/blog/413340/336432_O.jpg'),
    (5, 'C#','c_sharp','https://the-tech.kz/wp-content/uploads/2024/04/photo_2024-04-29_12-46-54.jpg'),
    (6, 'Go','go_lang','https://miro.medium.com/v2/resize:fit:1358/1*xofqkz49chC9XliDAuH1Qw.png'),
    (7, 'Swift','swift','https://i.pinimg.com/originals/df/b9/7a/dfb97a69381655c60569c2d653dbefc0.png'),
    (8, 'Kotlin','kotlin','https://media.proglib.io/wp-uploads/2017/06/mainkotlin.jpg'),
    (9, 'PHP','php','https://repository-images.githubusercontent.com/286744205/eccf6100-dbec-11ea-8094-6995de8227ea'),
    (10, 'Dart','dart','https://pic.rutubelist.ru/video/52/b4/52b4e52f7c9329d0178cbd80bb4d402e.jpg'),
    (11, 'Scala','scala','https://cdn.otus.ru/media/public/24/49/1_1801_4f11cf_1-1801-244974.png'),
]

# QO'LLASH
# insert_query = "INSERT INTO public.til (id, name) VALUES (%s, %s)"
# cur.executemany(insert_query, dasturlash_tillari)
# conn.commit()



#Testlar
testlar=[
    (1, 1, "Python dasturlash tili kim tomonidan yaratilgan?", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "James Gosling", "Guido van Rossum"),
    (2, 1, "Python qanday dasturlash tili hisoblanadi?", "Kompilyatsiyalanuvchi", "Interpretatsiyalanuvchi", "Assembler", "Ma'lumotlar bazasi tili", "Interpretatsiyalanuvchi"),
    (3, 1, "Python-da qaysi operator taqqoslash uchun ishlatiladi?", "==", "=", "!=", ":", "=="),
    (4, 1, "Python-da qaysi ma'lumot turi butun sonlarni ifodalaydi?", "float", "str", "int", "list", "int"),
    (5, 1, "Python-da qaysi funksiya ekranga chiqarish uchun ishlatiladi?", "print()", "echo()", "display()", "output()", "print()"),
    (6, 1, "Python-da qaysi belgi komment yozish uchun ishlatiladi?", "#", "//", "--", "/* */", "#"),
    (7, 1, "Python-da list qanday ma'lumot turi?", "O'zgaruvchan", "O'zgarmas", "Faqat o'qish mumkin", "Faol ma'lumot turi", "O'zgaruvchan"),
    (8, 1, "Python-da tuple qanday xususiyatga ega?", "O'zgaruvchan", "O'zgarmas", "Ko'p martalik", "Shartli", "O'zgarmas"),
    (9, 1, "Python-da qaysi operator qo‘shish uchun ishlatiladi?", "+", "-", "*", "/", "+"),
    (10, 1, "Python-da ifodani ekranga chiqarish qaysi funksiya orqali amalga oshiriladi?", "print()", "return()", "display()", "show()", "print()"),
    (11, 1, "Python-da qaysi kalit so'z sikl yaratish uchun ishlatiladi?", "for", "while", "if", "switch", "for"),
    (12, 1, "Python-da \"elif\" operatori qanday ishlaydi?", "Takrorlash", "Shartlarni tekshirish", "Funksiya yaratish", "Ma'lumotni o‘chirish", "Shartlarni tekshirish"),
    (13, 1, "Python-da funksiyalar qanday yaratiladi?", "function", "def", "fun", "void", "def"),
    (14, 1, "Python-da list elementlarini qanday indekslash mumkin?", "0 dan boshlab", "1 dan boshlab", "Harflar bilan", "Teskari tartibda", "0 dan boshlab"),
    (15, 1, "Python-da for sikli qanday ishlaydi?", "Berilgan diapazonda", "Tugaguncha", "Shart bajarilganda", "Hech biri", "Berilgan diapazonda"),
    (16, 1, "Python-da dictionary qanday yoziladi?", "{key: value}", "[key: value]", "(key, value)", "<key=value>", "{key: value}"),
    (17, 1, "Python-da massivlar qanday nomlanadi?", "tuple", "list", "dict", "set", "list"),
    (18, 1, "Python-da ma'lumot turlarini tekshirish uchun qaysi funksiya ishlatiladi?", "check()", "typeof()", "type()", "isType()", "type()"),
    (19, 1, "Python-da teskari indekslash qanday boshlanadi?", "-1", "0", "1", "-2", "-1"),
    (20, 1, "Python-da qanday operator qoldiqni hisoblash uchun ishlatiladi?", "%", "/", "//", "*", "%"),
    (21, 1, "Python-da qanday operator darajani hisoblash uchun ishlatiladi?", "**", "^", "^^", "//", "**"),
    (22, 1, "Python-da stringlarni qaysi belgilar yordamida belgilaymiz?", "'", "\"", "''", "Har ikkisi", "Har ikkisi"),
    (23, 1, "Python-da qaysi funksiya foydalanuvchidan ma'lumot olish uchun ishlatiladi?", "input()", "read()", "scan()", "get()", "input()"),
    (24, 1, "Python-da qaysi ma'lumot turi o'zgarmas hisoblanadi?", "list", "tuple", "dict", "set", "tuple"),
    (25, 1, "Python-da boolean qiymatlar qanday yoziladi?", "TRUE/FALSE", "True/False", "true/false", "0/1", "True/False"),
    (26, 1, "Python-da shartli operator qanday yoziladi?", "if", "when", "switch", "case", "if"),
    (27, 1, "Python-da list elementlarini qanday chiqarish mumkin?", "list[0]", "list{0}", "list(0)", "list.0", "list[0]"),
    (28, 1, "Python-da dictionary dan element olish uchun qaysi belgi ishlatiladi?", "[key]", "{key}", "(key)", "<key>", "[key]"),
    (29, 1, "Python-da qanday sikl shart bajarilmaguncha davom etadi?", "for", "while", "do while", "loop", "while"),
    (30, 1, "Python-da string uzunligini o'lchash uchun qaysi funksiya ishlatiladi?", "len()", "size()", "length()", "count()", "len()"),
    (31, 1, "Python-da qaysi kalit so‘z siklni to‘xtatadi?", "break", "continue", "stop", "exit", "break"),
    (32, 1, "Python-da qaysi kalit so‘z siklning keyingi iteratsiyasiga o'tish uchun ishlatiladi?", "break", "continue", "skip", "pass", "continue"),
    (33, 1, "Python-da bo‘sh funksiya yaratish uchun qaysi kalit so‘z ishlatiladi?", "empty", "skip", "pass", "None", "pass"),
    (34, 1, "Python-da qanday funksiyalar anonymous (nomi yo'q) hisoblanadi?", "def", "lambda", "fun", "None", "lambda"),
    (35, 1, "Python-da exception handling qaysi kalit so‘z bilan boshlanadi?", "catch", "try", "except", "handle", "try"),
    (36, 1, "Python-da massiv (list) elementlarini saralash uchun qaysi funksiya ishlatiladi?", "sort()", "sorted()", "order()", "arrange()", "sort()"),
    (37, 1, "Python-da range(5) ning natijasi qanday bo‘ladi?", "0,1,2,3,4", "1,2,3,4,5", "0,2,4,6,8", "None", "0,1,2,3,4"),
    (38, 1, "Python-da 2 va 3 qavatli for sikli necha marta bajariladi?", "5", "6", "6+", "Har xil", "6+"),
    (39, 1, "Python-da qanday metod stringni kichik harfga o‘tkazadi?", "lower()", "small()", "tiny()", "down()", "lower()"),
    (40, 1, "Python-da qanday metod stringni katta harfga o‘tkazadi?", "upper()", "big()", "capital()", "up()", "upper()"),
    (41, 1, "Python-da ma’lumotlarni faylga yozish uchun qaysi metod ishlatiladi?", "write()", "append()", "save()", "print()", "write()"),
    (42, 1, "Python-da \"with open()\" qanday maqsadda ishlatiladi?", "Kodni tezlashtirish", "Faylni o‘qish va yopish", "Malumotlarni kriptografik himoya qilish", "Har xil operatsiyalar", "Faylni o‘qish va yopish"),
    (43, 1, "Python-da qaysi modul tasodifiy sonlar yaratish uchun ishlatiladi?", "random", "math", "rand", "time", "random"),
    (44, 1, "Python-da qaysi metod stringni bo'sh joylaridan tozalaydi?", "strip()", "clean()", "replace()", "trim()", "strip()"),
    (45, 1, "Python-da rekursiv funksiya qanday ishlaydi?", "O‘z-o‘zini chaqiradi", "Faqat bitta argument qabul qiladi", "Foydalanuvchi ma’lumotlarini saqlaydi", "Oddiy funksiya", "O‘z-o‘zini chaqiradi"),
    (46, 1, "Python-da qaysi metod string ichidagi belgilarning indeksini qaytaradi?", "index()", "find()", "search()", "locate()", "find()"),
    (47, 1, "Python-da obyektlarni JSON formatiga o'tkazish uchun qaysi modul ishlatiladi?", "json", "pickle", "csv", "xml", "json"),
    (48, 1, "Python-da class yaratish uchun qaysi kalit so‘z ishlatiladi?", "class", "def", "object", "type", "class"),
    (49, 1, "Python-da obyekt yaratish uchun qanday sintaksis ishlatiladi?", "ClassName()", "new ClassName()", "ClassName.new()", "object(ClassName)", "ClassName()"),
    (50, 1, "Python-da qaysi kalit so‘z klass metodiga o‘zi ishlov berish imkonini beradi?", "self", "this", "me", "own", "self"),
    (51, 1, "Python-da o'zgaruvchilarga qaysi kalit so'z bilan global deb belgilash mumkin?", "global", "Global", "var", "static", "global"),
    (52, 1, "Python-da qaysi funksiya modulni yuklash uchun ishlatiladi?", "import", "include", "require", "load", "import"),
    (53, 1, "Python-da vaqt bilan ishlash uchun qaysi modul ishlatiladi?", "datetime", "time", "calendar", "clock", "datetime"),
    (54, 1, "Python-da obyekt metodlarini chaqirish uchun qanday operator ishlatiladi?", ".", "::", "->", ":", "."),
    (55, 1, "Python-da qaysi modul HTTP so‘rovlarini yuborish uchun ishlatiladi?", "requests", "http", "socket", "urllib", "requests"),
    (56, 1, "Python-da qaysi funksiya integerni float ga aylantiradi?", "float()", "int()", "convert()", "toFloat()", "float()"),
    (57, 1, "Python-da exception (xatolik) turini bilish uchun qaysi funksiya ishlatiladi?", "type()", "error()", "exception()", "info()", "type()"),
    (58, 1, "Python-da iterable obyektni ro‘yxatga aylantirish uchun qaysi funksiya ishlatiladi?", "list()", "tuple()", "dict()", "array()", "list()"),
    (59, 1, "Python-da listga element qo‘shish uchun qaysi metod ishlatiladi?", "append()", "add()", "push()", "insert()", "append()"),
    (60, 1, "Python-da listning ma'lum indeksiga yangi element qo'shish uchun qaysi metod ishlatiladi?", "insert()", "append()", "add()", "replace()", "insert()"),
    (61, 1, "Python-da dictionary ichidan element olish uchun qanday metod ishlatiladi?", "get()", "find()", "search()", "lookup()", "get()"),
    (62, 1, "Python-da qaysi metod string ichidagi so‘zlarni ajratish uchun ishlatiladi?", "split()", "divide()", "separate()", "cut()", "split()"),
    (63, 1, "Python-da iterable obyektning barcha elementlarini o‘z ichiga olgan list yaratish uchun qaysi funksiya ishlatiladi?", "list()", "tuple()", "set()", "dict()", "list()"),
    (64, 1, "Python-da faylni o‘qish rejimida ochish uchun qanday parametr ishlatiladi?", "'r'", "'w'", "'a'", "'x'", "'r'"),
    (65, 1, "Python-da faylga yozish uchun qanday parametr ishlatiladi?", "'w'", "'r'", "'a'", "'x'", "'w'"),
    (66, 1, "Python-da faylni faqat qo‘shimcha yozish uchun qanday parametr ishlatiladi?", "'a'", "'r'", "'w'", "'x'", "'a'"),
    (67, 1, "Python-da \"elif\" operatori nimani anglatadi?", "Else If", "Else", "Loop", "Break", "Else If"),
    (68, 1, "Python-da doimiy (constant) qiymatlar qanday belgilangan?", "O‘zgaruvchilarga katta harflar bilan", "const keyword bilan", "let keyword bilan", "static keyword bilan", "O‘zgaruvchilarga katta harflar bilan"),
    (69, 1, "Python-da list elementlarini teskari tartibda chiqarish uchun qaysi metod ishlatiladi?", "reverse()", "invert()", "flip()", "sort(reverse=True)", "reverse()"),
    (70, 1, "Python-da class ichida obyekt yaratish uchun qanday metod ishlatiladi?", "__init__()", "__class__()", "__new__()", "__main__()", "__init__()"),
    (71, 1, "Python-da class metodlarini belgilash uchun qanday dekorator ishlatiladi?", "@classmethod", "@staticmethod", "@property", "@function", "@classmethod"),
    (72, 1, "Python-da statik metod yaratish uchun qanday dekorator ishlatiladi?", "@staticmethod", "@classmethod", "@property", "@abstractmethod", "@staticmethod"),
    (73, 1, "Python-da abstract klass yaratish uchun qaysi modul kerak?", "abc", "abstract", "base", "meta", "abc"),
    (74, 1, "Python-da iterator yaratish uchun qaysi metodni ishlatish kerak?", "__iter__()", "__next__()", "iter()", "next()", "__iter__()"),
    (75, 1, "Python-da iterator keyingi elementni olish uchun qaysi metod ishlatiladi?", "__next__()", "__iter__()", "next()", "step()", "__next__()"),
    (76, 1, "Python-da qaysi modul grafik interfeys yaratish uchun ishlatiladi?", "tkinter", "pygame", "qt", "pygui", "tkinter"),
    (77, 1, "Python-da ma'lumotlarni CSV formatida o‘qish uchun qaysi modul ishlatiladi?", "csv", "pandas", "json", "excel", "csv"),
    (78, 1, "Python-da JSON ma'lumotlarini o‘qish uchun qaysi metod ishlatiladi?", "json.load()", "json.loads()", "json.parse()", "json.read()", "json.load()"),
    (79, 1, "Python-da JSON ma'lumotlarini stringga o‘tkazish uchun qaysi metod ishlatiladi?", "json.dumps()", "json.load()", "json.encode()", "json.stringify()", "json.dumps()"),
    (80, 1, "Python-da multiprocessing moduli nimaga xizmat qiladi?", "Parallel ishlov berish", "Fayllarni o‘qish", "Ma'lumotlarni saqlash", "Grafik interfeys yaratish", "Parallel ishlov berish"),
    (81, 1, "Python-da 'lambda' nima uchun ishlatiladi?", "Anonim funksiya yaratish", "O'zgaruvchi yaratish", "Module import qilish", "Loop yaratish", "Anonim funksiya yaratish"),
    (82, 1, "Python-da dictionary-dagi barcha kalitlarni olish uchun qaysi metod ishlatiladi?", "keys()", "values()", "items()", "get()", "keys()"),
    (83, 1, "Python-da dictionary-dagi barcha qiymatlarni olish uchun qaysi metod ishlatiladi?", "values()", "keys()", "items()", "get()", "values()"),
    (84, 1, "Python-da stringlarni qaysi operator bilan birlashtirish mumkin?", "+", "*", "-", "/", "+"),
    (85, 1, "Python-da obyektning turi qanday aniqlanadi?", "type()", "typeof()", "instance()", "class()", "type()"),
    (86, 1, "Python-da for loop qanday maqsadda ishlatiladi?", "Takrorlanuvchi elementlarni o‘tish", "Fayl o‘qish", "Shart tekshirish", "Fayl yozish", "Takrorlanuvchi elementlarni o‘tish"),
    (87, 1, "Python-da stringni uppercase ga o‘tkazish uchun qaysi metod ishlatiladi?", "upper()", "capitalize()", "title()", "uppercase()", "upper()"),
    (88, 1, "Python-da stringni lowercase ga o‘tkazish uchun qaysi metod ishlatiladi?", "lower()", "capitalize()", "title()", "lowercase()", "lower()"),
    (89, 1, "Python-da listni tartiblash uchun qaysi metod ishlatiladi?", "sort()", "order()", "sorted()", "arrange()", "sort()"),
    (90, 1, "Python-da yangi modul yaratish uchun nima qilish kerak?", "Yangi .py fayl yaratish", "Modulni yuklab olish", "import qilish", "Funksiya chaqirish", "Yangi .py fayl yaratish"),
    (91, 1, "Python-da exceptionlarni qanday ushlash mumkin?", "try-except", "if-else", "catch", "switch-case", "try-except"),
    (92, 1, "Python-da set qanday xususiyatga ega?", "Unikal elementlarni saqlaydi", "Tartiblangan", "O‘zgaruvchan emas", "Faqat sonlarni saqlaydi", "Unikal elementlarni saqlaydi"),
    (93, 1, "Python-da stringni raqamga aylantirish uchun qaysi funksiya ishlatiladi?", "int()", "str()", "float()", "eval()", "int()"),
    (94, 1, "Python-da obyektning ma’lum bir klassga tegishli ekanligini tekshirish uchun qaysi funksiya ishlatiladi?", "isinstance()", "issubclass()", "type()", "checktype()", "isinstance()"),
    (95, 1, "Python-da string ichidagi so‘zlarni ajratish uchun qaysi metod ishlatiladi?", "split()", "separate()", "cut()", "divide()", "split()"),
    (96, 1, "Python-da faylni yopish uchun qaysi metod ishlatiladi?", "close()", "stop()", "exit()", "terminate()", "close()"),
    (97, 1, "Python-da generator funksiyalarini yaratish uchun qaysi kalit so‘z ishlatiladi?", "yield", "return", "generate", "lambda", "yield"),
    (98, 1, "Python-da rekursiv funksiya nima qiladi?", "O‘zini o‘zi chaqiradi", "Loop yaratadi", "Matematik hisob-kitob qiladi", "Ma’lumotlarni saqlaydi", "O‘zini o‘zi chaqiradi"),
    (99, 1, "Python-da slicing operatori qanday ko‘rinishda yoziladi?", "[:]", "[::]", "()", "{}", "[:]"),
    (100, 1, "Python-da default argumentlar qanday ishlaydi?", "Funksiya argumentlari oldindan belgilangan qiymatga ega bo‘ladi", "Funktsiya doim argument talab qiladi", "Argumentlar soni aniq bo‘lishi kerak", "Funktsiya parametrlarini belgilab bo‘lmaydi", "Funksiya argumentlari oldindan belgilangan qiymatga ega bo‘ladi"),
]

# insert_query = """
# INSERT INTO public.testlar (id, til_id, savol, a_javob, b_javob, c_javob, d_javob, togri_javob)
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# """

# cur.executemany(insert_query, testlar)
#
# # O'zgarishlarni saqlash
# conn.commit()
#
# # Resurslarni yopish
# cur.close()
# conn.close()
#
# print("100 ta test muvaffaqiyatli qo‘shildi!")
