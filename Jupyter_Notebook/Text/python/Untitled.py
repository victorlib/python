
# coding: utf-8

# In[10]:


from subprocess import Popen, PIPE
import time

def convert(src, dst):
    d = {'src': src, 'dst': dst}
    commands = [
        '/usr/bin/docsplit pdf --output %(dst)s %(src)s' % d,
        'oowriter --headless -convert-to pdf:writer_pdf_Export %(dst)s %(src)s' % d,
    ]

    for i in range(len(commands)):
        command = commands[i]
        st = time.time()
        process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True) # I am aware of consequences of using `shell=True` 
        out, err = process.communicate()
        errcode = process.returncode
        if errcode != 0:
            raise Exception(err)
        en = time.time() - st
        print ('Command %s: Completed in %s seconds' % (str(i+1), str(round(en, 2))))
if __name__ == '__main__':
    src = 'C:/Users/Administrator/Desktop/pdf/Temp.doc'
    dst = 'C:/Users/Administrator/Desktop/pdf/Temp.pdf'
    convert(src, dst)

