import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,at):
        self.at = at

    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.at)
        for root,dirs,files in os.walk(file_from):
            for i in files:
                localPath = os.path.join(root,i)
                relativePath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file_to,relativePath)
                with open(localPath,"rb") as f:
                    dbx.files_upload(f.read(),dropboxPath,mode = WriteMode("overwrite"))

def main():
    at = "kmrypCXkgNEAAAAAAAAAAfjMTouLsgphnezNscGDTfVqSmzXcJ5MeqzN_nVfj4bP"
    transferData = TransferData(at)
    file_from = str(input("Enter The FolderPath to Transfer To Dropbox"))
    file_to = input("Enter The full Path To Upload To Dropbox")
    transferData.uploadFile(file_from,file_to)
    print("The File Has Been Moved")

main()


