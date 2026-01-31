# ConsoleMerger for Magellan 2.1.1

[![Version](https://img.shields.io/badge/version-1.0.3-blue.svg)](https://github.com/yourusername/consolemerger)
[![Java](https://img.shields.io/badge/java-11%2B-orange.svg)](https://www.oracle.com/java/technologies/javase-jre11-downloads.html)
[![Magellan](https://img.shields.io/badge/magellan-2.1.1-green.svg)](https://github.com/Magellan2/Magellan2)

Automated report merging tool for Magellan 2.1.1 / Eressea with headless support.

## What's New in v1.0.3

- ✅ **Message Tags Restored** - Fixes bug where color tags (Economy/Battle) were lost on first open.
- ✅ **Process Termination Fix** - Now exits cleanly with `System.exit(0)` for better automation support.
- ✅ **Automation Kit** - Included Python scripts for bulk merging.
- ⚠️ **Note**: Magellan client removes color tags on save - keep the merged file as read-only master

## Requirements

- Java 11+
- Magellan 2.1.1 libraries

## Quick Start

### Directory Structure

```
AutoMagellan/
├── bin/
│   ├── consolemerger-for2.1.1.jar
│   └── lib/                    # All Magellan 2.1.1 JARs
├── magellan_context/
│   ├── rules/                  # From Magellan 2.1.1
│   └── resources/              # From Magellan 2.1.1
└── data/
    ├── temp/                   # Input .cr files
    └── output/                 # Merged result
```

### Usage

**Windows:**
```cmd
java -cp "bin\consolemerger-for2.1.1.jar;bin\lib\*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data\temp\base.cr" "data\temp\turn.cr" "data\output\merged.cr"
```

**Linux/Mac:**
```bash
java -cp "bin/consolemerger-for2.1.1.jar:bin/lib/*" magellan.ext.console.merge.ConsoleMerger "magellan_context" "data/temp/base.cr" "data/temp/turn.cr" "data/output/merged.cr"
```

## Setup

1. Download required files from [Magellan 2.1.1](https://github.com/Magellan2/Magellan2):
   - [Rules](https://github.com/Magellan2/Magellan2/tree/master/magellan2/etc/rules) → `magellan_context/rules/`
   - [Resources](https://github.com/Magellan2/Magellan2/tree/master/magellan2/etc) → `magellan_context/resources/`

2. Place all Magellan 2.1.1 library JARs in `bin/lib/`

## Automation Kit (New!)

We now provide a robust Python based automation kit for bulk merging.
Check the [`automation_kit/`](automation_kit/) directory for scripts and instructions.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ClassNotFoundException` | Verify all JARs in `bin/lib/` and classpath order |
| Parser fails | Check `rules/eressea/` and `resources/` exist |
| Colors lost | Don't save in Magellan client - keep as read-only |

## License

MIT License - see [LICENSE](LICENSE) file

---

[Report Issues](https://github.com/yourusername/consolemerger/issues) • Made for the Eressea community
