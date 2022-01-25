import dropbox

class CS:
    def __init__(self,password):
#password is the access token provided by the user for the dropbox
        self.password=password  
    def upload_file(self,file_to,file_path):
        dbx=dropbox.Dropbox(self.password)
#file_to is the destination of the file
#dbx is a variable. dropbox is a module and Dropbox is a function
        file1=open(file_path,'rb')
#We have to read the file using rb(b=binary)
        readFile=file1.read()
#Variable is always = first variable.function(). Also, is we open a file (Line 12)
## we also have to use the read FUNCTION (Line 14) 
        dbx.files_upload(file1.read(),file_to)

def main():
#main doesn't have a parameter
    password='sl.BAzJnpfymppSAtxUt0XboThtq67tTecubJzwYKTXp0v0J2BYTjhN6jpiTfzBCk5XZGYNfdX3jdg-zYwzToFfbblhYUbiKGdMg0banGKcOIG7GhRALlsS0UDofEnIRtSoTOSJu2k'
    file_from=input("Enter your file's path")
    file_to=input("Enter your file's path to upload to dropbox")
    object=CS(password) 
    object.upload_file(file_to,file_from)
main()
   
        

        

