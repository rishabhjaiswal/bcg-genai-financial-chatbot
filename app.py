from flask import Flask, request

app = Flask(__name__)

def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
       return "In 2025, Total Revenue was $416,161M for Apple, $281,724M for Microsoft, and $94,827M for Tesla."
    elif user_query == "How has net income changed over the last year?":
       return "From 2024 to 2025, Apple had the highest net income growth at 19.49%, while Microsoft grew by 15.53%. Conversely, Tesla's net income significantly decreased by 46.10%."
   # Add more conditions for other predefined queries
    elif user_query == "Is there any relation in the data in Total Revenue and Total Liabilities?":
        return "Microsoft and Tesla both showed an increasing trend in Total Liabilities, but while Microsoft paired this with strong revenue growth, Tesla showed negative revenue growth in 2025. Apple, on the other hand, showed increasing revenue growth over the period while reducing its Total Liabilities in 2025."
    elif user_query == "How has Cash Flow changed over 2023-2025?":
        return "Only Microsoft maintained a positive percentage increase in Cash Flow for both years over the 2023-2025 period. Both Apple and Tesla saw their Cash Flow growth turn negative in 2025."
    elif user_query == "Has Total Assets increased or decreased?":
        return "Microsoft and Tesla both had positive percentage increases in Total Assets over the 2023-2025 period. However, Apple experienced a decrease in Total Assets in 2025 compared to 2024."
    else:
       return "Sorry, I can only provide information on predefined queries."
   

@app.route("/query")
def user_query():
    question = request.args.get("question", "Flask")
    res = simple_chatbot(question)
    return res
