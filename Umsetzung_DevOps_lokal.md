# Umsetzung DevOps lokal – Wechselkurs-API

## Beschreibung der Umsetzung

Für die lokale Umsetzung einer DevOps-Übung wurde eine kleine Wechselkurs-API mit Python und FastAPI entwickelt. Ziel ist es, einen Betrag mit einem angegebenen Wechselkurs umzurechnen und das Ergebnis als API-Antwort bereitzustellen. Die Umsetzung erfolgte in folgenden Schritten:

1. **Projektstruktur und Vorbereitung**
   - Ein neues Verzeichnis wurde angelegt und die Datei `wechselkurs.py` erstellt.
   - Die benötigten Python-Pakete (`fastapi`, `uvicorn`, `pydantic`) wurden in einer virtuellen Umgebung installiert.

2. **Implementierung der API**
   - Mit FastAPI wurde eine Web-API erstellt, die einen POST-Endpunkt `/wechseln` bereitstellt.
   - Die API erwartet ein JSON-Objekt mit den Feldern `betrag` (float) und `wechselkurs` (float).
   - Die Umrechnung erfolgt in einer eigenen Funktion, das Ergebnis wird als JSON zurückgegeben.

3. **Testen der API**
   - Die API wurde lokal mit folgendem Befehl gestartet:
     ```
     uvicorn wechselkurs:app --reload
     ```
   - Ein Testaufruf erfolgte über ein Jupyter Notebook mit dem Python-Paket `requests`:
     ```python
     import requests
     url = "http://127.0.0.1:8000/wechseln"
     payload = {"betrag": 100, "wechselkurs": 1.08}
     resp = requests.post(url, json=payload)
     print(resp.json())
     ```
   - Die Antwort der API enthält das umgerechnete Ergebnis im JSON-Format.

4. **Modell und Zusammenhang der Elemente**
   - Die API besteht aus einem FastAPI-Server, der Anfragen entgegennimmt und verarbeitet.
   - Die Kommunikation erfolgt über HTTP (POST) und JSON als Datenformat.
   - Die Trennung von Logik (Umrechnungsfunktion) und API-Definition sorgt für Übersichtlichkeit und Wartbarkeit.

## Name des Screenvideos
Das Screenvideo zur Demonstration des API-Aufrufs und der Antwort ist separat abzugeben und trägt den Namen: `wechselkurs_api_demo.mp4`

---

*Dieses Dokument beschreibt die einzelnen Arbeitsschritte zur lokalen Umsetzung der Wechselkurs-API. Das Screenvideo ist nicht enthalten.*
