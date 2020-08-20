def readFile(filename):
  return filename.read()
def topTenWords(wordCountDict):
  f1= open('stopwords.txt', 'r')
  stop_words = f1.read().split()
  f1.close()
  stopWordsDict = {}
  for word in stop_words:
    stopWordsDict[word] = 1
  from heapq import heappop, heappush, heapify
  heap = []
  for key in wordCountDict:
    if key not in stopWordsDict and key!='':
      heappush(heap, (-1*wordCountDict[key], key))
  for i in range(10):
    print(heappop(heap)[1])
  
def wordCount(contents):
  words = contents.split()
  Dict ={}
  import string
  table = str.maketrans('', '', string.punctuation)
  for i in range(len(words)):
    word = words[i].translate(table)
    word = word.lower()
    words[i] = word
  for word in words:
    if word in Dict:
      Dict[word] = Dict[word]+1
    else:
      Dict[word] = 1
  return Dict    
def main():
  filename= open('sample.txt', 'r')
  contents= readFile(filename)
  wordCountDict= wordCount(contents)
  topTenWords(wordCountDict)
if __name__ == "__main__":
    main()  