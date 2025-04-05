from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import markdown 


load_dotenv()


app = Flask(__name__)

client = OpenAI()  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    motion = request.form['motion']
    format = request.form['format']
    include_readings = 'include_readings' in request.form
    include_video = 'include_video' in request.form

    prompt = f"""
    You are a very experienced debater and a professional debate coach specializing in {format} format.

    Analyze the following motion: \"{motion}\"

    Return:
    - 3 categories the motion belongs to.
    - The difficulty (easy/medium/hard). 
    - Three detailed Government arguments. Write 7 sentences per argument, explaining in great detail why it is true and viable. 
    - Three detailed Opposition arguments. Write 7 sentences per argument, explaining in great detail why it is true and viable. 
    """
    if include_readings:
        prompt += "\n- Suggest 3 relevant readings (articles, papers, or books). Include titles and links if possible."
    if include_video:
        prompt += "\n- Share a link to a YouTube debate round relevant to the motion's category, preferably from WSDC, EUDC, WUDC, or Australian debate recordings."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        html_result = markdown.markdown(result)


    except Exception as e:
        result = f"❌ Error from OpenAI: {str(e)}"

    return render_template('result.html',
                           motion=motion,
                           result_html=html_result)


if __name__ == '__main__':
    app.run(debug=True)
