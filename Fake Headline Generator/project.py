import random

# Desi subject list
subjects = [
    "Lahore ka chota Don",
    "Chai wala AI robot",
    "Nani ka WhatsApp group",
    "Biryani obsessed cat",
    "Tiktok wali aunty",
    "Karachi ka Dracula",
    "Gujranwala ke gym boys"
]

# Desi actions list
actions = [
    "ne load-shedding ka badla le liya",
    "ne biryani mein pineapple daal di",
    "ne Metro bus hijack karli",
    "ne PSL trophy chura li",
    "ko PCB ka chairman bana diya gaya",
    "ne school ki bell baja kar bhaag gaya",
    "ne Math paper viral kar diya"
]

# Desi places list
places = [
    "Lahore ki Landa Bazaar mein",
    "Multan ke dahi bhallay stall ke pass",
    "Murree ke baraf mein",
    "Rawalpindi Express ke engine mein",
    "Islamabad ke Centaurus mall ke samne",
    "Sialkot ke wedding hall mein",
    "Gulshan-e-Iqbal ke signal par"
]

# While loop to ask again
while True:
    headline = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(places)}."
    print("\n Desi Headline:", headline)

    choice = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if choice != 'yes':
        print(" Generator stopped. Mazedaar headlines khatam! ")
        break

print("\n Apka Shukria Yahan Ana ka liya")