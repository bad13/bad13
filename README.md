# BSI Grundschutz Webtool

Dieses Repository enthält ein einfaches Beispiel für eine lokale Webanwendung zur Unterstützung des IT-Grundschutz nach Vorgaben des BSI (Bundesamt für Sicherheit in der Informationstechnik).

Die Anwendung basiert auf [Flask](https://flask.palletsprojects.com/) und lässt sich auf einem PC oder Notebook starten. Sie dient als Minimalbeispiel für eine portable Lösung ohne Benutzerverwaltung.

## Voraussetzungen
* Python 3.8 oder neuer
* Abhängigkeiten aus `requirements.txt`

Installation der Abhängigkeiten:
```bash
pip install -r grundschutz_tool/requirements.txt
```

## Starten der Anwendung
```bash
python grundschutz_tool/app.py
```

Danach ist die Weboberfläche unter `http://127.0.0.1:5000` erreichbar.

Die Beispielkonfiguration in `controls.json` zeigt exemplarisch zwei Kontrollen des IT-Grundschutz. Sie kann erweitert werden, um weitere Anforderungen abzubilden.
