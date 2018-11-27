import MemeGetter

# CONSTANTS
SOURCES_FILE = 'sources.dat'

def get_sources():
    with open(SOURCES_FILE, 'r') as f:
        return f.read().splitlines()

if __name__ == '__main__':
    all_memes = []
    sources = get_sources()
    sources = filter(str.strip, sources)

    for s in sources:
        mg = MemeGetter.MemeGetter(s)
        memes = mg.downloadMemes()
        print(s + ': ' + str(len(memes)))

        all_memes += memes

    MemeGetter.register_memes(all_memes)
