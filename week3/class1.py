def read_file_to_string(file_path="jason_learning_figma.pdf"):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        return f"This is an error:{e}"
    

content_string = read_file_to_string()
print(content_string)


list_of_bad_words = ["beat", "kill", "harm", "hurt", "maime", "burry"]

def find_bad_words(content):
    list_of_words = content.split(" ")

    for word in list_of_words:
        for bad_word in list_of_bad_words:
            if word == bad_word:
                return True
    
    return False

print(find_bad_words(content_string))
