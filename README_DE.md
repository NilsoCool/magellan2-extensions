# ConsoleMerger für Magellan 2.1.1

[![Version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://github.com/yourusername/consolemerger)
[![Java](https://img.shields.io/badge/java-11%2B-orange.svg)](https://www.oracle.com/java/technologies/javase-jre11-downloads.html)
[![Magellan](https://img.shields.io/badge/magellan-2.1.1-green.svg)](https://github.com/Magellan2/Magellan2)

Automatisiertes Report-Merge-Tool für Magellan 2.1.1 / Eressea mit Headless-Unterstützung.

## Neu in v1.0.3

- ✅ **Nachrichten-Tags wiederhergestellt** - Farbklassifizierung (Wirtschaft/Kampf) bleibt erhalten (Fix für erstes Öffnen).
- ✅ **Prozess-Exit Fix** - Beendet sich jetzt sauber mit `System.exit(0)` für bessere Automatisierung.
- ✅ **Automation Kit** - Python-Skripte für Massenverarbeitung enthalten.
- ⚠️ **Hinweis**: Magellan-Client entfernt Farbtags beim Speichern - Datei als Master-Kopie behalten

## Anforderungen

- Java 11+
- Magellan 2.1.1 Bibliotheken

## Schnellstart

### Verzeichnisstruktur

```
AutoMagellan/
├── bin/
│   ├── consolemerger-for2.1.1.jar
│   └── lib/                    # Alle Magellan 2.1.1 JARs
├── magellan_context/
│   ├── rules/                  # Von Magellan 2.1.1
│   └── resources/              # Von Magellan 2.1.1
└── data/
    ├── temp/                   # Eingabe .cr Dateien
    └── output/                 # Fusioniertes Ergebnis
```

### Verwendung

**Windows:**
```cmd
java -cp "bin\consolemerger-for2.1.1.jar;bin\lib\*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data\temp\basis.cr" "data\temp\zug.cr" "data\output\ergebnis.cr"
```

**Linux/Mac:**
```bash
java -cp "bin/consolemerger-for2.1.1.jar:bin/lib/*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data/temp/basis.cr" "data/temp/zug.cr" "data/output/ergebnis.cr"
```

## Einrichtung

1. Erforderliche Dateien von [Magellan 2.1.1](https://github.com/Magellan2/Magellan2) herunterladen:
   - [Rules](https://github.com/Magellan2/Magellan2/tree/master/magellan2/etc/rules) → `magellan_context/rules/`
   - [Resources](https://github.com/Magellan2/Magellan2/tree/master/magellan2/etc) → `magellan_context/resources/`

2. Alle Magellan 2.1.1 Bibliotheks-JARs in `bin/lib/` platzieren

## Automation Kit (Neu!)

Wir stellen jetzt ein robustes Python-Automatisierungs-Kit für Massenverarbeitung bereit.
Siehe Verzeichnis [`automation_kit/`](automation_kit/) für Skripte und Anleitungen.

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| `ClassNotFoundException` | Alle JARs in `bin/lib/` und Classpath-Reihenfolge prüfen |
| Parser schlägt fehl | `rules/eressea/` und `resources/` müssen existieren |
| Farben verloren | Nicht im Magellan-Client speichern - als read-only behalten |

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei

---

[Issues melden](https://github.com/yourusername/consolemerger/issues) • Erstellt für die Eressea-Community
