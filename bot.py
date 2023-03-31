import os
from fire import Fire
from llama_index import GPTListIndex, download_loader

def main(spreadsheet_id: str) -> None:

    # OPENAI_API_KEYを環境変数に設定してください。

    index_file = f'index/{spreadsheet_id}.json'

    if not os.path.exists(index_file):
        os.makedirs('index', exist_ok=True)
        GoogleSheetsReader = download_loader('GoogleSheetsReader')
        loader = GoogleSheetsReader()
        documents = loader.load_data(spreadsheet_ids=[spreadsheet_id])
        index = GPTListIndex.from_documents(documents)
        index.save_to_disk(index_file)
    else:
        index = GPTListIndex.load_from_disk(
            index_file
        )
    while True:
        inp = input("聞きたいことを教えてください。\n>>>")
        print(index.query("日本語で答えてください。" + inp))
        print()

Fire(main)
