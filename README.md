Garden Path Sentences Analysis
This project uses the Spacy library to analyze five garden path sentences. Garden path sentences are sentences that are difficult to parse, which can lead to readers misinterpreting their meaning.

Installation
To run this project, you will need to install Spacy. You can install Spacy using pip:

Copy code
pip install spacy
You will also need to download the en_core_web_sm model by running the following command:

Copy code
python -m spacy download en_core_web_sm
Usage
To analyze the garden path sentences, simply run the garden_path_sentences.py script. This script contains a list of five garden path sentences, and will use Spacy to analyze the structure of each sentence and identify difficult-to-parse constructions.

The script will output information about each token in the sentence, including the token's text, part of speech tag, dependency relation, and an explanation of the dependency relation. The script will also provide explanations for the pcomp and ROOT dependency relations.

Garden Path Sentences
The following are the five garden path sentences that will be analyzed by this project:

markdown
Copy code
1. The old man the boat.
2. The complex houses married and single soldiers and their families.
3. The prime number few.
4. The cotton clothing is usually made of grows in Mississippi.
5. I convinced her children are noisy.
License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.