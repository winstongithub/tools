import sys
import pygame.mixer

if __name__ == '__main__':
    pygame.mixer.init()
    if len(sys.argv) > 1:
        music_name = sys.argv[1]
        pygame.mixer.music.load(sys.argv[1])
        pygame.mixer.music.play()
        
    while True:
        opt = raw_input('play  pause   unpause    close\n')
        cmd = opt.strip(' ')
        if cmd == 'pause':
            pygame.mixer.music.pause()
            continue
        elif cmd == 'unpause':
            pygame.mixer.music.unpause()
            continue
        elif cmd == 'close':
            exit()
        elif cmd=='play':
            rawname = raw_input('input music name')
            name = rawname.strip(' ')
            pygame.mixer.music.load(name)
            pygame.mixer.music.play()
            continue
        print cmd , 'wrong command'
    
