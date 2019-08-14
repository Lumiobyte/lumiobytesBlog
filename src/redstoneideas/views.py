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
        'I know you\'re terrible at redstone... I won\'t judge. No pressue!',
    ]

    encourageMessage = random.choice(encourageMessageList)

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
