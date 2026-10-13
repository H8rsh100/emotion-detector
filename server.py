"""Flask web application that deploys the EmotionDetection package."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyse the text sent by the browser and describe the detected emotions.

    Returns:
        str: the emotion scores and the dominant emotion of the text, or a
        message asking the user to try again when the text is blank.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is "
        f"anger: {response['anger']}, disgust: {response['disgust']}, "
        f"fear: {response['fear']}, joy: {response['joy']} and "
        f"sadness: {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """Render the main page of the application."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
