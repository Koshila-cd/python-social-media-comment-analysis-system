import spacy

nlp = spacy.load('en_core_web_sm')


# ner.append(ent.text, ent.start_char, ent.end_char, ent.label_)
def recognition(text):
    doc = nlp(text)
    ner = []
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            ner.append(entity.text.casefold())
    return ner
