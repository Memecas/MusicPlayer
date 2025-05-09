#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

class FileExplorer:
    def __init__(self, root, current):
        
        # Atributos
        self._root_folder = Path(root)  # Pasta raiz onde estão as músicas
        self._current_folder = Path(current)  # Pasta atual para navegação
    
    # Método para listar subpastas no diretório atual
    def sub_folders(self):
        subs = []
        
        for item in self._current_folder.iterdir():
            if item.is_dir():
                subs.append(item)  # Adiciona apenas pastas
                
        return subs  # Retorna a lista de subpastas

    # Método para selecionar uma pasta e atualizar a pasta atual
    def select_folder(self, path):
        
        if isinstance(path, Path) and path.is_dir():  # Verifica se path é um diretório
            self._current_folder = path  # Atualiza a pasta atual

    # Método para listar arquivos MP3 na pasta atual
    def mp3_list(self):
        paths = []
        
        for item in self._current_folder.glob('*.mp3'):
            paths.append(item)  # Adiciona arquivos MP3 à lista
            
        return paths  # Retorna a lista de arquivos MP3

            
                
        
        
            
        
        
        