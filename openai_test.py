import openai
import asyncio

openai.api_key = '<YOUR API KEY HERE>'

messages = [
    {
        "role": "system",
        "content": "Instructions:\n1. Generate 2 quiz questions based on the provided text.\n2. Each question should be paraphrased and derived directly from the text.\n3. Ensure a roughly equal distribution of 'True' and 'False' correct answers.\n4. For multiple-choice questions, provide three false options and one correct option, with the correct answer randomly positioned in the list.\n\nExample format:\ncontent: What is one advantage of using a dehumidifier?; type: 'multiple'; options: 'Reduces the chance of electronics getting damaged'|'Helps keep humidity high to prevent mold and mildew'|'Makes your home smell better'|'Attracts insects to your home'; correct_answer: 'Reduces the chance of electronics getting damaged'\n\ncontent: A dehumidifier is not necessary if you live in a dry climate.; type: 'boolean'; options: 'True|False'; correct_answer: 'True'\n\nPlease generate 15 quiz questions adhering to the provided instructions."
    },
    {
        "role": "user",
        "content": "Set Up a Dehumidifier.Setting up a dehumidifier is something that you might not think about until you need to get it working in your home. But, a dehumidifier can save you money in the long run. If you have a lot of electronics in your home, you might want to consider setting one up. It reduces the chance of your electronics getting damaged because of moisture. It also helps keep humidity down in your home so that mold and mildew won't develop...Call for service.Hiring a professional to install a dehumidifier can be a bit more expensive than doing it yourself. But, if you have to call for service, make sure to call a professional. The first thing they'll ask is if your home is wood framed. If you're not sure, you should call a professional to check it out before you decide on a dehumidifier for your home.. ..Decide on the best dehumidifier for your home.There are a lot of different products to choose from. Some are meant for small rooms while others are meant for a large room. There are also models that are meant for the winter months and summer months. If you're not sure, you should contact a professional to help you with this decision.. ..Install the dehumidifier.You should always hire a professional to install the dehumidifier in your home. There are safety hazards associated with trying to install a dehumidifier.. ..Test the dehumidifier.Make sure to test the dehumidifier daily. If you don't test it, you'll be wasting money. You should also test it before you start using it, and check the settings to make sure they're correct.. ..Check the warranty.A dehumidifier doesn't last forever. Make sure to check the warranty information before you buy one. If you don't, you'll be spending money without knowing it..Clean the dehumidifier.You need to clean the dehumidifier every few weeks. If you don't, it won't work as well as it should.."
    },
    {
        "role": "assistant",
        "content": "Understood. I'll provide 2 quiz questions (random order) based on the text given. Each question should be either multiple choice or true/false, and should contain the following information:\n- content: The question\n- type: 'multiple' or 'boolean'\n- options: In a multiple choice question, we should give the users 4 answers: 3 false and 1 correct. The correct answer should be randomly positioned in the list. True/False for boolean question type questions.\n- correct_answer: One of the 4 correct answers or True/False for boolean question type. Ensure that there's a balance of 'True' and 'False' correct answers\n\nDesired format:\ncontent: <content string>; type: 'multiple';'options': '<optionX>|<optionX>|<optionX>|<optionX>'; correct_answer: '<optionX>'\n\ncontent: <content string>; type: 'boolean';'options': 'True|False'; correct_answer: 'True|False'"
    }
]


print('Generating questions. This might take a minute...')
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0,
    messages=messages,
)

print(response['choices'][0]['message']['content'])
