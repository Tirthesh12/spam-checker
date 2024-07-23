data = None

try:
  with open("key_word.txt","r")as f:
    data = f.read()
except FileNotFoundError:
  print("File Not Found!")

#print(data)

def spam_check(sentence,spam_list):
  sentence = sentence.lower()
  for word in spam_list:
    if word.lower() in sentence:
      print("marked as spam")
      return True
  print("The given sentence is safe")
  return False

x = spam_check("hey there i am playing Betting",data.split(', '))
print(x)