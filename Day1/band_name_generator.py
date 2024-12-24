def band_name_generator():
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    band_name = city +' '+ pet_name
    return band_name

def main():
    print("welcome to the Band Name Generator.")
    band_name = band_name_generator()
    print(f"Your band name could be {band_name}")
