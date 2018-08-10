import urllib.request
staffURL = 'http://csse1001.uqcloud.net/staff-info'

def getURL():
    stream = urllib.request.urlopen(staffURL)
    text = stream.read().decode('utf-8')
    stream.close()
    return text

def getText():
    """ Return the text in the file, 'staff.html'

    Parameters:
        No parameters

    Return:
        str: text in 'staff.html'
    """
    fd = open('staff.html', 'r')
    text = fd.read()
    fd.close()
    return text

def find(substr, string, start):
    """Return the position of the first substr in string, starting from start.
    Return None if not found

    Parameters:
        substr(str): substring being searched for
        string(str): string being searched
        start(str): index where the search begines

    Return:
        int: index where substr is found within string
    """
    pos = start
    size = len(substr)
    while pos < len(string):
        if substr == string[pos:pos+size]:
            return pos
        pos += 1
    return None

text = getText()
heading_index = find("ITLC Tutors", text, 0)
if heading_index is None:
    print("Heading not found")
else:
    room_index = find("Room:", text, heading_index)
    if room_index is None:
        print("Room not found")
    else:
        tag_index = find("<", text, room_index)
        if tag_index is None:
            print("tag not found")
        else:
            print(text[room_index+6:tag_index])
