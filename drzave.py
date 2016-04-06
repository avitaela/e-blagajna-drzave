seznam_drzav_in_mest = {"Slovenija": "Ljubljana", "Italija": "Rim", "Avstrija": "Dunaj", "Madzarska": "Budinpesta", "Hrvaska": "Zagreb"}

def glavno_mesto(drzava):
    mesto = seznam_drzav_in_mest[drzava]
    return mesto

if __name__ == "__main__":
    for x in range(0, 10):
        vnesena_drzava = raw_input("Vnesi ime drzave: ")
        if vnesena_drzava in seznam_drzav_in_mest:
            print "Glavno mesto", vnesena_drzava, "je:", glavno_mesto(vnesena_drzava)
        else:
            print "Vnesena drzava ni v seznamu."



