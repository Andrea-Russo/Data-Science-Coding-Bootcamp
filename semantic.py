"""
Andrea Russo AR23110010747
T20 Practical Task 1

"""

#%% Import necessary libraries
import spacy

#%% Execute code snippet 1 

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#%% Execute code snippet 2 
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#%% Code snippet 3

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity}")
    #print(sentence + "-" + similarity)
    
#%% Note on results and example    
"""
When comparing semantic similarities, we notice how the language model associates 
a higher similarity between monkey and banana (0.4) with respect that cat and banana (0.22). 
It appear that the model is able to draw upone the relation between monekys and bananas.
However, this relation is not transitive. While cat and monkey are quite similar (0.0.6),
the similarity between can and banana is quite low, meaning it does not carry over form
the similarity of cat and monkey.

An example where the same effect can be seen is "car-pilot-plane". 
While car and plane have similarity coefficient of 0.46, and plane and pilo of 0.47,
the word car and the word pilot have only a similarity of 0.23, 
showing once again that the similarity is not transitive.
"""

tokens_task = nlp('car pilot plane ')

for token1 in tokens_task:
    for token2 in tokens_task:
        print(token1.text, token2.text, token1.similarity(token2))
        
#%% Note on runnuing semanticsimilarity_example using en_core_web_sm

"""
Running the semanticsimilarity_example with 

"The model you're using has no word vectors loaded, so the result of the Doc.similarity
method will be based on the tagger, parser and NER, which may not give 
useful similarity judgements. This may happen if you're using one of the 
small models, e.g. `en_core_web_sm`, which don't ship with word vectors and 
only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available."

The reason why this message is displayied is understood by first recalling what
a word vector is:
Word vectors are numerical representations of words, capturing their meanings, 
syntactic properties, and relationships with other words. 
These representations are crucial for tasks that require an understanding of 
word similarity and semantic meaning.

The small models in spaCy, like en_core_web_sm, are designed to be lightweight and fast. 
They are optimized for tasks that don't necessarily require a deep understanding of word meanings,
such as tokenization. Because of their design goals, these models do not include pre-trained word vectors.
Instead, they rely on context-sensitive tensors generated from the 
internal states of the model's neural network as it processes text. 
These tensors can capture some semantic relationships based on the training data, 
but they are generally not as rich or accurate as dedicated word vectors 
for measuring word similarity.

When the .similarity() method is used in spaCy to compute the similarity between two documents,
spans, or tokens, the method attempts to use the best available information to make this
calculation. If the model loaded into spaCy includes pre-trained word vectors,
the method will use these vectors to determine similarity, leveraging their large amount of information.
However, if the model does not include word vectors, as with en_core_web_sm, 
spaCy falls back on using the context-sensitive tensors derived from the model's tagger, 
parser, and named entity recognition components.

This fallback can result in less meaningful similarity judgements because 
the tensors are more focused on syntactic functions and entity recognition 
than on capturing nuanced semantic relationships. 
The computed similarity might reflect syntactic or structural similarity 
rather than semantic similarity.
"""

#%% Movies reccomendations

def load_movies(filepath):
    movies = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            title, description = line.strip().split(' :', 1)
            movies[title] = description
    return movies

def recommend_movie(input_description, filepath='movies.txt'):
    movies = load_movies(filepath)
    
    # Process the input description with SpaCy
    input_doc = nlp(input_description)
    
    # Initialize variables to keep track of the most similar movie
    max_similarity = -1
    recommended_movie = None
    
    for title, description in movies.items():
        # Process each movie description with SpaCy
        movie_doc = nlp(description)
        
        # Compute similarity
        similarity = input_doc.similarity(movie_doc)
        
        # Update recommended movie if the current movie is more similar
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = title
    
    return recommended_movie

# Now use to find most similar movie
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = recommend_movie(input_description)
print(f"Recommended Movie: {recommended_movie}")
