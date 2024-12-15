# Projekt Data Analysis
## Beschreibung
Ziel des folgenden Projekts ist es, aus einer großen Sammlung an Rezensionen mittels Natural Language Processing (NLP) Techniken die am häufigsten genannten Themen zu extrahieren,
um fiktiven Entscheidungsträgern zu zeigen, 
welche Punkte am häufigsten angesprochen werden, um so in der Folge die Produktqualität zu verbessern.<br>
<br>
Zum Einsatz kommende Methoden, sind:<br>
- Textvorverarbeitung<br>
- Bag-of-Words (BoW)<br>
- Frequency-Inverse Document Frequency (TF-IDF)<br>
- Latent Dirichlet Allocation (LDA)<br>


## Systemanforderungen

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

remove_unwanted_characters(token): Diese Funktion entfernt alle Zeichen aus einem Token, die keine Buchstaben (a-z, A-Z) sind. Sie verwendet einen regulären Ausdruck (regex), um alle nicht alphabetischen Zeichen durch Leerzeichen zu ersetzen.

clean_raw_data(text): Diese Funktion bereinigt einen gegebenen Text durch mehrere Schritte der Textvorverarbeitung:

- Tokenisierung: Der Text wird in einzelne Wörter (Tokens) aufgeteilt.
Entfernen unerwünschter Zeichen: Alle nicht alphabetischen Zeichen werden durch die Funktion remove_unwanted_characters() entfernt.
- Entfernen spezifischer Wörter: Eine Liste von unerwünschten Wörtern (one, like) wird entfernt.
- Stopwörter entfernen: Häufige, nicht informative Wörter (Stopwörter) werden entfernt.
- Punktzeichen entfernen: Alle Satzzeichen werden entfernt.
- Lemmatisierung: Jedes Wort wird in seine Grundform umgewandelt.
- Umwandlung in Kleinbuchstaben: Alle Wörter werden in Kleinbuchstaben umgewandelt, um die Einheitlichkeit zu gewährleisten.

generate_bag_of_words(text_list): Die Funktion erstellt ein Bag-of-Words-Modell, das sowohl Einzelwörter als auch Wortpaare (2-Gramme) berücksichtigt. Sie berechnet die Häufigkeit der Wörter und gibt diese in einem sortierten Wörterbuch zurück. Dies ist eine grundlegende Methode zur Textdarstellung, die für viele Textanalyseaufgaben verwendet wird.

bow_dataframe(word_freq_text): Die Funktion erstellt einen DataFrame aus einem Wörterbuch von Wortfrequenzen und sortiert die Wörter nach ihrer Häufigkeit. Sie gibt die fünf häufigsten Wörter zurück, um die wichtigsten Begriffe aus einem Text zu extrahieren.

tfidf_vectorize_as_single_document(token_lists): Die Funktion berechnet die TF-IDF-Werte für ein zusammengeführtes Dokument, das aus einer Liste von Token-Listen besteht. Die berechneten TF-IDF-Werte werden in einem DataFrame zurückgegeben, der die Gewichtung der Begriffe in Bezug auf ihre Wichtigkeit darstellt.

transform_and_sort_tfidf(tfidf_df): Die Funktion transformiert und sortiert ein DataFrame, das TF-IDF-Werte enthält. Sie transponiert den DataFrame, benennt die Spalten um und sortiert die Begriffe nach ihrer Wichtigkeit in absteigender Reihenfolge der TF-IDF-Werte.

run_lda_analysis(text_list, num_topics): Die Funktion führt eine LDA-Analyse auf einem Textkorpus durch, wobei sie die Themen extrahiert und einen Kohärenzwert berechnet, der die Qualität der erkannten Themen beschreibt. Sie gibt das trainierte LDA-Modell und den Kohärenzwert zurück.

perform_lda(text_list, n_topics=5, n_top_words=10): Die Funktion führt eine LDA-Analyse auf einem gegebenen Textkorpus durch, wobei sie die wichtigsten Wörter für jedes Thema anzeigt. Sie verwendet den TfidfVectorizer, um den Text in eine TF-IDF-Matrix umzuwandeln, und das LDA-Modell, um Themen aus den Textdaten zu extrahieren.

Das Programm verarbeitet die Daten schrittweise, um saubere Texte zu erzeugen, die in der Folge für die Vektorisierung und eine anschließende Themenextraktion verwendet werden.


## Hinweise

Die Berechnungen der Coherence Scores brachten mit Datum 15.12.2024 folgende Ergebnisse:

    # Results from review
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 5) 0.2471651210039798
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 6) 0.2799919362448972
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 7) 0.2910895543971476
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 8) 0.3085074511989887
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 9) 0.29556273834970986

    # Results from summary (took too long on every execution of the program)
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 5) 0.5329306042849031
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 6) 0.5360185919104373
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 7) 0.5505435500322134
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 8) 0.573887214693374
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 9) 0.5465979486599257



