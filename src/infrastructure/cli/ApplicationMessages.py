welcome_message = "Welcome to NLTK-Me!\nWhat would you like to do?"
next_option_message = "What would you like to do next?"

tokenize_text = "1"
tokenize_sentence = "2"
remove_stopwords = "3"
count_total_words = "4"
count_repetitions_of_a_word = "5"
find_most_repeated_word = "6"
close_program = "7"
information = "info"

valid_user_options = [tokenize_text,
                      tokenize_sentence,
                      remove_stopwords,
                      count_total_words,
                      count_repetitions_of_a_word,
                      find_most_repeated_word,
                      close_program,
                      information]

tokenize_text_option = "1. Tokenize a text"
tokenize_sentence_option = "2. Tokenize a sentence"
remove_stopwords_option = "3. Remove stopwords"
count_total_words_option = "4. Count the total words of a text"
count_repetitions_option = "5. Count how many times a word appears in a text"
most_repeated_word_option = "6. Find the most repeated word in a text"
close_program_option = "7. Close the program"
display_info_option = "Do you want to know more about the different options? Just type 'info'!"
select_option_message = "Introduce a number to select an option: "

tokenize_text_select_file = "Let's tokenize a text! Please introduce the path to the file you want to tokenize."
tokenize_sentence_select_file = "Let's tokenize some sentences! Please introduce the path to the file you want to tokenize."
remove_stopwords_select_file = "Let's remove stopwords! Please introduce the path to the file you want to process."
count_total_words_select_file = "Let's count words! Please introduce the path to the file you want to process."
count_repetitions_select_file = "Let's count how many times a word is repeated! Please introduce the path to the file you want to process."
count_repetitions_input_message = "Now, please introduce the word you want to search for: "
most_repeated_word_select_file = "Let's find the most repeated word! Please introduce the path to the file you want to process."

display_info_title = "Did you ask for some info? Here you go!"
tokenize_text_info = "1. Tokenize a text: With Text Tokenizer, you can tokenize (split) a text into sentences. The text is split based on full stops. This option will create a file named 'processed.txt' in your desktop that will contain the result."
tokenize_sentence_info = "2. Tokenize a sentence: With Sentence Tokenizer, you can tokenize (split) a sentence into words. The sentences are split based on spaces. This option will create a file named 'processed.txt' in your desktop that will contain the result."
remove_stopwords_info = "3. Remove stopwords: This function removes the stopwords from a text. This means that all words with no meaning in the text (as articles, prepositions or punctuation marks) will be removed from the text. This option will create a file named 'processed.txt' in your desktop that will contain the result."
count_total_words_info = "4. Count the total words of a text: This function shows how many words are in the text. The result will be printed in the console."
count_repetitions_info = "5. Count how many times a word appears in a text: This function shows how many times a word appears in the text. The result will be printed in the console. lease note this function isn't case sensitive, which means that it differentiate between capital or lower-case letters."
most_repeated_word_info = "6. Find the most repeated word in a text: This function simply shows the most repeated word in the text! The result will be printed in the console. It's recommended to first execute the function 'Remove stopwords' in the file to avoid getting strange results (for instance, getting articles, pronouns or even punctuation marks as the most frequent word.)"

tokenize_file_succeeded = "Great! Your text has been tokenized! We have saved the output file here:\n"
remove_stopwords_succeeded = "Great! Your text has been processed! We have saved the output file here:\n"
count_total_words_succeeded = "Great! Your file has %s words."
count_repetitions_succeeded = "Done! The word %s appears %s times."
most_repeated_word_succeeded = "We found it! The most repeated word is: "

file_empty_or_not_found = "The file is empty or was not found!"
invalid_option_message = "\nSorry, the option you introduced is not correct. Please try again."
path_to_file_message = "Path to file: "
farewell_message = "\nThank you! Have a good day! :)"
credits_message = "\nNLTK-Me! CLI Version\nCreated by Macarena Avilés"

divider_start = "\n----------------------------------"
divider_end = "----------------------------------\n"
