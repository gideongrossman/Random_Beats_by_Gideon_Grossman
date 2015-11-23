
def GenerateSheetMusicImage():
    import subprocess
    path = 'C:\Gideon\Professional Education\djangoTutorialWithoutGal\hellodjango3\polls\static\polls\images'
    filename = 'testFile33'
    absolute_path = '%s\%s.ly' %(path, filename)
    sheet_music_file = open(absolute_path, 'w')
    sheet_music_file.write("\\version \"2.16.0\"\n{\n\tc\' b\' b\' b\'\n}")
    sheet_music_file.close()
    
    p = subprocess.Popen([
        r'C:\Program Files (x86)\LilyPond\usr\bin\lilypond-windows.exe',
        absolute_path
    ], cwd='C:\Gideon\Professional Education\djangoTutorialWithoutGal\hellodjango3\polls\static\polls\images')