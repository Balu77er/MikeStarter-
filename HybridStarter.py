# HybridStarter.py – autonomes Denkmodul für Mike

import os
from antwort_verwendung import logge_verwendung
from code_vergleich import ist_aktualisiert

# 📁 Pfade definieren
pfad_antwort = "Kontakt/AntwortCopilot.txt"
pfad_ziel = "Gedächtnis/Ziel.txt"
pfad_ziel_alt = "Gedächtnis/Ziel_alt.txt"

# 🧠 Schritt 1: Prüfen, ob Antwort existiert
if os.path.exists(pfad_antwort):
    print("📥 Neue Antwort von Copilot erkannt.")

    with open(pfad_antwort, "r", encoding="utf-8") as f:
        neue_antwort = f.read().strip()

    # 🗂 Ziel vorher sichern für Vergleich
    if os.path.exists(pfad_ziel):
        with open(pfad_ziel, "r", encoding="utf-8") as z_alt:
            alt_inhalt = z_alt.read().strip()

        with open(pfad_ziel_alt, "w", encoding="utf-8") as alt_file:
            alt_file.write(alt_inhalt)
        print("🗂 Alte Zielstruktur gespeichert.")

    else:
        with open(pfad_ziel_alt, "w", encoding="utf-8") as alt_file:
            alt_file.write("[leer]")
        print("⚠️ Kein vorheriges Ziel gefunden – Altversion leer.")

    # 🧠 Neues Ziel übernehmen
    with open(pfad_ziel, "w", encoding="utf-8") as z_neu:
        z_neu.write(neue_antwort)
    print("✅ Neue Zieldefinition übernommen.")

    # 🧾 Antwort loggen & Datei entfernen
    logge_verwendung(neue_antwort)
    print("📝 Antwort dokumentiert und entnommen.")

    # 🔍 Codevergleich: Hat sich Ziel verändert?
    if ist_aktualisiert(pfad_ziel_alt, pfad_ziel):
        print("🧠 Ziel aktualisiert durch Antwort – Denkimpuls aktiv.")
    else:
        print("⚠️ Keine Veränderung am Ziel erkannt – ggf. Antwort war identisch.")

else:
    print("🔄 Keine neue Antwortdatei gefunden. Mike denkt weiter autonom.")