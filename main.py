# Wechselkursrechner: Gibt den Betrag in einer anderen Währung aus
from fastapi import FastAPI            # Importiert die FastAPI-Klasse, um eine Web-API zu erstellen
from pydantic import BaseModel         # Importiert die BaseModel-Klasse für Daten-Validierung und -Serialisierung
from typing import Optional

# FastAPI-App initialisieren
app = FastAPI()

# Pydantic-Modell für die Anfrage
class WechselkursRequest(BaseModel):
    betrag: float
    wechselkurs: float

# Pydantic-Modell für die Antwort
class WechselkursResponse(BaseModel):
    ergebnis: float

def wechselkurs_rechner(betrag: float, wechselkurs: float) -> float:
    """
    Wandelt einen Betrag mit dem angegebenen Wechselkurs um.
    :param betrag: float, Betrag in der Ausgangswährung
    :param wechselkurs: float, Umrechnungsfaktor zur Zielwährung
    :return: float, Betrag in der Zielwährung
    """
    return betrag * wechselkurs


# FastAPI-Endpunkt
@app.post("/wechseln", response_model=WechselkursResponse)
def berechne_wechselkurs(request: WechselkursRequest):
    ergebnis = wechselkurs_rechner(request.betrag, request.wechselkurs)
    return WechselkursResponse(ergebnis=ergebnis)

if __name__ == "__main__":
    try:
        betrag = float(input("Geben Sie den Betrag ein: "))
        wechselkurs = float(input("Geben Sie den Wechselkurs ein: "))
        ergebnis = wechselkurs_rechner(betrag, wechselkurs)
        print(f"{betrag} umgerechnet mit Kurs {wechselkurs} ergibt {ergebnis:.2f}")
    except ValueError:
        print("Bitte geben Sie gültige Zahlen ein.")
    print("\nStarte FastAPI-App mit: uvicorn wechselkurs:app --reload")