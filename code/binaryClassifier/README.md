binary classifier classifies whether an image contains keyboard typing or not

- `binaryClassifier.py` trains a classifier based on the data specified under `/data/` folder

- `labelPredictor.py` uses the trained classifier (output of `binaryClassifier.py`) to predict whether an image has keyboard typing or not

- `cropImage.py` crops keyboard part (bottom part) of the entire screenshot for better accuracy

- `typingLocator.py` adds the results of whether the touch indicator is on the keyboard (`in`) or not (`out`) to the `typing_result.csv` file