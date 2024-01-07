import json

# 读取文件 A，并将其内容转换为 Python 对象
def read_jsonl(file_path):
    conversations = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            conversations.append(json.loads(line))
    return conversations

# 将文件 A 的格式转换为文件 B 的格式
def convert_format(conversations):
    new_format = []
    for conv in conversations:
        new_conversation = {
            "id": f"identity_{conv['conversation_id']}",
            "conversations": []
        }
        for turn in conv['conversation']:
            new_conversation["conversations"].append({
                "from": "user",
                "value": turn["human"]
            })
            new_conversation["conversations"].append({
                "from": "assistant",
                "value": turn["assistant"]
            })
        new_format.append(new_conversation)
    return new_format

# 主执行函数
def main():
    file_a_path = 'data/dummy_data.jsonl'
    file_b_path = 'data/qwen_demo.json'
    
    # 读取并转换
    conversations_a = read_jsonl(file_a_path)
    converted_conversations = convert_format(conversations_a)

    # 写入新格式到文件 B
    with open(file_b_path, 'w', encoding='utf-8') as file:
        json.dump(converted_conversations, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
