#!/usr/bin/env python3
import wget

url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png"

def wget_pic(imagelink):
    out_file ='/Users/zhhongxi/Desktop/pythonStudy/pythonProjects'
    pokemon = wget.download(imagelink, out=out_file)

wget_pic(url)

