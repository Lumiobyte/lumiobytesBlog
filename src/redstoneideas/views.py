from django.shortcuts import render
import random

def viewIdea(request):
    template = "redstoneideas/detail.html"

    encourageMessageList = [
        'How about you try this one...!',
        'Give it a go - I\'m sure you\'ll manage eventually!',
        'Aww cmon, it\'s probably not as hard as you think!',
        'I bet you can\'t build this!',
        'Have some fun!',
        'Enjoy building that...',
        'I dare you to do this one in under an hour. Time starts now!',
        'I know you\'re terrible at redstone... I won\'t judge. No pressure!',
    ]

    encourageMessage = random.choice(encourageMessageList)
    
    if random.randint(1, 4) == 2:
        adjectives = [
            'Colourful', 
            'Compact',
            'Big',
            'Tiny',
            'Bright',
            'Flashing',
            'Simple',
            'Complex'
            'Hidden',
            'Secret',
            'Ugly',
        ]

        size = [
            '2x2',
            '3x3', 
            '4x4', 
            '5x5', 
            '6x6',
            '7x7',
            '8x8',
            '9x9',
            '10x10'
            '2 high',
            '3 high',
            '4 high',
            '5 high',
            '6 high',
            '7 high',
            '8 high',
            '9 high',
            '10 high',
            '2 wide',
            '3 wide',
            '4 wide',
            '5 wide',
            '6 wide',
            '7 wide',
            '8 wide',
            '9 wide',
            '10 wide',
        ]

        location = [
            'on a mountain',
            'underwater',
            'underground',
            'in a secret lair',
            'out in the open',
            'in your redstone world',
            'in a castle',
            'in a little cottage',
        ]

        idea = random.choice(adjectives) + " " + random.choice(size) + " piston door " + random.choice(location) + "!"

    else:
        adjectives = [
            'Colourful',
            'Automated',
            'Useful',
            'Huge',
            'Big',
            'Small',
            'Tiny',
            'Wide',
            'High',
            'Multi-leveled',
            'Bright',
            'Flashing',
            'Epilepsy-inducing',
            'Laggy',
            'Game-crashingly laggy'
            'Hidden', 
            'Secret',
            'Ugly',
        ]

        ideaThingsToBuild1 = [
            'lighthouse',
            'sugarcane',
            'mob',
            'iron golem',
            'item', 
            'house',
            'piston door',
            'farm',
        ]
        ideaThingsToBuild2 = [
            'farm',
            'elevator',
            'harvester',
            'mover',
            'mover flying-machine',
            'house',
        ]
        ideaBuildWhere = [
            'on a mountain',
            'underwater',
            'underground',
            'in a secret lair',
            'out in the open',
            'in your redstone world',
            'in the air',
            'on an airplane',
            'that pops out of the ground',
            'that is launched from a flying machine that flies out of a cliff face'
        ]

        idea = random.choice(adjectives) + " " + random.choice(ideaThingsToBuild1) + " " + random.choice(ideaThingsToBuild2) + " " + random.choice(ideaBuildWhere) + "!"

    return render(request, template, {'encourageMessage': encourageMessage, 'idea': idea})
