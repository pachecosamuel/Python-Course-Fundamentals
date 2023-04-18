def music_notes():
    yield 'Dó'
    yield 'Ré'
    yield 'Mi'
    yield 'Fá'
    yield 'Sol'
    yield 'Lá'
    yield 'Si'

gen = music_notes()

[print(note) for note in gen]