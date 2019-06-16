from __future__ import print_function
from keras.models import Sequential
from keras import layers
import numpy as np
from keras.models import load_model
from six.moves import range


class CharacterTable(object):
    """Given a set of characters:
    + Encode them to a one-hot integer representation
    + Decode the one-hot or integer representation to their character output
    + Decode a vector of probabilities to their character output
    """
    def __init__(self, chars):
        """Initialize character table.
        # Arguments
            chars: Characters that can appear in the input.
        """
        self.chars = sorted(set(chars))
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

    def encode(self, C, num_rows):
        """One-hot encode given string C.
        # Arguments
            C: string, to be encoded.
            num_rows: Number of rows in the returned one-hot encoding. This is
                used to keep the # of rows for each data the same.
        """
        x = np.zeros((num_rows, len(self.chars)))
        for i, c in enumerate(C):
            x[i, self.char_indices[c]] = 1
        return x

    def decode(self, x, calc_argmax=True):
        """Decode the given vector or 2D array to their character output.
        # Arguments
            x: A vector or a 2D array of probabilities or one-hot representations;
                or a vector of character indices (used with `calc_argmax=False`).
            calc_argmax: Whether to find the character index with maximum
                probability, defaults to `True`.
        """
        '''
        if calc_argmax:
            x = x.argmax(axis=-1)
        '''
        return ''.join(self.indices_char[x] for x in x)


class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'

chars = '0123456789+ '
ctable = CharacterTable(chars)
DIGITS = 3
def test(x1, x2):
    q = '{}+{}'.format(x1, x2)
    q = q + ' '*(2*DIGITS+1-len(q))
    x = np.zeros((1, 2*DIGITS+1, len(chars)), dtype=np.bool)
    x[0] = ctable.encode(q, 2*DIGITS+1)
    model = load_model('addition_model.h5')
    correct = str(x1 + x2)
    correct += ' '*(DIGITS+1-len(correct))
    preds = model.predict(x)
    print(preds.shape)
    preds = np.argmax(preds, axis=-1)
    print(preds.shape)
    guess = ctable.decode(preds[0], calc_argmax=False)
    print('Q', q, end=' ')
    print('T', correct, end=' ')
    if correct == guess:
        print(colors.ok + '☑' + colors.close, end=' ')
    else:
        print(colors.fail + '☒' + colors.close, end=' ')
    print(guess)
    return guess
test(123,232)