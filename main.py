book_path = "books/frankenstein.txt"

def main():
   contents = get_book_contents(book_path)
   num_words = get_num_words(contents)
   letters = get_num_letters(contents)
   sorted_letters_list = letters_sorted_to_list(letters)
   
   print(f"--- Begin report of {book_path} ---")
   print(f"There are {num_words} words found in the book.")
   print()

   for item in sorted_letters_list:
      if not item["letter"].isalpha():
         continue
      print(f"The '{item['letter']}' character was found {item['num']} times")

   print("--- End report ---")
   

def get_num_words(contents):
   word_count = contents.split()
   return len(word_count)

def sort_on(d):
   return d["num"]

def letters_sorted_to_list(letters):
   sorted_list = []
   for le in letters:
      sorted_list.append({"letter": le, "num": letters[le]})
   sorted_list.sort(reverse=True, key=sort_on)
   return sorted_list

def get_num_letters(contents):
   letters = {}
   for l in contents:
      lowered = l.lower()
      if lowered in letters:
         letters[lowered] += 1
      else:
         letters[lowered] = 1
   return letters

def get_letter_sums(contents):
   letter_sums = contents.split()
   return letter_sums
  
def get_book_contents(path):
   with open(book_path) as f:
      return f.read()


main()