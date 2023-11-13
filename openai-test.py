from openai import OpenAI
import openai
client = OpenAI()





def translate_nodejs_to_python(nodejs_code):
   try:
        response = openai.completions.create(
            model="text-davinci-003",  # Assuming this is the latest model as of April 2023
            prompt=f"Convert the following Node.js code to Python:\n\n{nodejs_code}",
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].text.strip()
   except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
nodejs_code_example = """
// Node.js code example
const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(8080);
"""

translated_python_code = translate_nodejs_to_python(nodejs_code_example)
if translated_python_code:
    print("Converted Python Code:\n", translated_python_code)
else:
    print("Translation failed.")

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