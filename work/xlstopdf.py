#Sam Albertson, June 25 2018

from win32com import client
import win32api, os, pdb, time

path = os.getcwd()+'\\'

os.chdir(path)

excel = client.DispatchEx("Excel.Application")

#requires full filepath, not just filename
def openWorkbook(filename):
    try:        
        xlwb = excel.Workbooks(filename)
    except Exception as e:
        try:
            xlwb = excel.Workbooks.Open(filename)
        except Exception as e:
            print(e)
            xlwb = None
    return(xlwb)

def saveWorkbook(wb,savename):
    ws = wb.Worksheets[0]
    wb.SaveAs(savename, FileFormat=57)
    wb.Close()
    excel.Quit()

def convertWorkbooks():
    for filename in os.listdir(path):
        if filename.endswith('xlsx'):
            fullname = path + filename
            savename = path + filename.split('.xlsx')[0] + '.pdf'
            wb = openWorkbook(fullname)
            saveWorkbook(wb,savename)

convertWorkbooks()