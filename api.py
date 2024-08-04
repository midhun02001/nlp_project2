import requests
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
import spacy
from fpdf import FPDF

# Function to fetch news article
def fetch_news_article(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json().get('articles')
    if articles:
        title = articles[0]['title'] or ""
        description = articles[0]['description'] or ""
        return title + ' ' + description
    return None

# Replace 'your_api_key' with your actual News API key
api_key = '5d61127398784ba7a2819236ef4b8620'
news_article = fetch_news_article(api_key)
print(news_article)

# Function to extract entities using NLTK
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_entities_nltk(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    named_entities = ne_chunk(pos_tags)
    return named_entities

nltk_entities = extract_entities_nltk(news_article)
print(nltk_entities)

# Function to extract entities using SpaCy
nlp = spacy.load("en_core_web_sm")

def extract_entities_spacy(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

spacy_entities = extract_entities_spacy(news_article)
print(spacy_entities)

# Function to compare entities
def compare_entities(nltk_entities, spacy_entities):
    nltk_named_entities = set()
    for chunk in nltk_entities:
        if hasattr(chunk, 'label'):
            entity_name = ' '.join(c[0] for c in chunk)
            entity_type = chunk.label()
            nltk_named_entities.add((entity_name, entity_type))

    spacy_named_entities = set(spacy_entities)

    return nltk_named_entities, spacy_named_entities

nltk_named_entities, spacy_named_entities = compare_entities(nltk_entities, spacy_entities)

print("Entities extracted by NLTK:")
print(nltk_named_entities)
print("\nEntities extracted by SpaCy:")
print(spacy_named_entities)

print("\nCommon Entities:")
print(nltk_named_entities & spacy_named_entities)

print("\nEntities unique to NLTK:")
print(nltk_named_entities - spacy_named_entities)

print("\nEntities unique to SpaCy:")
print(spacy_named_entities - nltk_named_entities)

# Function to create PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'NER Comparison Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

pdf = PDFReport()
pdf.add_page()
pdf.chapter_title('News Article')
pdf.chapter_body(news_article)

nltk_entities_text = "\n".join([str(ent) for ent in nltk_entities])
pdf.add_chapter('Entities extracted by NLTK', nltk_entities_text)

spacy_entities_text = "\n".join([str(ent) for ent in spacy_entities])
pdf.add_chapter('Entities extracted by SpaCy', spacy_entities_text)

comparison_text = f"""
Common Entities:
{nltk_named_entities & spacy_named_entities}

Entities unique to NLTK:
{nltk_named_entities - spacy_named_entities}

Entities unique to SpaCy:
{spacy_named_entities - nltk_named_entities}
"""
pdf.add_chapter('Comparison of Entities', comparison_text)

pdf.output('ner_comparison_report.pdf')
