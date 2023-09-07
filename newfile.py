import re
import PyPDF2


def extract_vowel_words(text):
    words = re.findall(r'\b[aeiouAEIOU]\w+\b', text)
    return words


def main():
    input_pdf_path = 'C:\\Users\\master\\Desktop\\sample.pdf'
    output_txt_path = 'vowel_words.txt'

    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()

    vowel_words = extract_vowel_words(text)

    with open(output_txt_path, 'w') as output_file:
        for word in vowel_words:
            output_file.write(word + '\n')

    print("Vowel words:")
    for word in vowel_words:
        print(word)


if __name__ == "__main__":
    main()

