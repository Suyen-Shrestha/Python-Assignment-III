

def TowerOfHanoi(n , source, destination, auxilliary):
   if n == 1:
      print ("Move disk 1 from tower",source,"to tower",destination)
      return
   TowerOfHanoi(n-1, source, auxilliary, destination)
   print ("Move disk",n,"from tower",source,"to tower",destination)
   TowerOfHanoi(n-1, auxilliary, destination, source)


n = 4
print('Source tower: "A"')
print('Auxilliary tower: "B"')
print('Destination tower: "C"\n')

print(f'No. of discs: {n}\n')


TowerOfHanoi(n, 'A', 'C', 'B')

