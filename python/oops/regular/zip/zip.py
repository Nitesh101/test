import zipfile
zip = zipfile.ZipFile('new.zip','w')
zip.write('file1.txt')
zip.write('file2.txt')
zip.close()
