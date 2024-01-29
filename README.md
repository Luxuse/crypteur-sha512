# crypteur-sha512

# Crypteur de Mot de Passe SHA-512

Un script simple en Python qui utilise l'algorithme de hachage SHA-512 pour crypter les mots de passe. Il offre une option pour sauvegarder les mots de passe cryptés dans un fichier.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/crypteur-sha512.git
   cd crypteur-sha512


python encrypteur.py


Suivez les instructions du menu pour crypter un mot de passe et, éventuellement, le sauvegarder dans un fichier.
Fonctionnalités

    Crypte les mots de passe en utilisant SHA-512.
    Permet de sauvegarder les mots de passe cryptés dans un fichier.

test on 

*Windows 
*termux
*linux

Exemples

python

# Exemple d'utilisation dans du code Python

from crypteur_sha512 import encrypt_password, save_to_file

password_to_encrypt = "MotDePasseSecret"
encrypted_password = encrypt_password(password_to_encrypt)
save_to_file(password_to_encrypt, encrypted_password, 'passwords.txt')

Contribuer

Les contributions sont les bienvenues ! Suivez ces étapes pour contribuer :

    Forkez le projet
    Créez une branche pour votre fonctionnalité (git checkout -b fonctionnalite/nom)
    Committez vos changements (git commit -am 'Ajoutez une fonctionnalité')
    Poussez vers la branche (git push origin fonctionnalite/nom)
    Créez une nouvelle pull request

Licence

mit
