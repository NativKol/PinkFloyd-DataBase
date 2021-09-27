FILE_PATH = r"C:\Users\nativ\PycharmProjects\untitled\magshimim\week4\HW4\Pink_Floyd_DB.txt"

def sort_file(file_path):
    """
    function that sort the file contains all of the details about pink floyd in dicts
    :param file_path: the address od the file
    :type file_path: str
    :return: a Data Structure after sort
    :rtype: dict
    """
    lines = sum(1 for line in open(file_path))      # check rows in file

    ##############
    # INITIALIZE #
    ##############

    album_dict = {}         # name:song tuple
    songs_tuple = ()        # (songs_dict, year)
    songs_dict = {}         # name:song_detail
    song_details = [0, 0, 0]       # [time, author, lyrics]
    my_file1 = open(file_path, "r")
    text1 = my_file1.read()
    full_lines = text1.split("\n")
    text1 = str(full_lines)
    add_album = False
    add_song = False
    add_song2 = False
    add_song3 = False
    album = ""
    song = ""
    time = ""
    author = ""
    year = ""
    lyrics = ""

    ##############
    # main sort #
    ##############

    for row in range(lines):
        line = full_lines[row]          # get line

        # album
        if line[0] == '#':
            if add_song2:
                song_details[0] = author
                song_details[1] = time
                song_details[2] = lyrics
                songs_dict.update({song: song_details})
                # initialize
                song_details = [0, 0, 0]
                song = ""
                lyrics = ""
                add_song2 = False
                add_song3 = False

            if add_album:
                songs_tuple = (songs_dict, year)
                album_dict.update({album: songs_tuple})
                # initialize
                album = ""
                songs_dict = {}

            for letter in range(len(line)):
                if not line[letter] == '#':
                    album += line[letter]
            album = album.split("::")
            year = album[1]
            album = album[0]
            # initialize
            add_album = True

        # song
        elif line[0] == '*':
            if add_song:
                if add_song3:
                    song_details = [0, 0, 0]
                    song_details[0] = author
                    song_details[1] = time
                    song_details[2] = lyrics
                    songs_dict.update({song: song_details})
                    # initialize
                    song = ""
                    lyrics = ""

            for letter in range(len(line)):
                if not line[letter] == '*':
                    song += line[letter]
            song = song.split("::")
            lyrics += song[3] + " \n"
            time = song[2]
            author = song[1]
            song = song[0]
            # initialize
            add_song = True
            add_song2 = True
            add_song3 = True

        # lyrics
        else:
            for letter in range(len(line)):
                if line[letter] != '*' and line[letter] != "#":
                    lyrics += line[letter]
            lyrics += "\n"

    # finalizing update
    song_details = [0, 0, 0]     # initialize
    song_details[0] = author
    song_details[1] = time
    song_details[2] = lyrics
    songs_dict.update({song: song_details})
    songs_tuple = (songs_dict, year)
    album_dict.update({album: songs_tuple})

    return album_dict

# list of albums
def action_one(text):
    text = text.keys()
    text = str(text)
    text = text[11:-2:]
    request = "201|ALBUM:" + text + "&SONG:NONE&LYRICS:NONE"        # add the data to the base of the protocol
    return request

# list of songs by album name
def action_two(text, album_name):
    try:
        text = text.get(album_name)
        text = text[0]
        text = text.keys()
        text = str(text)
        text = text[11:-2:]
        request = "202|ALBUM:NONE&SONG:" + text + "&LYRICS:NONE"         # add the data to the base of the protocol
    except Exception as e:
        request = "402|the album name is not valid"          # add the data to the base of the protocol (error)

    return request

# length of song by song name
def action_three(text, song_name):
    try:
        for key in text:                        # going through every song
            text1 = text.get(str(key))
            text1 = text1[0]
            if song_name in text1.keys():
                songs = text1.get(song_name)
                break
        text = songs[1]
        request = "203|ALBUM:NONE&SONG:(" + text + ")&LYRICS:NONE"          # add the data to the base of the protocol
    except Exception as e:
        request = "403|the song name is not valid"      # add the data to the base of the protocol (error)

    return request

# lyrics of song by song name
def action_four(text, song_name):
    try:
        for key in text:                    # going through every song
            text1 = text.get(str(key))
            text1 = text1[0]
            if song_name in text1.keys():
                songs = text1.get(song_name)
                break
        text = songs[2]
        request = "204|ALBUM:NONE&SONG:NONE&LYRICS:" + text         # add the data to the base of the protocol
    except Exception as e:
        request = "403|the song name is not valid"              # add the data to the base of the protocol (error)

    return request

# get album by the name of the song
def action_five(text, song_name):
    try:
        for key in text:                    # going through every song
            text1 = text.get(str(key))
            text1 = text1[0]
            if song_name in text1.keys():
                album = key
                break
        request = "205|ALBUM:" + album + "&SONG:NONE&LYRICS:NONE"       # add the data to the base of the protocol
    except Exception as e:
        request = "403|the song name is not valid"               # add the data to the base of the protocol (error)

    return request

# search song name by word
def action_six(text, word):
    word = word.lower()
    songs_with_word = ""
    text = text.values()
    text = tuple(text)
    for i in range(len(text)):          # going through every album
        text1 = text[i]
        text1 = text1[0]
        songs = text1.keys()
        songs = str(songs)
        songs = songs[11:-2:]
        songs = songs.lower()
        songs = songs.split(", ")
        for j in range(len(songs)):             # going through every song
            if str(word) in songs[j]:
                songs_with_word += songs[j] + ", "

    songs_with_word = songs_with_word[0:-2:]

    request = "206|ALBUM:NONE&SONG:" + str(songs_with_word) + "&LYRICS:NONE"  # add the data to the base of the protocol
    return request

# search song by word in the lyrics
def action_seven(text, word):
    word = word.lower()
    songs_with_word = ""
    text = text.values()
    text = tuple(text)
    for i in range(len(text)):          # going through every album
        text1 = text[i]
        text1 = text1[0]
        for key in text1.keys():            # going through every song
            lyrics = text1.get(key)
            lyrics = lyrics[2]
            lyrics = lyrics.lower()
            if word in lyrics:
                songs_with_word += key + ", "

    songs_with_word = songs_with_word[0:-2:]
    request = "207|ALBUM:NONE&SONG:" + str(songs_with_word) + "&LYRICS:NONE"  # add the data to the base of the protocol
    return request
