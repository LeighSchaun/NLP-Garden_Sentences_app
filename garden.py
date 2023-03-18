import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The prime number few.",
    "The cotton clothing is usually made of grows in Mississippi.",
    "I convinced her children are noisy."
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence: ", sentence)
    for token in doc:
        print(token.text, " - ", token.pos_, " - ", token.dep_, " - ", spacy.explain(token.dep_))
    print("\n\n")

print(spacy.explain("pcomp"))
print(spacy.explain("ROOT"))

# Explanation for pcomp: 
# prepositional complement, which is a noun, pronoun, or clause that completes the meaning of a preposition

# Explanation for ROOT: root of a sentence is the main verb or predicate that everything else in the sentence modifies or describes. It is always the highest node in the dependency tree.
