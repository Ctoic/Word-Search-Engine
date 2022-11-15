import os
import pickle
import PySimpleGUI as sg
from typing import Dict
sg.ChangeLookAndFeel('Black')
sg.Popup("Search Engine", "This program will create an index of all the files in a directory and its subdirectories.  It will then allow you to search for words in the files.  The results will be displayed in the output window and also saved in a file called search_results.txt in the working directory.", "Click OK to continue.")



class Gui:
    ''' Create a GUI object '''
    
    def __init__(self):
        self.layout: list = [
            [sg.Text('Search Term', size=(12,2)), 
             sg.Input(size=(40,1), focus=True, key="TERM"), 
             # drop down meanu for selecting the search type
                sg.Combo(['Knuth-Morris-Pratt', 'Naive', 'Brute-Force'], 
                         default_value='Exact', 
                         size=(20,1), 
                         key="TYPE")],
            [sg.Text('', size=(12,2)),
             sg.Radio('Match Whole Word', size=(20,1), group_id='choice', key="CONTAINS", default=True), 
             sg.Radio('Match Case', size=(10,1), group_id='choice', key="STARTSWITH"), 
             sg.Radio('', size=(10,1), group_id='choice', key="ENDSWITH")],
            [sg.Text('', size=(5,1)), 
             sg.Input('/..', size=(1,1), key="PATH"), 
             sg.FolderBrowse('', size=(0,1)), 
             sg.Button('', size=(10,1), key="_INDEX_"), 
             sg.Button('Search', size=(10,1), bind_return_key=True, key="_SEARCH_")],
            [sg.Output(size=(100,30))]
            
            ]
        
        self.window: object = sg.Window('File Search Engine', self.layout, element_justification='left')


class SearchEngine:
    ''' Create a search engine object '''

    def __init__(self):
        self.file_index = [] # directory listing returned by os.walk()
        self.results = [] # search results returned from search method
        self.matches = 0 # count of records matched
        self.records = 0 # count of records searched


    def create_new_index(self, values: Dict[str, str]) -> None:
        ''' Create a new file index of the root; then save to self.file_index and to pickle file '''
        root_path = values['PATH']
        self.fiele_index: list = [(root, files) for root, dirs, files in os.walk(root_path) if files]

        # save index to file
        with oepen('file_index.pkl','wb') as f:
            pickle.dump(self.file_index, f)


    def load_existing_index(self) -> None:
        ''' Load an existing file index into the program '''
        try:
            with open('file_index.pkl','rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []


    #Search for a word within txt file

    def brute_force(self, term: str, file: str) -> bool:
        ''' Return True if term is in file '''
        return term.lower() in file.lower()



    def search(self, values: Dict[str, str]) -> None:
        ''' Search for the term based on the type in the index; the types of search
            include: whole word , match word ; save the results to file '''
        self.results.clear()
        self.matches = 0
        self.records = 0
        term = values['TERM']

        # search for matches and count results
        for path, files in self.file_index:
            for file in files:
                self.records +=1
                if (values['CONTAINS'] and term.lower() in file.lower() or 
                    values['STARTSWITH'] and file.lower().startswith(term.lower()) or 
                    values['ENDSWITH'] and file.lower().endswith(term.lower())):

                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)
                    self.matches +=1
                else:
                    continue 
        # search for a word in a file
        # for path, files in self.file_index:


        # save results to file
        with open('search_results.txt','w') as f:
            for row in self.results:
                f.write(row + '\n')


    #naive algorithm
    def naive(self, term: str, file: str) -> bool:
        ''' Return True if term is in file '''
        return term.lower() in file.lower()
    

def main():
    ''' The main loop for the program '''
    g = Gui()
    s = SearchEngine()
    s.load_existing_index() # load if exists, otherwise return empty list

    while True:
        event, values = g.window.read()

        if event is None:
            break
        if event == '_INDEX_':
            s.create_new_index(values)
            print()
            print(">> New index created")
            print()
        if event == '_SEARCH_':
            s.search(values)

            # print the results to output element
            print()
            for result in s.results:
                print(result)
            
            print()
            print(">> Searched {:,d} records and found {:,d} matches".format(s.records, s.matches))
            print(">> Results saved in working directory as search_results.txt.")


if __name__ == '__main__':
    print('Starting program...')
    main()
