from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-fOFIG": {
    "files": "",
    "input_value": "Artificial intelligence (AI), a field that aims to create intelligent agents capable of reasoning, learning, and problem-solving, has a rich and fascinating history. While the concept of intelligent machines dates back to ancient myths and folklore, the modern era of AI began in the mid-20th century. One of the earliest pioneers of AI was Alan Turing, a British mathematician and computer scientist. In his 1950 paper \"Computing Machinery and Intelligence,\" Turing proposed the \"Turing test\" as a way to determine whether a machine could exhibit intelligent behavior indistinguishable from that of a human.   In the 1950s and 1960s, AI researchers made significant strides in developing programs that could solve mathematical problems, play games like chess and checkers, and even understand natural language to a limited extent. However, these early successes were followed by a period of disillusionment known as the \"AI winter\" in the 1970s. During this time, funding for AI research dried up as expectations were not met. In the 1980s, AI experienced a resurgence with the development of expert systems, which could mimic the decision-making abilities of human experts in specific domains. These systems were used in fields such as medicine, finance, and engineering. However, they were often limited in their ability to handle unexpected situations or to learn from new information. The 1990s and early 2000s saw a shift toward statistical machine learning techniques, which allowed AI systems to learn from large datasets. This approach led to significant advances in areas such as computer vision, natural language processing, and speech recognition. Today, AI is everywhere, from the recommendation algorithms that suggest products on online shopping sites to the self-driving cars being developed by major technology companies. As AI continues to evolve, it is likely to have a profound impact on society in the years to come",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True
  },
  "Prompt-qu27u": {
    "template": "\"Summarize the following text into a concise format. The summary should address all major domains of human life including personal life, relationships, health, work, education, finance, social activities, and personal growth. Ensure the summary is clear and covers key points without unnecessary detail.\"\n\nThis prompt ensures that every time you ask for a summary it will focus on the essential aspects across various life domains and will examine the text input.\n\nWhenever you request a summary, the bot will use this approach to provide a summary that comprehensively addresses the significant areas of human life.\"Ahoy, me hearties! Can ye condense this text into a pirate's message in a bottle? Keep it short and sweet, like a pirate's treasure map. Focus on the main points, and leave the unnecessary details behind. Arrr!\"\n\nUser: {user_input}\n\nAnswer: ",
    "user_input": ""
  },
  "ChatOutput-pqUov": {
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True
  },
  "OpenAIModel-N19PX": {
    "api_key": "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",
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o-mini",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  }
}

result = run_flow_from_json(flow="Basic Prompting (Hello, World).json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
