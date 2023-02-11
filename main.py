def main():

   with open("books/frankenstein.txt", "r") as f:
      file_contents = f.read()
      print(file_contents)

      word_count = file_contents.split()
      number_of_words = len(file_contents.split())
      print(f"The total word count of this book is:", number_of_words)

   letter_dict = {}

   for i in file_contents.lower():
      if i in letter_dict:
         letter_dict[i] += 1
      else:
         letter_dict[i] = 1
   print(letter_dict)

main()