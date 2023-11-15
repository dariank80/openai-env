from flask import Flask, request, render_template
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

def translate_nodejs_to_python(nodejs_code):
    try:
        response = client.chat.completions.create(model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that identifies the language of the given code."},
            {"role": "user", "content": f"Convert the following code to Python:\n\n{nodejs_code}"}
        ])
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nodejs_code = request.form['nodejs_code']
        translated_python_code = translate_nodejs_to_python(nodejs_code)
        return render_template('index.html', python_code=translated_python_code)
    return render_template('index.html', python_code='')

if __name__ == '__main__':
    app.run(debug=True)


# messages = []
# system_msg = input("What type of chatbot would you like to create? ")
# messages.append({"role": "system", "content": system_msg})

# print("Your new assistant is ready")
# while True:
#     user_msg = input("You: ")
#     if user_msg == "quit()":
#         break  # Exit the loop if the user enters 'quit()'

#     messages.append({"role": "user", "content": user_msg})

#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
#     reply = response.choices[0].message.content
#     messages.append({"role": "assistant", "content": reply})
#     print("Assistant:", reply)9



# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)