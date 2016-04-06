cenik_izdelkov = {"krompir": 0.75, "banane": 1.2, "salama": 2.2, "sir": 1.8, "kruh": 2.1}

def cena(izdelek):
    if izdelek == "krompir":
        return cenik_izdelkov["krompir"]
    elif izdelek == "banane":
        return cenik_izdelkov["banane"]
    elif izdelek == "salama":
        return cenik_izdelkov["salama"]
    elif izdelek == "sir":
        return cenik_izdelkov["sir"]
    elif izdelek == "kruh":
        return cenik_izdelkov["kruh"]
    else:
        return "Tega izdelka ni na ceniku."

if __name__ == "__main__":
    while True:
        izdelek = (raw_input("Za informacijo o ceni vtipkajte ime izdelka:").lower())
        print "Cena izdelka je: ", cena(izdelek)