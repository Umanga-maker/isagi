from random import choice

capital = "Kathmandu"

bird = "Lophophorus"

flower = "Rhododendron"

song = "Yo Mann ta mero nepali hoo"

def randomfunfact():
    funfacts = ["Nepal is considered small, but it does have the highest peak.","Kathmandu is the city of thousand temples, but many would say it is polluted.","Beauty of nature can be found all over Nepal.","Most of Nepali youths go abroad for their better future."]

    index = choice ("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()