import subprocess

try:
    from comtypes import client
except ImportError:
    client = None

def doc2pdf(doc):
    """
    convert a doc/docx document to pdf format
    :param doc: path to document
    """
    doc = os.path.abspath(doc) # bugfix - searching files in windows/system32
    if client is None:
        return doc2pdf_linux(doc)
    name, ext = os.path.splitext(doc)
    try:
        word = client.CreateObject('Word.Application')
        worddoc = word.Documents.Open(doc)
        worddoc.SaveAs(name + '.pdf', FileFormat=17)
    except Exception:
        raise
    finally:
        worddoc.Close()
        word.Quit()


def doc2pdf_linux(doc):
    """
    convert a doc/docx document to pdf format (linux only, requires libreoffice)
    :param doc: path to document
    """
    cmd = 'libreoffice --convert-to pdf'.split() + [doc]
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=10)
    stdout, stderr = p.communicate()
    if stderr:
        raise subprocess.SubprocessError(stderr)
