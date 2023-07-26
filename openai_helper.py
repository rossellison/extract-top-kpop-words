import openai
import os
openai_key = os.getenv('OPENAI_API_KEY')
import json
import pandas as pd

openai.api_key = openai_key

def extract_kpop_data(text):
    prompt = get_prompt_kpop() + text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user","content": prompt}]
    )
    content = response.choices[0]['message']['content']

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Measure", "Value"])

    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Word": ["", "", "", "", ""],
        "Count": ["", "", "", "", ""]
    })



def get_prompt_kpop():
    return '''Here is the list of the top 25 most common Korean words in Kpop: 내, 난, 널, 더, 나, 넌, 수, 너, 다, 그, 이, 날, 내가, 나는, 몰라, 나를, 너의, 또, 너를, 왜, 없어, 내게, 네, 너무, 걸, 니, 해, 니가, 봐, 우리, 나의, 다시, 네가, 한, 혼자, 알고, 그게, 모습, 밤이. 
    I want you to count how many times each of the top 25 most common Korean words in Kpop are used in the following Kpop lyrics.
    Return your response as a valid JSON string of the top 5 most frequently occuring Korean words that also appeared in the top 25 most common Korean words in Kpop.
    The format should be this,
    {
        "나": "32",
        "너의": "23",
        "한": "14",
        "우리": "12",
        "다시": "11"
    }
    Kpop Lyrics:
    ============
    '''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = '''
    The most common words in Kpop in your lyrics
    '''
    df = extract_kpop_data(text)

    print(df.to_string())
