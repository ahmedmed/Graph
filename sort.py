import csv
with open ('Analyser.txt', 'r') as rf:
	with open ('Analyser_copy.txt','w') as wf:
		for line in rf:
			wf.write(line)



#with open('CacheSubSystem_copy.vcd') as csvfile:
 #   readCSV = csv.reader(csvfile, delimiter='|')
  #  for row in readCSV:
       
#with open('CacheSubSystem_copy.vcd', 'w') as writeFile:
 #   writer = csv.writer(writeFile)
  #  writer.writerows(lines)

#readFile.close()
#writeFile.close()







#with open('CacheSubSystem_copy.vcd', 'r') as csv_file:
   # csv_reader = csv.DictReader(csv_file)

    #with open('CSV.txt', 'w') as new_file:
       # fieldnames = ['parameter', 'size']

        #csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        #csv_writer.writeheader()

        #for line in csv_reader:
           
            #csv_writer.writerow(line)


bands = list()
with open ('Analyser_copy.txt')	as fin:
	for line in fin:
		bands.append(line.strip())

bands.sort()

filename = 'bands_sorted.txt'
with open ('Analyser_copy.txt','w') as fout:
	for band in bands:
		fout.write(band + '\n') 
