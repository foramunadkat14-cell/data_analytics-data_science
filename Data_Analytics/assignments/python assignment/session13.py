#1.  Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song names (like a Spotify playlist) and prints each song name one by one using recursion.

def print_playlist_songs(songs):
    if not songs:
        return
    print(songs[0])
    print_playlist_songs(songs[1:])



#2.  Create a recursive function count_unread_messages(messages) that takes a nested dictionary representing WhatsApp chat groups and subgroups, and returns the total number of unread messages across all groups.<br><br><em><strong>Hint:</strong> Each group can have a 'count' key for unread messages and a 'subgroups' key with a list of more groups.</em>

def count_unread_messages(messages):
    total = messages.get('count', 0)    
    for subgroup in messages.get('subgroups', []):
        total += count_unread_messages(subgroup)
    return total


#3.  Given the following code, identify which variables are local and which are global, and explain what will be printed when you call outer() and then print(x) at the end:<br><br>```python

# x = 'global'
# def outer():
# x = 'outer'
# def inner():
# nonlocal x
# x = 'inner'
# inner()
# print('Inside outer:', x)
# outer()
# print('Outside:', x)
# ```<br><br><em><strong>Hint:</strong> Focus on the scope of x inside and outside the functions.</em>


x = 'global'
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'inner'
    inner()
    print('Inside outer:', x)
outer()
print('Outside:', x)

#4.  Build a recursive function format_number_short(n) that takes a number (like a follower count on Instagram or YouTube) and returns it as a string in short format: 1500 as '1.5K', 1200000 as '1.2M', 500 as '500'.


def format_number_short(n, suffix_idx=0):
    suffixes = ["", "K", "M", "B", "T"]
    if n < 1000 or suffix_idx == len(suffixes) - 1:
        if suffix_idx == 0:
            return str(n)
        num_str = f"{n:.1f}".replace('.0', '')
        return f"{num_str}{suffixes[suffix_idx]}"
    return format_number_short(n / 1000, suffix_idx + 1)
