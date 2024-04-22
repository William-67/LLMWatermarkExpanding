from datasets import load_dataset
import json
import re

import scipy.stats

def remove_special_characters(text):
    # Delete informal expression
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', text)
    return cleaned_text

def main():
    realnewslike = load_dataset("allenai/c4", "realnewslike", streaming=True)
    dataset = realnewslike["train"]
    count = 0

    with open('c4dataset.txt', 'w') as text_file:
        for example in dataset:
            if count == 50:
                break

            # Serialize example to JSON string
            example_id = count + 1
            example_text = remove_special_characters(example['text'])
            example_text = example_text.replace("\n", " ")
            # print(example_text)

            text_file.write(str(example_id))
            text_file.write("\n")
            text_file.write(example_text)
            text_file.write("\n")

            count +=1


# def read_json_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#     return data

# --------------------------training split
# not watermarked
# watermarked
# adversarial 
    

if __name__ == "__main__":
    # print(scipy.stats.norm.sf(9.81))
    main()
    # json_data = read_json_file("examples.json")
    # for prompt in json_data['prompt']:
    #     print(prompt["text"])