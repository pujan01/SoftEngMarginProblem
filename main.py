with open('input.txt', 'r') as f:
  with open('DAT1.txt', 'w') as w:
   lineCounter = 0
   for lines in f:
     lineCounter += 1
     if lineCounter == 1:
       line = lines.split()
       leftMargin = int(line[0])
       rightMargin = int(line[1])
       continue
     print(" "*leftMargin, end = '')
     w.write(" "*leftMargin)
     marginPosition = leftMargin
     line = lines.split()
     for words in line:
       wordlength = len(words)
       if (marginPosition + wordlength) > (80 - rightMargin):
          marginPosition = leftMargin + wordlength + 1
          toWrite = "\n" + " "*leftMargin + words + " "
       else:
         if words.endswith("."):
           marginPosition += wordlength + 2
           toWrite = words + "  "
         else:
           marginPosition += wordlength + 1
           toWrite = words + ' '
       print(toWrite, end = '')
       w.write(toWrite)
     print()
     w.write('\n')

