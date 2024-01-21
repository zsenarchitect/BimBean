"""run in venv"""

import opencc

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

# Example usage:
simplified_texts = ["你好，这是简体中文。", "我喜欢学习编程。"]
converted_texts = convert_simplified_to_traditional(simplified_texts)

for simplified_text, traditional_text in converted_texts.items():
    print(f"Simplified: {simplified_text}")
    print(f"Traditional: {traditional_text}")
