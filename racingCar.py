import gym
import universe
import random

def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    #For every 15 iterations, sum the total obsevations and take the avg
    #if avg is lower than 0, change the direction
    if(j >= 15):
        if(total_sum/j == 0):
            turn = True
        else:
            turn = False

        total_sum = 0
        j =0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False

    if(observation_n != None):
        j += 1
        total_sum += reward_n
    return (turn, total_sum, prev_total_sum)


def main():
    #Initialise the environment
    env = gym.make('flashames.CoasterRacer-v0')
    observation_n = env.reset()   #observation_n is an array of n environment initialization, Here it is only one

    #no of game iterations
    n = 0
    j = 0

    total_sum = 0
    prev_total_sum = 0
    turn = False

    #define our turns
    left = [('KeyEvent',"ArrowUp", True), ('KeyEvent',"ArrowLeft", True),('KeyEvent',"ArrowRight", False)]
    right = [('KeyEvent',"ArrowUp", True), ('KeyEvent',"ArrowLeft", False),('KeyEvent',"ArrowRight", True)]
    forward = [('KeyEvent',"ArrowUp", True), ('KeyEvent',"ArrowLeft", False),('KeyEvent',"ArrowRight", False)]

    while True:
        n += 1

        if(n > 1):

            if(observation_n[0] != None):
                prev_score = reward_n[0]

                #1.Should we turn
                if(turn):
                    #2. Where to turn
                    event = random.choice([left, right])
                    action_n = [event for ob in observation_n]

                    turn = False #Set turn to false as we have already turned
                else:
                    #If turn is false then go straight
                    action = [forward for ob in observation_n]

                if(observation_n[0] != None):
                    turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

                observation_n, revard_n, done_n, info = env.step(action_n)
                env.render()

if __name__ == '__main__':
    main()
