import subprocess

DEBUG = 0

def GetActualFileName(fileToLookup):

  errorFound = False
  command = 'ls ' + fileToLookup
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  if DEBUG:
    print(result.returncode, result.stdout, result.stderr)

  if result.stderr:
    print("error found")
    print('Error code:' + str(result.returncode))
    print(result.stderr)
    errorFound = True
  else:
    print("no error found")
    print('Error code:' + str(result.returncode))
    print(result.stdout)


  returnStr = result.stdout
  if DEBUG:
    print(returnStr)
  returnStr =  returnStr[returnStr.find('/')+1:]
  returnStr = returnStr.strip('\n')
  return errorFound, returnStr

errorFound, result = GetActualFileName('temp/milan1_*.pgp')
print(result)
errorFound, result = GetActualFileName('temp/filedoesntexist.pgp')
if errorFound:
  print("cant find the file you are looking for")
else:
  print("all good")
