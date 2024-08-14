def converter_camel_case(s):
    palavra = s.split('_')
    frase = ''.join(palavra)
    return frase

str1 = "hello_world"
str2 = "this_is_a_snake_case_string"

print(converter_camel_case(str1))
print(converter_camel_case(str2))