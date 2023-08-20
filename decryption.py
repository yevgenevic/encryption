import pyAesCrypt
import os
import sys


# faylni dekodlash funksiyasi
def decryption(file, password):
    # bufer hajmini belgilaymiz
    buffer_size = 512 * 1024

    # deshifrlaydigan metodni chaqiramiz
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # natijani ko'rish uchun shifrlangan fayl nomini chop etish
    print("[Fayl '" + str(os.path.splitext(file)[0]) + "' deshifrlandi]")

    # asl faylni o'chirib tashlang
    os.remove(file)


# kataloglarni skanerlash funksiyasi
def walking_by_dirs(dir, password):
    # belgilangan katalogdagi barcha pastki kataloglar bo'ylab aylanish
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # agar fayl topilsa deshifrlash
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # agar  katalog toplsa, u holda fayllarni qidirishda siklni takrorlaymiz
        else:
            walking_by_dirs(path, password)


password = input("deshifrlash uchun parolni kiriting: ")
# shifrlash uchun kiritgan parolni yozasiz
walking_by_dirs("/home/yevgenevic/Music", password)
# os.remove(str(sys.argv[0]))
