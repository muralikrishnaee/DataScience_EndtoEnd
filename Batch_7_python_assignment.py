####################################
#Questions on String
###################################

#Input String for assignments 
inp_str = " I am very keen in building up my career in Data Science, but not sure from where to start. If I search the web it throws me thousands of articles, few are relevant others make me confused, again I come around to the same page. Supervised has provided me a good platform to remove all such qualms which were wrangling in my mind"
print(inp_str)



# Problem 1
# Consider the above text as a string, figure out the average length of the string.
string_length = len(inp_str)
print("The average length of the given string is: \t", string_length)

# In my understanding avergae length of the string is ratio of length of sum of the words to number of words
# split the string 
import string
string_split = inp_str.split()

# sum of length of words
sum_length_of_words = sum([len(word) for word in string_split])
print("Length of sum of the words: \t", sum_length_of_words)

count_of_words = len(string_split)
print("Count of the words: \t", count_of_words)

average_length = round((sum_length_of_words/count_of_words),2)
print("Avergae length of the given String is: \t", average_length)



# Problem 2 
# Lower the text in the string.
string_lower = inp_str.lower()
print(string_lower)



# Problem 3 
# Try to get the clean text removing the punctuation from the string.
#Identify puctuations
punctuations = ""
for word in string.punctuation:
    punctuations = punctuations + word
print("Identified Punctuations are: \n", punctuations)

# Elimiate and return the string without punctuations
final_string = ""
for word in inp_str:
    if word not in punctuations:
        final_string = final_string + word
print("String free from punctuations is: \n", final_string)
 


# Problem 4
# Extract word "Data Science" from the string.
# My method is to find the position of Data Science word , find the length and use slice 
# method to fetch the string 
word_to_extract = "Data Science"

# use find to calculate the starting position of the word 
start_of_the_word = inp_str.find(word_to_extract)
print("Starting poisition of the word is: \n", start_of_the_word)

# length of the word 
length_of_the_word = len(word_to_extract)
print("Length of the word is: \n", length_of_the_word)

# Slice the string
Final_extract = inp_str[start_of_the_word:(start_of_the_word + length_of_the_word)]
print("Word extracted is: \n", Final_extract)



# Problem 5 
# Find the frequency of words used in the string.
# Split the string into words
words_from_string = inp_str.split()

# create empty lists for appending word count and word processing
freq_of_words = []

for word in words_from_string: 
    # calculate count of words and append to the list
    count_of_words = words_from_string.count(word)
    freq_of_words.append(count_of_words)
    
print(freq_of_words)
word_count_pair = list(zip(words_from_string,freq_of_words))

# remove duplicate pairs 
final_word_count_pair = list(set(word_count_pair))
        
print("Final word counts are: \n", final_word_count_pair)



#Problem 6
#Fetch the duplicate pairs used in the string.

split_string = inp_str.split()

count_string = []
word_processing = []

for word in split_string:
    if split_string.count(word) > 1:
        word_processing.append(word)
        count_string.append(split_string.count(word))
        word_count_pair = list(zip(word_processing,count_string))
        
        duplicate_word_count_pair = list(set(word_count_pair))
print("Final list of duplicate word count pairs are: \n", duplicate_word_count_pair)    



# Problem 7 
# Can you change the word "Supervised" to "Unsupervised" in the string

print("Oringinal String is: \n", inp_str)
final_str = inp_str.replace('Supervised','Unsupervised')
print("\nFinal String is: \n", final_str)



# Problem 8
# Splitting of the string with a dot operator(.)
split_strings = inp_str.split('.')
for str in split_strings:
    print("\nStrings after splitting based on '.' operator are: \n",str)



# Problem 9 
# Find the words from the string which ends with "e"

string_ends_with_e = []
split_words = inp_str.split()
for word in split_words:
    if word.endswith('e'):
        string_ends_with_e.append(word)
print("List of words ends with 'e' are: \n", string_ends_with_e)    



# Pronlem 10 
# Figure out number of a's used in the string.
# Method: 1
for i in inp_str: 
    if i == 'a': 
        count = inp_str.count(i)
print("count of 'a's are:", count)

# Method: 2
c = len([i for i in inp_str if i == 'a'])
print("count of 'a's are:", c)

# Method: 3
cc = inp_str.count('a')
print("count of 'a's are:", cc)



####################################
#Questions on String
###################################
# Data
# In the weekend , I purchased 250g of apple, 500g of sugar, 2.5 kg of rice, 2.5 litres of milk 
# and finally 1 dozen of egg.

# Problem 1 
# Can you help me frame the above purchase in the form of dictionary with commodities as keys to it.
items ={'apple':0.25, 'sugar':0.5, 'rice':2.5, 'milk':2.5, 'egg':1 }
print(items)



# Problem 2
# I forgot to mention another item, 1kg of atta packet. Can you also add it ?
items.update({'atta':1})
print(items)



# Problem 3
# Instead of 2kg of rice, I bought only 1kg of rice. Can you change the corresponding value ?
items.update({'rice':1})
print(items)



# Problem 4 
# Can you list out all these items using a loop.
for item in items.items():
    print(item)



# Problem 5 
price = {'apple':220, 'sugar':43, 'rice':45, 'milk': 30, 'egg':60}
print(price)

final_price = sum(items[k] * price[k] for k in price)
print(final_price)




####################################
#Questions on List
###################################

#data
# AI companies list 
ai_companies = ['Amazon', 'Facebook', 'HiSilicon', 'Google', 'Apple', 'Microsoft', 'SenseTime']
print(ai_companies)

# Problem 1 
# Sort the list in ascending order

ai_companies.sort()
print("Sorted list: \n", ai_companies)

ai_companies.sort(reverse=True)
print("Sorted list: \n", ai_companies)



# Problem 2 
# Add multiple companies at once 'Nvidia', 'OpenAI' , 'Qualcomm' and 'Reliance' to the list
ai_companies.extend(['Nvidia','OpenAI','Qualcomm','Reliance'])
print(ai_companies)



# Problem 3
# Lower the list using List comprehension
ai_companies_lower = [item.lower() for item in ai_companies]
print(ai_companies_lower)



# Problem 4 
# Elimiate 'Reliance' from the list
ai_companies_final = [item for item in ai_companies if item != "Reliance"]
print(ai_companies_final)



# Problem 5
# Extract 'Facebook', 'Google' and 'Microsoft' using a single command
ai_companies_final = [item for item in ai_companies if item in ['Facebook', 'Google' , 'Microsoft']]
print(ai_companies_final)




####################################
#Questions on Tuple
###################################
# Problem 1 
# Consider the above standard price problem statement and place the prices in the form of the tuple.
price_tuple = (220, 43, 45, 30, 60)
print(price_tuple)
type(price_tuple)



# Problem 2
# Find out the min and max price among them.
min_price = min(price_tuple)
max_price = max(price_tuple)

print("Minimum Price is :\t", min_price)
print("Maximum Price is :\t", max_price)



# Problem 3 
# Also, convert the above "AI_companies" list to a tuple.
ai_companies_tuple = tuple(ai_companies)
print(ai_companies_tuple)



# Problem 4 
# Combine two above tuples to a single tuple.
final_tuple = price_tuple + ai_companies_tuple
print(final_tuple)



# Print 5
# Compare the length of two tuples.
len1 = len(price_tuple)
len2 = len(ai_companies_tuple)

if len1 == len2: 
    print("Both the Tuples have same length")
else: 
    print("Both the Tuples have different length")        











































