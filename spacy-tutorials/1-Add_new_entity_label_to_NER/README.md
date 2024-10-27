# #1 Add a new entity label to NER

## 📖 Description 📖

Jupyter Notebook example on how to add a new entity label to spaCy's default NER model.

<br>

## 🧠 Learning goals 🧠

- **Enhancing spaCy’s default NER model:** We will focus on customizing spaCy's default Named Entity Recognition (i.e., NER) model to recognize specific entities by adding a custom entity label, *COMMODITY*, to spaCy's NER model. This customization will be applied to a text file containing web-scraped data where entities like gold and silver are mentioned in both financial contexts (e.g., gold as a commodity) and non-financial contexts (e.g., gold as an Olympic medal). Our goal is to tweak the NER model to accurately identify entities only in financial contexts.

- **Refining NER model for better accuracy:** We will improve the accuracy of the NER model by addressing key issues:

    - False positives: Reducing cases where the NER model incorrectly identifies entities in the wrong (i.e., non-financial) context.
    - False negatives: Finding cases where the NER model misses entities that are in the right (i.e., financial) context.
    - Incorporating aliases: Adding patterns for aliases (e.g., *XAU/USD* for gold) to ensure that additional relevant articles are captured.

- **Evaluating and improving results:** We will analyze the outcomes of our refined NER approach, assessing how the custom patterns and aliases contribute to the improved detection of relevant financial articles.

<br>

## 🚀 Getting started 🚀

See the <a href="https://github.com/rokbenko/ai-playground/blob/main/spacy-tutorials/1-Add_new_entity_label_to_NER/new_entity_label.ipynb">`new_entity_label.ipynb`</a> file with comments.

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Jupyter Notebook](https://jupyter.org/) `7.1.0`
- [spaCy Python SDK](https://pypi.org/project/spacy/) `3.7.4`
