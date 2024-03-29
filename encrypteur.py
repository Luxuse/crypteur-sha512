import hashlib

def encrypt_password(password):
    sha512 = hashlib.sha512()
    sha512.update(password.encode('utf-8'))
    return sha512.hexdigest()

def save_to_file(password, hashed_password, filename):
    with open(filename, 'a') as file:
        file.write(f"{password}={hashed_password}\n")

def main():
    while True:
        print("Menu :")
        print("1. Crypter et sauvegarder un mot de passe")
        print("2. Quitter")

        choice = input("Entrez votre choix (1 ou 2) : ")

        if choice == '1':
            password_to_encrypt = input("Entrez le mot de passe à crypter : ")
            encrypted_password = encrypt_password(password_to_encrypt)
            print("Mot de passe original :", password_to_encrypt)
            print("Mot de passe crypté en SHA-512 :", encrypted_password)
            
            save_choice = input("Voulez-vous sauvegarder le mot de passe dans un fichier ? (Oui/Non) : ")
            if save_choice.lower() == 'oui':
                save_to_file(password_to_encrypt, encrypted_password, 'passwords.txt')
                print("Mot de passe sauvegardé avec succès.")
        elif choice == '2':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()


