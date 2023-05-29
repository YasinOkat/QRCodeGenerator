import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

directory = os.getcwd()
print(directory + " ")

fontpath = directory + "/" + "bin" + "/" + "/LiberationSans-Regular.ttf"

device_map = {
    1: 'LPC-2023-',
    2: 'RT-2023-',
    3: 'ACC-2023-',
    4: 'BO-2022-',
    5: 'BOS-2022-',
    6: 'BY-2022-',
    7: 'ELT-2023-',
    8: 'MNT-2023-',
    9: 'PSW-2023-',
    10: 'SW-2023-',
    11: 'MOU-2023-',
    12: 'KLA-2023-',
    13: 'NVR-2023-',
    14: 'KAS-2023-',
    15: 'YZC-2023-',
    16: 'LSJ-2023-',
}

while True:
    try:
        cihaz = int(input("Cihaz seçiniz:\n"
                          "1. Laptop\n"
                          "2. Router\n"
                          "3. Access Point\n"
                          "4. Barkod Okuyucu\n"
                          "5. Barkod Okuyucu Şarj Ünitesi\n"
                          "6. Barkod Yazıcı\n"
                          "7. El Terminali\n"
                          "8. Monitör\n"
                          "9. PoE Switch\n"
                          "10. PoE Olmayan Switch\n"
                          "11. USB Mouse\n"
                          "12. Kablolu Klavye\n"
                          "13. NVR\n"
                          "14. Masaüstü Kasa\n"
                          "15. Yazıcı\n"
                          "16. Laptop Şarj Aleti\n"
                          "17. Listede yok, manuel gireceğim (büyük etiket)\n"
                          "18. Listede yok, manuel gireceğim (küçük etiket)\n"
                          ))
        if cihaz in device_map:
            kod = device_map[cihaz]
            break
        elif cihaz == 17 or cihaz == 18:
            kod = input("Kod giriniz: (Örn. SW, LPC vb.)\n") + '-2023-'
            break

        if cihaz > 18 or not isinstance(cihaz, int):
            raise ValueError
    except ValueError:
        print("Öyle bir cihaz yok")


def kontrol_et(gir):
    while True:
        deger = input(gir)
        if not deger.isdigit() or len(deger) > 5:
            print("Geçersiz giriş")
        else:
            print("Geçerli giriş")
            break
    return int(deger)


itibaren = kontrol_et("Kaçtan itibaren?\n")
kadar = kontrol_et("Kaça kadar?\n")

if kadar - itibaren < 0:
    print("İkinci birinciden küçük olamaz.")
    kadar = kontrol_et("Kaça kadar?\n")


def sifirlari_kontrol_et(uzunluk):
    if len(str(uzunluk)) > 5:
        return "NULL"
    return "0" * (5 - len(str(uzunluk)))


if cihaz == 5 or cihaz == 7 or cihaz == 11 or cihaz == 16 or cihaz == 18:
    while True:
        if kadar - itibaren > 8:
            print("Küçük barkodlarda, en fazla 9 etiket çıkartabilirsin")
            kadar = kontrol_et("Kaça kadar?\n")
            continue
        elif kadar - itibaren < 9:
            break

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2)

    for i in range(itibaren, kadar + 1):
        sifirSayisi = sifirlari_kontrol_et(i)

        qr.add_data(kod + sifirSayisi + str(i))
        qr.make(fit=True)
        img_qr = qr.make_image()
        logo = Image.open(directory + "/" + "bin" + "/" + "movus2.jpeg")
        draw = ImageDraw.Draw(logo)
        font = ImageFont.truetype(fontpath, 40)
        draw.text((int(530), (int(img_qr.size[1]))),
                  kod + sifirSayisi + str(i), fill=(0, 0, 0), font=font)

        pos = (530, 0)
        logo.paste(img_qr, pos)
        logo.save(kod + sifirSayisi + str(i) + ".png")

        qr.clear()

    for i, j in zip(range(itibaren, itibaren + 2), (range(0, kadar - itibaren))):
        sifirSayisi = sifirlari_kontrol_et(itibaren + j)
        newlogo = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j) + ".png")
        sifirSayisi = sifirlari_kontrol_et(itibaren + j + 1)
        newLogo1 = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j + 1) + ".png")
        pos = (900 + j * 900, 0)
        newlogo.paste(newLogo1, pos)
        newlogo.save(directory + "/" + kod + sifirSayisi + str(itibaren + j + 1) + ".png")

    for i, j in zip(range(itibaren + 3, itibaren + 6), (range(0, kadar - itibaren - 2))):
        if kadar - itibaren > 2:
            sifirSayisi = sifirlari_kontrol_et(itibaren + j + 2)
            newlogo = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j + 2) + ".png")
            sifirSayisi = sifirlari_kontrol_et(itibaren + j + 3)
            newLogo1 = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j + 3) + ".png")
            pos = (0 + j * 900, 450)
            newlogo.paste(newLogo1, pos)
            newlogo.save(directory + "/" + kod + sifirSayisi + str(itibaren + j + 3) + ".png")

    for i, j in zip(range(itibaren + 6, itibaren + 9), (range(0, kadar - itibaren - 5))):
        if kadar - itibaren > 5:
            sifirSayisi = sifirlari_kontrol_et(itibaren + j + 5)
            newlogo = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j + 5) + ".png")
            sifirSayisi = sifirlari_kontrol_et(itibaren + j + 6)
            newLogo1 = Image.open(directory + "/" + kod + sifirSayisi + str(itibaren + j + 6) + ".png")
            pos = (0 + j * 900, 900)
            newlogo.paste(newLogo1, pos)
            newlogo.save(directory + "/" + kod + sifirSayisi + str(itibaren + j + 6) + ".png")

    for i in range(itibaren, kadar):
        sifirSayisi = sifirlari_kontrol_et(i)
        os.remove(directory + "/" + kod + sifirSayisi + str(i) + ".png")
else:

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=4)

    for i in range(itibaren, kadar + 1):
        sifirSayisi = sifirlari_kontrol_et(i)

        qr.add_data(kod + sifirSayisi + str(i))
        qr.make(fit=True)
        img_qr = qr.make_image()
        logo = Image.open(directory + "/" + "bin" + "/" + "movus.jpeg")
        draw = ImageDraw.Draw(logo)
        font = ImageFont.truetype(fontpath, 40)
        draw.text((int(logo.size[0] - img_qr.size[0] + 110), (int(logo.size[1] - 90))),
                  kod + sifirSayisi + str(i), fill=(0, 0, 0), font=font)

        yCoord = int((logo.size[1] - img_qr.size[1])) - 90
        xCoord = int(logo.size[0] - img_qr.size[0])

        pos = (xCoord, yCoord)
        logo.paste(img_qr, pos)

        logo.save(kod + sifirSayisi + str(i) + ".png")
        qr.clear()
