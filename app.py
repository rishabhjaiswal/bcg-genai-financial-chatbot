import streamlit as st

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
   

st.title("Financial Analysis Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on appm rerun
    
for message in st.session_state.messages:
    with st.chat_message(message['key']): 
        st.markdown(message['value'])


if prompt := st.chat_input("Please ask your financial query."):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({'key': "user", 'value': prompt})


# Display assistant response in chat message container
if prompt:  
    with st.chat_message("assistant"):
        response = simple_chatbot(prompt)
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"key": "assistant", "value": response})
    

