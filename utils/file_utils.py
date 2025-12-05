"""Utility functions for file operations related to RSA keys and text documents.

This module provides:
- Loading text files into a Tkinter canvas.
- Saving and loading RSA public and private keys in JSON format.
"""

import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog


def load_file_to_canvas(text: str) -> None:
    """Allow user to open document into tkinter canva.

    Args:
        text: Text actually display in the canva

    Raises:
        FileNotFoundError: If file not found or doesn't exist.

    """
    filename = filedialog.askopenfilename(title="Ouvrir votre document",
                                          filetypes=[("txt files", ".txt"), ("all files", ".*")])
    try:
        with Path.open(filename) as fichier:
            content = fichier.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
    except FileNotFoundError as e:
        msg = "Le fichier n'a pas été sélectionné ou n'existe pas."
        raise FileNotFoundError(msg) from e

def save_secret_key(d: int, n: int) -> None:
    """Save the RSA private key to a file in JSON format.

    Args:
        d: The private exponent.
        n: The modulus of the private key.

    """
    file_path = Path("rsa_secret")
    with file_path.open("w") as f:
        dico = {"n": n, "d": d}
        json.dump(dico, f, indent=2)

def load_secret_key() -> tuple[int,int]:
    """Load the RSA private key from a JSON file.

    Returns:
        A tuple containing (d, n) if the file exists and is valid, otherwise None.

    """
    try:
        file_path = Path("rsa_secret")
        f = file_path.open()
        r = json.load(f)
        return r["d"], r["n"]
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None

def save_public_key(e: int, n: int) -> None:
    """Save the RSA public key to a file in JSON format.

    Args:
        e: The public exponent.
        n: The modulus of the public key.

    """
    file_path = Path("rsa_public")
    with file_path.open("w") as f:
        dico = {"n": n, "e": e}
        json.dump(dico, f, indent=2)

#Fonction de récupération de cle public
def load_public_key() -> tuple[int,int]:
    """Load the RSA public key from a JSON file.

    Returns:
        A tuple containing (e, n) if the file exists and is valid, otherwise None.

    """
    try:
        file_path = Path("rsa_public")
        f = file_path.open()
        r = json.load(f)
        return r["e"], r["n"]
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
