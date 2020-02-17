def main():
   word=input('Enter a word (more than three letters): ')
   word.upper()
   TripleConsecutive(word)
   print('in consecutive alphabetical order')
def TripleConsecutive(word):
   for i in range(len(word)-2):
      if ord(word[i])+2==ord(word[i+1])+1==ord(word[i+2]):
         print('{0} contains three successive letters'.format(word))
         break
      elif i==len(word)-3:
         print('{0} don\'t contains three successive letters'.format(word))
main()
      
         
