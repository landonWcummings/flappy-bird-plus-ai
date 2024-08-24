from flap import Game
import pygame
import neat
import os
import time
import pickle

class flapGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.ball = self.game.ball
        self.pipes = self.game.pipes
        self.score = self.game.score

    def play(self, config):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game.ball.flap()
            
            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()

    
    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            output = net.activate((self.ball.y, self.pipes.mid(self.ball.x)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.ball.flap()

            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()

        pygame.quit()
    
    def train_ai(self, genome1, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        


        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate((self.ball.y, self.pipes.mid(self.ball.x)))
            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 ==1:
                self.game.ball.flap()



            game_info = self.game.loop()
            self.game.draw()
            pygame.display.update()

            if self.game.score >= 300 or self.game.tries > 0:
                self.calculate_fitness(genome1)
                break

    def calculate_fitness(self, genome1):
        genome1.fitness += self.game.score
        





def eval_genomes(genomes, config):
    width, height = 600, 600
    window = pygame.display.set_mode((width,height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        genome1.fitness = 0
        if i == len(genomes) -1:
            break
        
        game = flapGame(window, width, height)
        game.train_ai(genome1, config)
        





def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpiont-12')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)

    with open("best.pickle", "wb" ) as f:
        pickle.dump(winner, f)

    best_genome = stats.best_genome()
    print("\nBest Genome:\n", best_genome)



def test_ai(config):
    width, height = 600, 600
    window = pygame.display.set_mode((width,height))
    with open("best.pickle", "rb" ) as f:
        winner = pickle.load(f)

    game = flapGame(window,width,height)
    game.test_ai(winner, config)
        
    


    

if __name__ == '__main__':
    width, height = 600, 600
    window = pygame.display.set_mode((width,height))

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
   
    #game = flapGame(window,width,height)
    #game.play(config)

    run_neat(config)
    test_ai(config)


