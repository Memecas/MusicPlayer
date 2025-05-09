#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

class FileExplorer(Path):
    def __init__(self, root,current):
        
        #Attributes
        self._root_folder = Path(root) #root_folder_of_all_music_folders
        root_dir = self._root_folder
        self._current_folder = Path(current) #folder_navigated_through_subfolders 
        curr_dir = self._current_folder
        
        #Methods
        def sub_folders():
            subs = []
            
            for item in root_dir.iterdir():
                
                if item.is_dir():
                    subs.append(item)
                    
                else: return None
                
            return subs
        
        def select_folder(self,path):
            
            if isinstance(path,Path):
                self._current_folder = path
            
        def mp3_list(self):
            paths = []
            
            for item in curr_dir.glob('*.mp3'):
                paths.append(item)
                
            return paths
            
                
        
        
            
        
        
        