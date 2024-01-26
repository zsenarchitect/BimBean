#! python3
import opencc # pip install opencc-python-reimplemented

def convert_simplified_to_traditional(simplified_texts):
    # Create an OpenCC converter for Simplified to Traditional conversion
    converter = opencc.OpenCC('s2t')
    
    # Create a dictionary to store the converted texts
    converted_texts = {}

    for simplified_text in simplified_texts:
        # Perform the conversion for each text
        traditional_text = converter.convert(simplified_text)
        
        # Store the result in the dictionary
        converted_texts[simplified_text] = traditional_text

    return converted_texts

# # Example usage:
# simplified_texts = ["你好，这是简体中文。", "我喜欢学习编程。"]
# converted_texts = convert_simplified_to_traditional(simplified_texts)

# for simplified_text, traditional_text in converted_texts.items():
#     print(f"Simplified: {simplified_text}")
#     print(f"Traditional: {traditional_text}")


import io
import json



with io.open(r"C:\Users\szhang\github\BimBean\helper\detail_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


dictionary = convert_simplified_to_traditional([x[2] for x in data.values()])

for value in data.values():
    value[2] = dictionary[value[2]]
    


with io.open(r"C:\Users\szhang\github\BimBean\helper\detail_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)