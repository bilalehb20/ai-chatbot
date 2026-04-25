# Mini AI Chatbot (Python)

Een eenvoudig maar professioneel mini-project dat laat zien hoe basis AI-concepten in Python toegepast kunnen worden.

## Doel van het project

Het doel is om een werkende chatbot te bouwen met een **intelligente component**:
rule-based intentherkenning. De bot analyseert gebruikersinvoer en kiest automatisch een passende reactie.

Dit project is ontworpen als schoolportfolio-bewijs van praktische AI-toepassing.

## Hoe werkt het?

De chatbot gebruikt simpele NLP-logica:

1. Gebruikersinvoer wordt genormaliseerd (lowercase + opschonen van spaties).
2. De tekst wordt geclassificeerd naar een intent (bijv. begroeting, tijd, datum, help, afsluiten).
3. Op basis van de intent geeft de bot een passende reactie terug.

Hoewel dit geen zwaar machine-learning model is, toont het wel een kern-idee van AI:
**input interpreteren en beslissen op basis van logica**.

## Gebruikte technologieen

- Python 3
- Rule-based AI / intent classification
- Basis error handling (lege input, veilige afsluiting met Ctrl+C)

## Projectstructuur

- `main.py` - hoofdprogramma met chatbotlogica
- `README.md` - projectuitleg
- `requirements.txt` - dependencies (geen externe pakketten nodig)

## Installatie en uitvoeren

1. Zorg dat Python 3 geinstalleerd is.
2. Open een terminal in de projectmap.
3. (Optioneel) Installeer dependencies:

```bash
pip install -r requirements.txt
```

4. Start de chatbot:

```bash
python main.py
```

## Voorbeeldinputs

- `hallo`
- `hoe laat is het?`
- `welke datum is het vandaag?`
- `wie ben je?`
- `help`
- `stop`

## Wat heb ik geleerd? (reflectie)

Met dit project heb ik geleerd hoe je:

- gebruikersinput structureert en verwerkt;
- AI-achtig gedrag bouwt met intentherkenning;
- nette, leesbare Python-code schrijft met functies;
- een project professioneel documenteert voor GitHub/portfolio.

## Mogelijke uitbreidingen

- Meer intents toevoegen (weer, rekenen, FAQ).
- Logging van gesprekken naar een bestand.
- Integratie met een echte AI API (bijv. OpenAI) voor geavanceerdere antwoorden.
