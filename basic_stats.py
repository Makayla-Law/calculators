import statistics

og_data = '19, 20, 22, 23, 24, 24, 26, 26, 28, 29, 30, 32, 33, 34, 35, 37, 37, 38, 38, 42'
print('Original Data: '+og_data)

def statsfunc(og_data):
  og_datasplit = og_data.split(',')
  og_dataclean1 = [i.replace(',','') for i in og_datasplit]
  og_dataclean = [float(i) for i in og_dataclean1]
  mean = statistics.mean(og_dataclean)
  print('Mean: '+str(mean))
  numerator_lis = []
  for i in og_dataclean:
    q = (int(i))-mean
    j = q**2
    numerator_lis.append(j)
  
  print('Numerator terms to sum: '+str(numerator_lis)+'\n')
  
  
  numerator_sum = 0
  for i in numerator_lis:
    numerator_sum+= int(i)
  print('Numerator:'+str(numerator_sum)+'\n')
  denominator = (len(numerator_lis))-1
  print('Denominator: '+str(len(numerator_lis))+'-1' +' = '+str(denominator)+'\n')
  variance = numerator_sum/denominator
  
  print(str(numerator_sum)+'/('+str(len(numerator_lis))+'-1)'+' = Variance = '+str(variance))
  print('Standard Deviation: '+str(variance**(1/2)))
  
new_data= ('0.72,0.14, 0,09,0.03,0.02')
statsfunc(new_data)
