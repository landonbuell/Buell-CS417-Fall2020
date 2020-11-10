from tkinter import (Tk, Button, BOTH, messagebox, Frame, Label,
                     filedialog, W, Entry, StringVar)
from zipfile import ZipFile
from typing import List
from pathlib import Path
import os
import sys

class UI:
    """
    Find files in this directory, and extract all their
    contents into this directory.

    If files are encrypted, ask for passwords.
    """
    def __init__(self):
        filenames: List[str] = self.get_zips()
        if not filenames:
            messagebox.\
                showwarning('No zip files',
                            'There are no zip archives here')
            sys.exit(1)

        self.zip_filenames: List[str] = []
        for zip_name in filenames:
            result_code = self.extract_all(zip_name)
            if result_code:
                if result_code == 'File exists':
                    messagebox.showwarning('File(s) exists',
                                           'File(s) already unpacked.\n'
                                           + "Won't overwrite existing files")
                    sys.exit(1)
                self.zip_filenames.append(zip_name)

        self.master: Tk = Tk()
        self.master.title('Simple ZIP extractor')

        self.archive_done: List[bool] = [False] * len(self.zip_filenames)

        file_table: Frame = Frame(self.master)
        file_table.pack()
        my_font: Tuple[Any] = ('Helvetica', 12)

        label: Label
        label = Label(file_table, text="File", font=my_font)
        label.grid(row=0, column=0, sticky=W)
        label = Label(file_table, text="Password", font=my_font)
        label.grid(row=0, column=1, sticky=W)
        label = Label(file_table, text="", font=my_font)
        label.grid(row=0, column=2, sticky=W)

        btn: Button
        self.pwd_variables: List[StringVar] = []
        for index, filename in enumerate(self.zip_filenames):
            row_num = index + 1
            label = Label(file_table, text=filename, font=my_font)
            label.grid(row=row_num, column=0, sticky=W)

            pwd_var = StringVar()
            self.pwd_variables.append(pwd_var)
            pwd_entry: Entry = Entry(file_table, width=16,
                                     textvariable=pwd_var,
                                     font=my_font)
            pwd_entry.grid(row=row_num, column=1, stick=W)

            btn = Button(file_table, text='Extract',
                         command=lambda x=index: self.extract(x))
            btn.grid(row=row_num, column=2, stick=W)


        btn = Button(self.master, text='Cancel', command=self.quit)
        btn.pack(fill=BOTH, expand=1)

        self.master.lift()
        self.master.update()
        self.master.mainloop()

    def get_zips(self) -> List[str]:
        filenames: List[str] = os.listdir(".")
        zips: List[str] = []
        for name in filenames:
            if name.lower().endswith(".zip"):
                zips.append(name)
                archive: ZipFile = ZipFile(name)
                zip_filenames: List[str] = archive.namelist()
                for stored_name in zip_filenames:
                    info: ZipInfo = archive.getinfo(stored_name)
        return zips

    def extract_all(self, zipfile_name: str, password: bytes=b'') -> bool:
        archive: ZipFile = ZipFile(zipfile_name)
        zip_filenames: List[str] = archive.namelist()

        filename: str
        extraction_failed: bool = False
        error_code: str = ""
        for filename in zip_filenames:
            file_pathname: Path = Path(filename)
            if file_pathname.exists():
                return "File exists"

            if password:
                try:
                    archive.extract(filename, ".", pwd=password)
                except RuntimeError as e:
                    error_code = str(e)
                    break

            else:
                try:
                    archive.extract(filename, ".")
                except RuntimeError as e:
                    error_code = str(e)
                    break

        if 'encrypted' in error_code:
            return 'Archive is encrypted'
        if 'Bad password' in error_code:
            return 'Bad password'
        return ""

    def extract(self, index: int) -> bool:
        zipfile_name: str = self.zip_filenames[index]
        password: bytes = bytes(self.pwd_variables[index].get(),
                                encoding='utf8')
        error_code = self.extract_all(zipfile_name, password)
        if error_code:
            messagebox.showwarning('Extraction Failed', error_code)
        else:
            self.archive_done[index] = True
            messagebox.showwarning('Extraction Successful',
                                   zipfile_name + ' unpacked successfully')

        archives_remain = sum(1
                              for done in self.archive_done
                              if not done)
        if not archives_remain:
            self.quit()

    def quit(self) -> None:
        self.master.withdraw()
        self.master.destroy()

def main():
    ui: UI = UI()

if __name__ == '__main__':
    main()




