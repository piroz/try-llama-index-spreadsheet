# try-llama-index-spreadsheet
data input from google spreadsheet to llama_index

You need to issue an [OAuth client ID](https://developers.google.com/fit/android/get-api-key?hl=ja#:~:text=Android%20OAuth%20client%20IDs%20are%20linked%20to%20specific,modify%20a%20project%20in%20the%20Google%20API%20Console.) in your Google Cloud Platform project and save it in credential.json 

You need [OPENAI API KEY](https://platform.openai.com/account/api-keys)

# example

This example creates index from [Google Sheet](https://docs.google.com/spreadsheets/d/1NM7l4LyisJQ4lx7kQZBqs9us4faDBeseSJDVKuzszlU/edit#gid=0) and execute bot.

The spreadsheet_id in this sheet is the URL segment marked below.

ttps://docs.google.com/spreadsheets/d/`1NM7l4LyisJQ4lx7kQZBqs9us4faDBeseSJDVKuzszlU`/edit#gid=0

Specify the spreadsheet_id as the bot launch argument as shown below.

```bash
$ pipenv sync
$ env OPENAI_API_KEY=xxxxxx python bot.py 1NM7l4LyisJQ4lx7kQZBqs9us4faDBeseSJDVKuzszlU
INFO:googleapiclient.discovery_cache:file_cache is only supported with oauth2client<4.0.0
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total LLM token usage: 0 tokens
INFO:llama_index.token_counter.token_counter:> [build_index_from_nodes] Total embedding token usage: 0 tokens
聞きたいことを教えてください。
>>>家はどこですか ？
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 211 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 0 tokens

家は海の中にあります。

聞きたいことを教えてください。
>>>昨年末はどうしていました？
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 226 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 0 tokens

昨年末は海外旅行をしました。

聞きたいことを教えてください。
>>>朝食はたべましたか？
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 216 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 0 tokens

はい、朝食をたべました。

聞きたいことを教えてください。
>>>何をたべました？
INFO:llama_index.token_counter.token_counter:> [query] Total LLM token usage: 210 tokens
INFO:llama_index.token_counter.token_counter:> [query] Total embedding token usage: 0 tokens

チキン南蛮でした。

聞きたいことを教えてください。
```

