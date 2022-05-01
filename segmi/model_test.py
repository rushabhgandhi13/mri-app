from utils import *
set_seed(42)

model = load_model()

checkpoint_filepath = './model_checkpoint/'
model.load_weights(checkpoint_filepath)

input = load_volume("image_118.npy")

# outputs a numpy array of shape (128, 128, 128,4)
output = predict(model, input)
# outputs 64th slice of the output of shape (128, 128)
output_slice = argmax_output(output, slice_num=64)
x