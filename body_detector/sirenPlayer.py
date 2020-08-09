import pygame

pygame.init()
pygame.mixer.init()

def playSiren():
    if pygame.mixer.music.get_busy() == False:
        print('playing')    
        pygame.mixer.music.load('siren.wav')
        pygame.mixer.music.play()    
    else:
        pass
