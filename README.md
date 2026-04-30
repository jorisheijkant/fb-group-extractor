# Samenvatten van Facebook-groepen
In deze _repository_ staat code om van de html van Facebook-groep (wekelijkse) samenvattingen te maken. 

Deze code is geschreven in het kader van een AI-cursus van het [Fonds Bijzondere Journalistieke Projecten](https://fondsbjp.nl/).

## Benodigdheden
Voor dit script heb je een moderne versie van Python nodig en wat libraries, zie `requirements.txt`. Die kun je in één keer installeren via het commando `pip install -r requirements.txt`. Gebruik bij voorkeur een virtuele omgeving als venv of Conda.

De samenvattingen kun je maken met lokale modellen via [Ollama](https://ollama.com/) of via een cloud provider als Anthropic. In het laatste geval, voeg ook een API key toe in de `.env` (zie `.env.example`). 

## Stappenplan
- Open de FB-groep in je browser. Scroll naar beneden, eventueel geautomatiseerd met [Foxscroller](https://addons.mozilla.org/en-US/firefox/addon/foxscroller/). 
- Check of alle posts geladen zijn als html door de console te openen. Draai dan het volgende commando in de JS-console:
```
document.querySelectorAll('div').forEach(div => {
  if (div.textContent.trim() === 'Meer weergeven') {
    div.click();
  }
});
```
- Sla de pagina op als html-bestand (Ctrl+S of Cmd+S). Zet het in de `html/`-map. Let op: commit dit bestand niet naar Github, het is groot. Maar het staat standaard al in de `.gitignore` als je het in die map zet.
- Draai `extract_posts_from_html.py` (pas de paden naar je bestanden aan indien nodig) om de posts op te slaan in een csv-bestand. 
- Draai `make_summary.py` om een samenvatting te maken van de posts.

### TODO
- Datum van posts uitlezen zodat we wekelijkse samenvattingen kunnen maken, in plaats van een samenvatting van alle posts. 
- Een uniek id toevoegen aan elke post.
