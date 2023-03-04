from sentence_transformers import SentenceTransformer, models
import numpy as np


def encode_sentences(sentences, pretrain_name):
    """

    Parameters
    ----------
    sentences
    pretrain_name

    Returns
    -------

    """
    model = SentenceTransformer(pretrain_name)
    # Sentences are encoded by calling model.encode()
    embeddings = model.encode(sentences).flatten()
    return sentences, embeddings


def compare(ground_truth, predictions):
    """

    Parameters
    ----------
    ground_truth
    predictions

    Returns
    -------

    """
    return np.all(np.isclose(ground_truth, predictions, atol=1e-07))


if __name__ == "__main__":
    sentences, embeddings = encode_sentences("i am a hero", "all-MiniLM-L6-v2")
    ground_truth = np.random.random(embeddings.shape)
    print(np.isclose(ground_truth, embeddings, atol=1e-07))
