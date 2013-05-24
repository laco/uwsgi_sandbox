from flask import Flask
import nltk.data

app = Flask(__name__)
#classifier = nltk.data.load("classifiers/NAME_OF_CLASSIFIER.pickle")
class Classifier(object):
    def classify(self, data):
        return data

classifier = Classifier()

@app.route('/')
def hello_world():
    words = ['some', 'words', 'in', 'a', 'sentence']
    feats = dict([(word, True) for word in words])
    return repr(classifier.classify(feats))

    # return """Hello World2!
# ide meg valami
# """

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0')

