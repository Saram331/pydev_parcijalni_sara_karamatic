import json

# TODO: dodati type hinting na sve funkcije


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename: str) -> list[dict]:
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename: str, data: list[dict]) -> None:
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.




   
    # Omogućite unos kupca
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers
    # pass


# TODO: Implementirajte funkciju za upravljanje proizvodima. + radi
def manage_products(products: list[dict]) -> None:
    """
    Allows the user to add a new product or modify an existing product.
    """
    while True:
        print("\n1. Dodaj novi proizvod")
        print("2. Izmijeni postojeći proizvod")
        print("3. Izlaz")
        choice = input("Odaberite opciju: ")

        if choice == "1":
            
            name = input("Unesite naziv proizvoda: ")
            price = float(input("Unesite cijenu proizvoda: "))
            description = input("Unesite opis proizvoda: ")
            product = {
                "id": len(products) + 1,
                "name": name,
                "price": price,
                "description": description
            }
            products.append(product)
            print(f"Proizvod '{name}' uspješno dodan.")
            save_data(PRODUCTS_FILE, products)

        elif choice == "2":
            
            if not products:
                print("Nema proizvoda za izmjenu.")
                return

            print("\nLista proizvoda:")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product['name']} - ${product['price']}")

            while True:
                try:
                    product_choice = int(input("Odaberite broj proizvoda za izmjenu (ili 0 za povratak): "))
                    if product_choice == 0:
                        break
                    if 1 <= product_choice <= len(products):
                        product = products[product_choice - 1]
                        print(f"Trenutni podaci za proizvod: {product['name']} - {product['price']} -{product['description']}")
                        
                        new_name = input(f"Unesite novi naziv (trenutno: {product['name']}): ")
                        new_price = float(input(f"Unesite novu cijenu (trenutno: {product['price']}): "))
                        new_description = input(f"Unesite novi opis (trenutno: {product['description']}): ")
                        
                        product['name'] = new_name
                        product['price'] = new_price
                        product['description'] = new_description
                        print(f"Proizvod '{new_name}' uspješno izmijenjen.")
                        
                        save_data(PRODUCTS_FILE, products)
                        break
                    else:
                        print("Nevažeći broj proizvoda. Pokušajte ponovno.")
                except ValueError:
                    print("Pogrešan unos. Molimo unesite ispravan broj.")

        elif choice == "3":
            break
        else:
            print("Nevažeći unos. Pokušajte ponovno.")


   

    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke

    # pass


# TODO: Implementirajte funkciju za upravljanje kupcima. + radi
def manage_customers(customers: list[dict]) -> None:
    """
    Allows the user to add a new customer or view all customers.
    """

   
    while True:
        print("\n1. Dodaj novog kupca")
        print("2. Prikaži sve kupce")
        print("3. Povratak")
        choice = input("Odaberite opciju: ")

        if choice == "1":
            
            name = input("Unesite ime kupca: ")
            email = input("Unesite email kupca: ")
            vat_id = input("Unesite VAT ID kupca: ")
            customer = {
                "name": name,
                "email": email,
                "vat_id": vat_id
            }
            customers.append(customer)
            print(f"Kupac '{name}' uspješno dodan.")
            save_data(CUSTOMERS_FILE, customers)

        elif choice == "2":
            
            print("\nLista kupaca:")
            for customer in customers:
                print(f"{customer['name']} ({customer['email']}) - VAT ID: {customer['vat_id']}")

        elif choice == "3":
            break
        else:
            print("Nevažeći izbor. Pokušajte ponovno.")
   
   
   
   
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    # pass


# TODO: Implementirajte funkciju za prikaz ponuda.

def display_offers(offers: list[dict]) -> None:
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    while True:
        print("\n1. Prikaz svih ponuda")
        print("2. Prikaz ponuda za određeni mjesec")
        print("3. Prikaz pojedinačne ponude")
        print("4. Povratak")
        choice = input("Odaberite opciju: ")

        if choice == "1":
            for offer in offers:
                print_offer(offer)

        elif choice == "2":
            month = input("Unesite mjesec (brojkom - MM): ")
            for offer in offers:
                if offer['date'][:7] == f"{offer['date'][:4]}-{month}":
                    print_offer(offer)

        elif choice == "3":
            offer_id = int(input("Unesite ID ponude: "))
            for offer in offers:
                if offer['offer_number'] == offer_id:
                    print_offer(offer)
                    break
            else:
                print("Ponuda s tim ID-em ne postoji.")

        elif choice == "4":
            break
        else:
            print("Nevažeći izbor. Pokušajte ponovno.")


   
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    # pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer: dict) -> None:
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
