## Drill 1. Get the unique email domains (the part after @), lowercase:
emails = ["ali@Gmail.com", "sara@yahoo.com", "omar@gmail.com", "zara@YAHOO.com"]
domain = {email.split("@")[1].lower() for email in emails}
print(domain)

##Drill 2. From this sentence, get the set of unique word lengths:
sentence = "the cat sat on the big mat"


word_length = {len(word) for word in sentence.split()}


print(word_length)
