# 🪙 Coin Collector – Anleitung

Ein einfaches 2D-Sammelspiel-Projekt in Python mit pygame.

## 📋 Voraussetzungen

- **Python 3.11+** installiert
- **Git** (optional, für Versionskontrolle)
- Zugriff auf die Kommandozeile (PowerShell, CMD oder Terminal)

---

## 🚀 Installation & Setup

### 1. Virtuelle Umgebung erstellen
```powershell
python -m venv .venv
```

### 2. Virtuelle Umgebung aktivieren
**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 3. Abhängigkeiten installieren
```powershell
pip install -e .
```

Oder mit `uv` (schneller):
```powershell
uv pip install -e .
```

---

## 🎮 Spiel starten

### Basis-Befehl
```powershell
python -m coin_collector play --level src/coin_collector/levels/Nefzger_level.json
```

### Mit benutzerdefinierten Optionen
```powershell
python -m coin_collector play `
  --level src/coin_collector/levels/Nefzger_level.json `
  --fps 60 `
  --debug
```

**Parameter:**
- `--level` (erforderlich): Pfad zur Level-JSON-Datei
- `--fps` (optional, Standard: 60): Bilder pro Sekunde
- `--debug` (optional): Debug-Modus aktivieren


---

## 📁 Level-Dateien

Level werden als JSON-Dateien definiert. Beispiel-Struktur:

```json
{
  "width": 800,
  "height": 600,
  "player_start": {
    "x": 50,
    "y": 50
  },
  "coins": [
    {
      "x": 100,
      "y": 100,
      "r": 5
    }
  ],
  "walls": [
    {
      "x": 200,
      "y": 200,
      "w": 100,
      "h": 20
    }
  ]
}
```

**Felder:**
- `width` (int, 320-1920): Fensterbreite
- `height` (int, 240-1080): Fensterhöhe
- `player_start` (Vec2): Starposition des Spielers
- `coins` (Array): Münzen mit x, y, r (Radius)
- `walls` (Array, optional): Wände mit x, y, w, h (Breite, Höhe)

---

## 🎮 Spielsteuerung

- **Pfeiltasten / WASD**: Spieler bewegen
- **ESC / Fenster schließen**: Spiel beenden

---

## 🛠️ Entwicklung

### Projekt-Struktur
```
coin_collector/
├── src/coin_collector/
│   ├── __init__.py          # Paket-Initialisierung
│   ├── __main__.py          # CLI-Einstiegspunkt
│   ├── game.py              # Spiel-Logik
│   ├── draw.py              # Rendering-Funktionen
│   ├── config.py            # Datenmodelle & Level-Loader
│   └── levels/              # Level-Dateien
│       ├── level_example.json
│       └── Nefzger_level.json
├── pyproject.toml           # Projekt-Konfiguration
├── README.md                # Projekt-Beschreibung


### Abhängigkeiten
- **pygame 2.6.1+**: Spiel-Engine
- **pydantic 2.12.5+**: Datenvalidierung
- **typer 0.21.1+**: CLI-Framework
- **pytest 9.0.2+**: Unit-Tests
- **ruff 0.14.13+**: Code-Linting

---

## 🧪 Tests ausführen

```powershell
pytest
```

Mit Verbose-Output:
```powershell
pytest -v
```

---

## 🔍 Code-Qualität prüfen

### Mit Ruff linten
```powershell
ruff check src/
```

Automatisch beheben:
```powershell
ruff check src/ --fix
```

---

## 📦 Paket bauen

```powershell
uv build
```

Oder mit pip:
```powershell
pip install build
python -m build
```

---

## 🐛 Häufige Fehler

### Fehler: "ModuleNotFoundError: No module named 'pygame'"
**Lösung:** Abhängigkeiten installieren:
```powershell
pip install -e .
```

### Fehler: "Level-Datei nicht gefunden"
**Lösung:** Korrekten Pfad zur JSON-Datei angeben (absolut oder relativ):
```powershell
python -m coin_collector play --level ./src/coin_collector/levels/level_example.json
```

### Fehler: "pygame.error: video system not initialized"
**Lösung:** Im Debug-Modus testen:
```powershell
python -m coin_collector play --level src/coin_collector/levels/level_example.json --debug
```

---

## 💡 Tipps

- **Neue Levels erstellen:** Kopiere eine vorhandene Level-JSON und passe die Koordinaten an
- **FPS anpassen:** Für langsamere/schnellere Gameplay nutze `--fps`:
  ```powershell
  python -m coin_collector play --level src/coin_collector/levels/level_example.json --fps 30
  ```
- **Virtuelle Umgebung deaktivieren:**
  ```powershell
  deactivate
  ```

---

## 📧 Kontakt & Support

Bei Fragen oder Bugs bitte das Projekt überprüfen oder Issues öffnen.

---

**Viel Spaß beim Spielen! 🎮**
