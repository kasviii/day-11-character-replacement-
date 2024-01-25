def replace_char(input_str, char_to_replace, replacement_char):
    output_str = ""
    for char in input_str:
        if char == char_to_replace:
            output_str += replacement_char
        else:
            output_str += char
    return output_str

input_str = input("Enter a string: ")
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the replacement character: ")

output_str = replace_char(input_str, char_to_replace, replacement_char)

print(f"Input: {input_str}\nOutput: {output_str}")
