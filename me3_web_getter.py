import meme_getter
import me3.core.me3_persistence as me3_persistence

# CONSTANTS
SOURCES_FILE = 'meme_sources.dat'
MEMES_FILE = 'StuffMemes.dat'

def get_sources():
    with open(SOURCES_FILE, 'r') as f:
        return f.read().splitlines()

if __name__ == '__main__':
    all_memes = []
    sources = get_sources()
    sources = filter(str.strip, sources)

    for s in sources:
        mg = meme_getter.MemeGetter(s)
        memes = mg.downloadMemes()
        print(s + ': ' + str(len(memes)))

        all_memes += memes

    me3_persistence.register_memes(all_memes, MEMES_FILE)
