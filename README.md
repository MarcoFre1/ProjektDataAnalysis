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

remove_unwanted_characters(token): Entfernt unerwünschte Zeichen aus den Token, behält aber Buchstaben und Umlaute.

clean_raw_data(text): Entfernt alle Punkte, Sonderzeichen und Emojis; Entfernt unerwünschte spezifische Wörter; Entfernt Stoppwörter; Führt Lemmatisierung durch; Konvertiert die Wörter in Kleinbuchstaben

generate_bag_of_words(text_list): Daten vorbereiten, erstellen einer Instanz von CountVectorizer, Vektorisierer auf Daten anwenden, ermitteln der Worthäufigkeit.

bow_dataframe(word_freq_text): 

tfidf_vectorize_as_single_document(token_lists): Umwandlung der Token-Listen in Strings und Zusammenführen zu einem einzigen Dokument, Erstellung und Anwendung des TfidfVectorizer und die Umwandlung der TF-IDF-Matrix in einen DataFrame.

transform_and_sort_tfidf(tfidf_df): 

run_lda_analysis(text_list, num_topics): Berechnung des Coherence Scores

perform_lda(text_list, n_topics=5, n_top_words=10): Erstellen und Anwenden des CountVectorizer, erstellen und anwenden der LDA und anzeigen der Top-Wörter für jedes Thema.

Der Code verarbeitet die Daten schrittweise, um "saubere Texte" zu erzeugen, die dann für die Vektorisierung und anschließende Themenextraktion verwendet werden.


## Hinweise

Die Berechnung der Coherence Scores brachten mit Datum 15.12.2024 folgende Ergebnisse:

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



