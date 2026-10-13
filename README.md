# Emotion Detector — Final Project

Project: **Developing AI Applications with Python and Flask — Final Project (Emotion Detector)**

An AI based web application that detects the emotions expressed in written text.
The text is analysed by the **Watson NLP library** (`EmotionPredict` model) and the
application reports the score of every emotion together with the dominant emotion.

## Features

- `emotion_detector(text)` in the `EmotionDetection` package sends the text to the
  Watson NLP EmotionPredict service and returns a dictionary with the scores for
  anger, disgust, fear, joy and sadness plus the `dominant_emotion`.
- Invalid (blank) input is handled through the HTTP status code `400` returned by
  the service: every value becomes `None`, and the web application answers with an
error message instead of a result.
- The results are deployed to the browser through a Flask web application, which
  prints an error message for blank input instead of a result.
- The code is PEP 8 compliant and passes Pylint with a perfect score of `10.00/10`.

## Repository layout

| Path | Description |
| --- | --- |
| `EmotionDetection/__init__.py` | Package initialiser that imports the application module |
| `EmotionDetection/emotion_detection.py` | Application function `emotion_detector()` using the Watson NLP library |
| `server.py` | Flask server that deploys the application (`/` and `/emotionDetector`) |
| `templates/index.html` | Interface of the application |
| `static/mywebscript.js` | Client side script that calls `/emotionDetector` |
| `test_emotion_detection.py` | Unit tests for the five emotions |
| `requirements.txt` | Python dependencies of the project |

## Installation

```bash
python -m pip install -r requirements.txt
```

## Usage

Import the package and call the application function:

```python
from EmotionDetection.emotion_detection import emotion_detector

emotion_detector("I love this new technology")
```

```python
{
    'anger': 0.01001,
    'disgust': 0.005005,
    'fear': 0.004004,
    'joy': 0.970971,
    'sadness': 0.01001,
    'dominant_emotion': 'joy'
}
```

A blank statement returns `None` for every emotion, which means the text was
invalid and could not be analysed.

## Web deployment

```bash
python server.py
```

Open <http://localhost:5000/>, type a sentence and press **Run Sentiment Analysis**.
The application answers with, for example:

> For the given statement, the system response is anger: 0.01001, disgust: 0.005005,
> fear: 0.004004, joy: 0.970971 and sadness: 0.01001. The dominant emotion is **joy**.

Blank input shows: `Invalid input! Try again.`

## Unit tests

```bash
python -m unittest -v test_emotion_detection.py
```

## Static code analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

## License

Apache License 2.0 — see [LICENSE](LICENSE).
