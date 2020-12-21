def summer(x):
  local=0
  for i in x:
    local=local+i
  return local**2
def main():
  print("Sonuc:")
  print(summer([12,-7,5,-89.4,3,27,56,57.3]))
main()