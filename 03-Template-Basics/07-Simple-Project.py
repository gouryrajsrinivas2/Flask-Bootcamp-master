# Set up your imports and your flask app.
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    # This home page should have the form.
    return render_template('exercise_home_page.html')


# This page will be the page after the form
@app.route('/report')
def report():
    username=request.args.get('first')
    uppercase=False
    lowercase=False
    lastdigit=False

    uppercase=any(c.isupper() for c in username)
    lowercase=any(c.islower() for c in username)
    lastdigit=username[-1:].isdigit()

    return render_template('exercise_feedback_page.html',uppercase=uppercase,lowercase=lowercase,lastdigit=lastdigit)
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
