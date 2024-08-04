# Named Entity Recognition (NER) Comparison Project

This project compares named entity recognition (NER) techniques using SpaCy and NLTK. It fetches a contemporary news article from the News API, extracts named entities using both rule-based (NLTK) and machine learning-based (SpaCy) approaches, and generates a PDF report comparing the results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ner-comparison.git
    cd ner-comparison
    ```

2. Install the required Python libraries:
    ```bash
    pip install spacy nltk requests fpdf
    ```

3. Download the SpaCy model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Obtain an API key from [News API](https://newsapi.org/) and replace `your_api_key` in the script with your actual API key.

2. Run the script:
    ```bash
    python api.py
    ```

3. The script will fetch a news article, extract named entities using both NLTK and SpaCy, compare the results, and generate a PDF report named `ner_comparison_report.pdf`.

## Output

The output PDF report contains:
- The fetched news article.
- Entities extracted by NLTK.
- Entities extracted by SpaCy.
- Comparison of entities, including common entities and entities unique to each method.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
