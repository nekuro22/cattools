1️⃣ Version im Code aktualisieren

    Öffne cattools.py.

    Ändere die Versionsnummer in der Variable VERSION:

VERSION = "0.0.2"  # neue Version

    Speichere die Datei.

2️⃣ Neue Befehle hinzufügen

In cattools.py wird über sys.argv geprüft, was der Benutzer eingibt.
Beispiel: neuen Befehl hello hinzufügen

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print(VERSION)
        elif sys.argv[1] == "hello":
            print("Hallo von Cattools 😺")
        else:
            print(f"Unbekannter Befehl: {sys.argv[1]}")
    else:
        print("cattools – deine Toolsammlung\nNutze '--version' für Versionsinfo")

Jetzt kannst du im Terminal testen:

cattools hello

→ Ausgabe:

Hallo von Cattools 😺

Du kannst beliebig viele neue Befehle einbauen, z. B.:

elif sys.argv[1] == "install":
    print("Installiere alle Tools...")
elif sys.argv[1] == "update":
    print("Cattools aktualisieren...")

3️⃣ DEBIAN/control aktualisieren

    Öffne cattools_pkg/DEBIAN/control.

    Passe die Versionsnummer an:

Version: 0.0.2

Speichern und schließen.

    Wichtig: Package, Architecture, Maintainer etc. bleiben gleich.

4️⃣ .deb neu bauen

    Wechsle in das Verzeichnis über cattools_pkg:

dpkg-deb --build cattools_pkg

    Optional: neue Datei umbenennen:

mv cattools_pkg.deb cattools_0.0.2_all.deb

5️⃣ Neue Version installieren / Update testen

sudo apt install --reinstall ./cattools_0.0.2_all.deb

Prüfen:

cattools --version

→ Ausgabe sollte jetzt 0.0.2 sein.
✅ Zusammenfassung

    Version in cattools.py erhöhen.

    Neue Befehle in cattools.py hinzufügen.

    Version in cattools_pkg/DEBIAN/control anpassen.

    .deb neu bauen (dpkg-deb --build).

    Installieren oder updaten (sudo apt install --reinstall).

    Testen (cattools --version und neue Befehle).
