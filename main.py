sozluk = {
    "VIBE": "bir seyin cagristirdigi sey veya verdigi his",
    "CRINGE": "utanc verici veya degisik bir sey",
}

kelime = input("Anlamadıgınız bir sozcuk yazın (buyuk harflerle)")

if kelime in sozluk.keys():
    print(sozluk[kelime])
else:
    print("Bu kelime sözlukte yok")
