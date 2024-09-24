from flask import Flask, request, render_template
import pickle

# Load your model
model = pickle.load(open('flood.pkl', 'rb'))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract and convert the input data
    jan = float(request.form['jan'])
    feb = float(request.form['feb'])
    mar = float(request.form['mar'])
    apr = float(request.form['apr'])
    may = float(request.form['may'])
    jun = float(request.form['jun'])
    jul = float(request.form['jul'])
    aug = float(request.form['aug'])
    sep = float(request.form['sep'])
    oct = float(request.form['oct'])
    nov = float(request.form['nov'])
    dec = float(request.form['dec'])
    annual = float(request.form['annual'])


    # Prepare the input for the model
    x = [[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec,annual]]
    
    # Make a prediction
    y = model.predict(x)[0]
    
    # Render the prediction result
    return render_template('predict.html', Prediction=y)

if __name__ == '__main__':
    app.run(debug=True)
