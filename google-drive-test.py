from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

def main():
    # 1. Auth
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth = GoogleAuth()
    gauth.auth_method = 'service'
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('secrets/service_account.json', scope)
    drive = GoogleDrive(gauth)

    # 2. List all files
    file_list = drive.ListFile().GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))

    # 3. List all files in 'survey' folder
    file_list = drive.ListFile({'q': "parents in '1rm3ndf7blr_LAqQB3wnuf65YsKoUCr8v'"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))

    # 4. Create a file in 'survey' folder and add permision for dl.mini.2019 user
    file1 = drive.CreateFile({'title': 'Hello.txt', 'parents': [{'id': '1rm3ndf7blr_LAqQB3wnuf65YsKoUCr8v'}]})
    file1.SetContentString('Hello')
    file1.Upload()
    file1.InsertPermission({
        'type': 'user',
        'value': 'dl.mini.2019@gmail.com',
        'role': 'writer'
    })

    # 5. Delete all 'Hello.txt' files
    file_list = drive.ListFile().GetList()
    for file1 in file_list:
        if file1['title'] == 'Hello.txt':
            file1.Delete()

main()