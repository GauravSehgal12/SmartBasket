from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the rules dataframe
rules = pd.read_pickle('rules.pkl')

# Debug prints to check rules data and types
print("Sample rules:")
print(rules.head())
print("Types:", type(rules.iloc[0]['antecedents']), type(list(rules.iloc[0]['antecedents'])[0]))

def recommend_items(input_item, rules_df):
    input_item = input_item.lower()
    recommendations = set()

    for _, row in rules_df.iterrows():
        antecedents = list(row['antecedents'])
        antecedents = [str(i).lower() for i in antecedents]

        if input_item in antecedents:
            consequents = list(row['consequents'])
            consequents = [str(i).lower() for i in consequents]
            recommendations.update(consequents)
            print(f"MATCH FOUND: {antecedents} => {consequents}")  # Debug print

    return list(recommendations)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        item = request.form['item'].lower()
        recommendations = recommend_items(item, rules)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
