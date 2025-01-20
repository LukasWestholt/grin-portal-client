# Installation und Ausführung von `grin-portal-client`

This python package is for https://grin-portal.broadinstitute.org/.

### 1. Poetry installieren

Stelle sicher, dass **Poetry** auf deinem System installiert sind.

Um **Poetry** zu installieren, führe den folgenden Befehl aus:

```bash
pip install poetry
````

#### Überprüfe die Installation

```bash
poetry --version
````

Falls der Befehl fehlschlägt, muss `Python\Scripts` in die PATH Umgebungsvariable.

### 2. Projekt installieren
Klonen oder lade das Projekt herunter. Gehe dann in das Projektverzeichnis und führe den folgenden Befehl aus,
um alle Abhängigkeiten zu installieren:


```bash
poetry install --dev
````

### 3. Anwendung ausführen
Du kannst das Projekt mit Poetry ausführen, indem du folgenden Befehl verwendest:

```bash
poetry run grin-portal-client
````

oder

```bash
poetry run python -m grin-portal-client
````

### 4. Tests ausführen
Um Tests auszuführen (falls vorhanden), verwende:

```bash
poetry run pytest
````
