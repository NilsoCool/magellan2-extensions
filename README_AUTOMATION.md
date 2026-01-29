# ConsoleMerger for Magellan 2.1.1 - Automation Setup
# ConsoleMerger für Magellan 2.1.1 - Automatisierungs-Setup

**Version:** V.1.0.2 (Economy Patch)
**Compatible:** Magellan 2.1.1 (2025/2026) / Eressea
**Java Required:** JRE 11+

---

## 🇬🇧 English Documentation

This patched version of ConsoleMerger is designed to run in a headless environment (e.g., triggered by Python scripts). It fixes the "lost color tags" issue and is compatible with modern Magellan library changes.

### 1. Recommended Directory Structure

To ensure stability, your automation environment should follow this exact structure. The Java command depends on the libs being separated from the jar.

```text
AutoMagellan/
├── bin/
│   ├── consolemerger-for2.1.1.jar      # The patched executable
│   └── lib/                            # MUST contain all jars from Magellan 2.1.1 libs
│       ├── magellan-library.jar
│       ├── commons-beanutils.jar
│       ├── jdom.jar
│       └── ... (all other dependencies)
│
├── magellan_context/                   # The "Brain" (Magellan Dir)
│   ├── rules/                          # COPY from your Magellan 2.1.1 installation
│   │   ├── eressea/                    # Essential for parsing Eressea reports
│   │   └── ...
│   └── resources/                      # COPY from Magellan installation (i18n)
│
└── data/                               # Working directory (Managed by Python)
    ├── inbox/                          # Where Python puts downloaded zips
    ├── temp/                           # Extracted .cr files
    └── output/                         # Final merged result
```

### 2. Command Line Usage

Your Python script must execute the following Java command.
**Note:** The Classpath (`-cp`) order is critical. `consolemerger` must be first.

**Windows Syntax:**
```batch
java -cp "bin\consolemerger-for2.1.1.jar;bin\lib\*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data\temp\base_report.cr" "data\temp\turn_report.cr" "data\output\merged_final.cr"
```

**Linux/Mac Syntax:**
```bash
java -cp "bin/consolemerger-for2.1.1.jar:bin/lib/*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data/temp/base_report.cr" "data/temp/turn_report.cr" "data/output/merged_final.cr"
```

### 3. Python Integration Notes

*   **Classpath:** Ensure you include all JARs in `bin/lib/`.
*   **Context:** The first argument (`magellan_context`) must point to a folder containing valid `rules` and `resources` subfolders. Without this, the parser will fail or drop data.

---

## 🇩🇪 Deutsche Dokumentation

Diese gepatchte Version des ConsoleMerger wurde für den Einsatz in automatisierten Umgebungen (z.B. Python-Skripte) entwickelt. Sie behebt das Problem der verlorenen Farbtags ("economy", "battle") und ist mit den Änderungen der Magellan 2.1.1 Bibliotheken kompatibel.

### 1. Empfohlene Verzeichnisstruktur

Für einen stabilen Betrieb sollte Ihre Automatisierungsumgebung dieser Struktur folgen. Der Java-Befehl setzt voraus, dass die libs vom jar getrennt sind.

```text
AutoMagellan/
├── bin/
│   ├── consolemerger-for2.1.1.jar      # Die gepatchte ausführbare Datei
│   └── lib/                            # MUSS alle JARs von Magellan 2.1.1 enthalten
│       ├── magellan-library.jar
│       ├── commons-beanutils.jar
│       ├── jdom.jar
│       └── ... (alle anderen Abhängigkeiten)
│
├── magellan_context/                   # Das "Gehirn" (Magellan Verzeichnis)
│   ├── rules/                          # KOPIE aus Ihrer Magellan 2.1.1 Installation
│   │   ├── eressea/                    # Unverzichtbar für Eressea-Reports
│   │   └── ...
│   └── resources/                      # KOPIE aus der Installation (Übersetzungen)
│
└── data/                               # Arbeitsverzeichnis (Verwaltet von Python)
    ├── inbox/                          # Python legt hier heruntergeladene Zips ab
    ├── temp/                           # Entpackte .cr Dateien
    └── output/                         # Das fertige, fusionierte Ergebnis
```

### 2. Verwendung (Kommandozeile)

Ihr Python-Skript muss den folgenden Java-Befehl ausführen.
**Hinweis:** Die Reihenfolge im Classpath (`-cp`) ist entscheidend. `consolemerger` muss an erster Stelle stehen.

**Windows Syntax:**
```batch
java -cp "bin\consolemerger-for2.1.1.jar;bin\lib\*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data\temp\basis_report.cr" "data\temp\zug_report.cr" "data\output\ergebnis.cr"
```

**Linux/Mac Syntax:**
```bash
java -cp "bin/consolemerger-for2.1.1.jar:bin/lib/*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data/temp/basis_report.cr" "data/temp/zug_report.cr" "data/output/ergebnis.cr"
```

### 3. Hinweise zur Python-Integration

*   **Classpath:** Stellen Sie sicher, dass alle JAR-Dateien in `bin/lib/` eingebunden sind.
*   **Kontext:** Das erste Argument (`magellan_context`) muss auf einen Ordner zeigen, der gültige Unterordner für `rules` und `resources` enthält. Ohne dies wird der Parser fehlschlagen oder Daten verlieren.
