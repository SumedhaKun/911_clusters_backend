import spacy
from spacy.tokens import Span
import train_data
import random
from tqdm import tqdm
from spacy.training.example import Example

nlp = spacy.load("en_core_web_sm")
model=None
if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe('ner')
    
for _,annotations in train_data.TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

optimizer = nlp.begin_training()
for itn in range(100):
    random.shuffle(train_data.TRAIN_DATA)
    losses = {}
    for text, annotations in tqdm(train_data.TRAIN_DATA):
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update(
            [example],  
            drop=0.5,  
            sgd=optimizer,
            losses=losses)
    print(losses)

output_dir = "models"
nlp.to_disk(output_dir)
