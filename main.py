import credentials
import dropbox

dbx = dropbox.Dropbox(credentials.ACCESS_TOKEN)

def main():

    for entry in dbx.files_list_folder('').entries:
        print(entry.name)
    push_to_dbx('abc.jpg')






def push_to_dbx(file_path)
    f = open(file_path)
    file_size = os.path.getsize(file_path)

    write_mode = dropbox.files.WriteMode('overwrite',None)

    CHUNK_SIZE = 4 * 1024 * 1024

    if file_size <= CHUNK_SIZE:
        print dbx.files_upload(f, dest_path)
    else:
        upload_session_start_result = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
        cursor = dropbox.files.UploadSessionCursor(session_id=upload_session_start_result.session_id,
                                                   offset=f.tell())
        commit = dropbox.files.CommitInfo(path=dest_path,
                                          mode=write_mode,
                                          autorename=false)
        while f.tell() < file_size:
            if ((file_size - f.tell()) <= CHUNK_SIZE):
                print dbx.files_upload_session_finish(f.read(CHUNK_SIZE),
                                                cursor,
                                                commit)
            else:
                dbx.files_upload_session_append(f.read(CHUNK_SIZE),
                                                cursor.session_id,
                                                cursor.offset)
                cursor.offset = f.tell()




if __name__ == "__main__":
    main()