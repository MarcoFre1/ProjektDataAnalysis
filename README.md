# Projekt Data Analysis
## Beschreibung
Ziel des folgenden Projekts ist es, aus einer großen Sammlung an Rezensionen mittels Natural Language Processing (NLP) Techniken die am häufigsten genannten Themen zu extrahieren,
um fiktiven Entscheidungsträgern zu zeigen, 
welche Punkte am häufigsten angesprochen werden, um so in der Folge die Produktqualität zu verbessern.<br>
<br>
Zum Einsatz kommende Methoden, sind:<br>
- Textvorverarbeitung<br>
- Bag-of-Words (BoW)<br>
- TF-IDF<br>
- Latent Semantic Analysis (LSA)<br>
- Latent Dirichlet Allocation (LDA)<br>


## System Requirements

Folgendes Tool wird zum Herunterladen des Repositorys benötigt:<br>
-> Git-SCM: https://git-scm.com/downloads<br>

Weiters ist eine Conda-Umgebung zum Aktivieren der Umgebung, sowie zum Ausführen des Pyhton-Skripts nötig:<br>
-> Anaconda- oder Miniconda-Distributionen: https://www.anaconda.com/download | https://docs.anaconda.com/miniconda/

## Installation

Um dieses Projekt auszuführen, müssen zuerst eine Conda-Umgebung eingerichtet und die erforderlichen Pakete installiert werden. <br>
Stellen Sie sicher, dass Conda auf Ihrem System installiert ist. <br>
Beachten Sie dazu bitte die Installationsanweisungen des Herstellers: https://docs.anaconda.com/anaconda/install/windows/

Folgen Sie anschließend den beschriebenen Anweisungen:

<b>1. Klonen des Repositorys</b><br>
<div>
  <pre style="display: inline-block; padding: 5px; background-color: #e3f2fd; border-radius: 5px;">
    <code id="command">git clone https://github.com/MarcoFre1/ProjektDataAnalysis</code>
  </pre>
  <button onclick="copyToClipboard()" style="background-color: #007BFF; color: white; padding: 5px; border: none; border-radius: 5px; cursor: pointer; display: inline-block; vertical-align: left;">
  </button>
</div>

Achtung: Mit <b>cd</b> in den Repository-Pfad wechseln
<br><br>
<b>2. Erstellen der Conda-Umgebung unter Windows</b>
<br>
<div>
  <pre style="display: inline-block; padding: 5px; background-color: #e3f2fd; border-radius: 5px;">
    <code id="command">conda env create -f environmentWindows.yml</code>
  </pre>
  <button onclick="copyToClipboard()" style="background-color: #007BFF; color: white; padding: 5px; border: none; border-radius: 5px; cursor: pointer; display: inline-block; vertical-align: left;">
  </button>
</div>
<br>
<b>3. Aktivieren der Umgebung</b>
<br><br>
<div>
  <pre style="display: inline-block; padding: 5px; background-color: #e3f2fd; border-radius: 5px;">
    <code id="command">conda activate ProjektDataAnalysis</code>
  </pre>
  <button onclick="copyToClipboard()" style="background-color: #007BFF; color: white; padding: 5px; border: none; border-radius: 5px; cursor: pointer; display: inline-block; vertical-align: left;">
  </button>
</div>
<br>
<b>4. Ausführen des Programms</b>
<br><br>
<div>
  <pre style="display: inline-block; padding: 5px; background-color: #e3f2fd; border-radius: 5px;">
    <code id="command">python PythonCode.py</code>
  </pre>
  <button onclick="copyToClipboard()" style="background-color: #007BFF; color: white; padding: 5px; border: none; border-radius: 5px; cursor: pointer; display: inline-block; vertical-align: left;">
  </button>
</div>

## Funktionen des Codes

## Hinweise

