from app import simple_chatbot


def test_total_revenue_query():
    # Define input
    user_input = "What is the total revenue?" 
    # call the function
    response = simple_chatbot(user_input)
    # check if the response contains expected data
    assert "Total Revenue was $416,161M for Apple" in response
    assert "$281,724M for Microsoft" in response
    assert "$94,827M for Tesla" in response


def test_net_income_query():
    response = simple_chatbot("How has net income changed over the last year?")
    assert "Apple had the highest net income growth at 19.49%" in response

def test_unsupported_query_returns_error_message():
    # Test how the bot handles unexpected questions
    response = simple_chatbot("What is the weather in London?")
    assert response == "Sorry, I can only provide information on predefined queries."