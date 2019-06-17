# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# (Use the English alphabet with 26 letters!)
# უნდა დავწეროთ ფუნქცია რომელიც მიიღებს ლისტს რომელშიც იქნება ალფაბეტის მიხედვით ასობგერები, და 
# ფუნქციამ უნდა დააბრუნოს ის ასობგერა რომელიც არის გამოტოვებული ლისტში (ალფაბეტის მიხედვით)
#მაგალითად:
#['a','b','c','d','f'] -> 'e'
#['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):
    alphabet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # ანბანი, დიდ და პატარა ასოებში (საჭიროა)
    chars_first = chars[0] # მიღებული ლისტის პირველი ასო.

    alphabet_index = alphabet.index(chars_first) # თუ მერამდენე ადგილზეა ასობგერა (chars_first)
    chars_len = alphabet_index+1+len(chars) # ამით მოხდება ინდექსაციის ფარგლების განსაზღვრა ცვლად alphabet ში, chars ისთვის
    for x in alphabet[alphabet_index:chars_len]: # მოხდა ფარგლების განსაზღვრა chars ისთვის
        if x not in chars: # თუ ლისტ chars ში ვერ მოიძებნა ასობგერა მაშინ დააბრუნოს ვერმოძებნილი ასობგერა ;)
            return x
            
print(find_missing_letter(['a','b','c','d','f']))            
