# General Import
import pandas as pd
from spacy.language import Language

def lemmatize_text(ser: pd.Series,nlp: Language)-> pd.Series:
        """Lemmatizes the text"""
        texts = ser.to_list()
        clean_texts = []
        for doc in nlp.pipe(texts,batch_size = 1):
            tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
            clean_texts.append(' '.join(tokens))
        return pd.Series(clean_texts)

def preprocess_input_data(input_dict:dict,nlp: Language)-> pd.DataFrame:
    """Preprocesses the input data"""
    input_df = pd.DataFrame(input_dict,index=[0])
    return (
         input_df
                .assign(
                    text = lambda df:df.text
                                        .pipe(lemmatize_text,nlp = nlp)     
                )
    )

    