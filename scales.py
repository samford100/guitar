notes = ['A ', 'A#', 'B ', 'C ', 'C#', 'D ', 'D#', 'E ', 'F ', 'F#', 'G ', 'G#']

# whole, whole, half, whole, whole, whole, half
major_progression = [1, 1, .5, 1, 1, 1, .5]
# whole, half, whole, whole, half, whole, whole
minor_progression = [1, .5, 1, 1, .5, 1, 1]


def rotate(arr, n):
    return arr[n:] + arr[:n]


def create_scale(note, steps):
    # create 12-tone starting with start note
    note_index = notes.index(note)
    chromatic = notes[note_index:] + notes[:note_index] + [notes[note_index]]
    # turn steps into indices
    # indices = [0, 2, 4, 5, 7, 9, 11, 12]
    indices = [0]
    for s in steps:
        indices.append(int(indices[-1] + 2 * s))
    scale = [chromatic[i] for i in indices]
    return scale


def create_chromatic(note):
    note_index = notes.index(note)
    chromatic = notes[note_index:] + notes[:note_index]
    return chromatic


def create_guitar():
    return [
        create_chromatic('E '),
        create_chromatic('B '),
        create_chromatic('G '),
        create_chromatic('D '),
        create_chromatic('A '),
        create_chromatic('E '),
    ]


def filter_guitar(guitar, notes):
    # replace all notes not in notes with ' '
    for i, s in enumerate(guitar):
        for j, n in enumerate(s):
            if n not in notes:
                guitar[i][j] = '  '
    return guitar


def print_guitar(guitar, root=None):
    print('-' * 70)
    for s in guitar:
        for l in s:
            if l == root:
                # v = str(colored(255, 0, 0, l)).strip()
                v = colored(l, RED)
            else:
                v = colored(l)
            print("{0:^4}".format(v), end='')
            print("{0:^4}".format('|'), end='')
        print()
    print('-' * 70)
    for i in range(12):
        print("{0:<6}".format(str(i)), end='')
        # print("{0:^4}".format(' '), end='')
    print()


def colored(text, color='39m'):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text
    #
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def get_chords(scale):
    return [get_chord(scale, n) for n in scale]


def get_chord(scale, root=None):
    # rotate scale to root
    if root:
        scale = rotate(scale[:-1], scale.index(root))
    return [scale[i] for i in [0, 2, 4]]


def print_chords(chords):
    d = ['   I', '  ii', ' iii', '  IV', '   V', '  vi', 'viiº']
    for i in range(len(chords) - 1):
        print(f'{d[i]}: {chords[i]}')


def highlight_notes(guitar, notes):
    for i, s in enumerate(guitar):
        for j, n in enumerate(s):
            if n in notes:
                guitar[i][j] = colored(n, color=RED)
    return guitar


def get_pentatonic(scale):
    return [scale[i] for i in [0, 1, 2, 4, 5]]


BLUE = '34m'
RED = '31m'
print_guitar(create_guitar())
# all c major info
c_scale = create_scale('C ', major_progression)
am_scale = create_scale('A ', minor_progression)
c_guitar = filter_guitar(create_guitar(), c_scale)
c_major_chords = get_chords(c_scale)
c_major_pentatonic = get_pentatonic(c_scale)

print_guitar(c_guitar, 'C ')
print_chords(c_major_chords)
print(f'{c_major_pentatonic}')
print_guitar(highlight_notes(c_guitar, get_chord(c_scale)))
print_guitar(filter_guitar(create_guitar(), get_chord(c_scale)))
print_guitar(highlight_notes(c_guitar, c_major_pentatonic))
print_guitar(filter_guitar(create_guitar(), c_major_pentatonic))
