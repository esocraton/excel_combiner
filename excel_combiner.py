"""
excel_combiner by esocraton

MIT License

Copyright (c) 2023 Samil Boyalikli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import pandas as pd

print("""EXCEL COMBINER




""")
file_paths = []

def head():
    file_name = input("Type the names of the files you want to merge: ")
    real_file_name = f'{file_name}.xlsx'
    file_paths.append(real_file_name)
def end():
    main_file_name = input("Type the name of the main file where the files you merged are combined: ")
    dataframes = [pd.read_excel(file_path) for file_path in file_paths]
    combined_df = pd.concat(dataframes)
    combined_df.to_excel(f'{main_file_name}.xlsx', index=False)

while True:
    choise = input("""
    Press 1 to add a file
    Press 0 to merge the files you added
    1 or 0: """)
    if choise == '1':
        try:
            head()
        except Exception as e:
            print(e)
            print("""
            
            
            
            Please write the error to us...
            esocraton@gmail.com""")
            time.sleep(30)
            print("""




            bemsoft      @       esocraton""")
            time.sleep(3)
            break
    elif choise == '0':
        try:
            end()
            print("""
        
        
        
        
            bemsoft      @       esocraton""")
            time.sleep(3)
            break
        except Exception as e:
            print(e)
            print("""



            Please write the error to us...
            esocraton@gmail.com""")
            time.sleep(30)
            print("""




                        bemsoft      @       esocraton""")
            time.sleep(3)
            break
    else:
        print("Please press 1 or 0")
