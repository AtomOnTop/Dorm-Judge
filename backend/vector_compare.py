# NumPy is a library for fast math on arrays/vectors.

import numpy as np



def compare_vector(vector, predefined_matrix):
    """
    vector: 1D numpy array (shape: r)
    predefined_matrix: 2D numpy array containing all vectors (shape: N x r)
    i.e. N rows, where each row is one vector of length r

    
    """
    # If the matrix has no elements, there is nothing to compare against.
    # Return "no best match" (None) and an empty ranked list.
    if predefined_matrix.size == 0:
        return None, []

    # --- Step 1: dot products -------------------------------------------
    # "@" is matrix multiplication.
    
    dot_products = predefined_matrix @ vector

    # --- Step 2: lengths (norms) ----------------------------------------
    # Length of the single input vector -> one number.
    norm_vector = np.linalg.norm(vector)
    # Length of EVERY row of the matrix -> N numbers.
    # axis=1 means "calculate along each row" (axis=0 would be down columns).
    norms_matrix = np.linalg.norm(predefined_matrix, axis=1)

    # --- Step 3: cosine similarity for all rows at once -----------------
    # Bottom part of the formula for each row:
    # (length of input vector) * (length of that row)  -> N numbers
    denominators = norm_vector * norms_matrix

    # Safe division, element by element: dot_products / denominators
    #   where=denominators != 0   -> only divide where the denominator is not 0
    #   out=np.zeros_like(...)    -> start with an array of zeros; any position
    #                                we skip (because of division by zero)

    similarities = np.divide(
        dot_products,
        denominators,
        out=np.zeros_like(dot_products),
        where=denominators != 0,
    )

    # --- Step 4: rank from best to worst --------------------------------
    # np.argsort gives the POSITIONS (indices) that would sort the array
    # from lowest to highest.
    # [::-1] reverses that, so it becomes highest to lowest.

    ranked_indices = np.argsort(similarities)[::-1]

    # List comprehension (a compact for-loop) that builds a list of
    # (vector, score) pairs, in ranked order from best to worst.

    ranked_pairs = [(predefined_matrix[i], similarities[i]) for i in ranked_indices]

    # Return two things:
    #   1. the best matching vector (first in the ranking)
    #   2. the full ranked list of (vector, score) pairs
    return predefined_matrix[ranked_indices[0]], ranked_pairs


