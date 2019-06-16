from keras.models import Model
from keras.layers import Input, LSTM, Dense


# define an input sequence and process it
encoder_inputs = Input(shape=(None, num_encoder_tokens))
model = Model(inputs=[], outputs=[])