"""
Andrea Russo AR23110010747
T19 Practical Task 1

"""

# Import relevant modules and load en_core_web_sm
import spacy
npl = spacy.load('en_core_web_sm')


# Create list with garden-path sentences
gardenpathSentences = ["Time flies like an arrow, fruit flies like a banana.", 
                       "Before the trial, the lawyer, who studied in Harvard, consulted Paris experts.", 
                       "Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.", 
                       "The cotton clothing is made of grows in Mississippi."]


# For each sentence, print the tokenized version. 
# Then, perform entity recognition.
for sentence in gardenpathSentences:
    doc = npl(sentence)
    print([(token, token.orth_, token.orth) for token in doc])
    print([(entity, entity.label_, entity.label) for entity in doc.ents])

# Use spaCy inbuild explain method to print meanings of 'ORG' and 'GPE'
print(spacy.explain('ORG'))
print(spacy.explain('GPE'))

"""
ORG:
    The enityt was 'ORG', which spacy.explains returns as 'Companies, agencies, institutions, etc.'. 
    This made sense as the entity was Harvard, which is indeed an insitution.
    
GPE:
    The enityt was 'GPE', which spacy.explains returns as 'Countries, cities, states'. 
    This made sense as the entitites were Paris and Mississipi, which are a city and a state.
"""
