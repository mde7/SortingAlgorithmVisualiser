import algorithms as algo
import sys, time
import pygame

##############
# ALGORITHMS #
##############

algorithms = {
    "SelectionSort" : algo.SelectionSort(),
    "BubbleSort": algo.BubbleSort()
}

#################
# GAME SETTINGS #
#################

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

###########
# COLOURS #
###########

WHITE = (255, 255, 255)  # Initial page
PURPLE = (190, 65, 190)  # Array ith value
BLUE = (0,0,255)  # Sorted ith value
GREEN = (0, 255, 0)  # Sorting ith value

##################
# IMPLEMENTATION #
##################

def draw_window(window=WIN, width=WIDTH, algorithm=None, swap1=None, swap2=None):
    window.fill(WHITE)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}   Time: {time.time() - algorithm.start_time:.1f}    Status: Sorting")
    block_size = width//len(algorithm.array)
    for _ in range(len(algorithm.array)):
        block_colour = PURPLE
        if algorithm.array[_] == swap1:
            block_colour = BLUE
        elif algorithm.array[_] == swap2:
            block_colour = GREEN
        pygame.draw.rect(window, block_colour, (_*block_size, width - algorithm.array[_], block_size, algorithm.array[_]))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

def draw_final_window(window, algorithm, time):
    pygame.display.set_caption(f"Algorithm: {algorithm.name}   Time: {time:.1f}    Status: Sorted")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


def main(window, width):
    if len(sys.argv) <=1:
        print("Please enter the sorting algorithm")
    if len(sys.argv) >2:
        print("Too many arguements, please enter in the format of: python3 algo_vis.py SortingAlgorithm")
    algorithm_name = sys.argv[1]
    if algorithm_name in algorithms:
        algorithm = algorithms[algorithm_name]
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    time = algorithm.execute()
                    draw_final_window(window, algorithm, time)
    else:
        print("Please enter a valid sorting algorithm")
            

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH)