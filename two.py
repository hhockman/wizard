#!/usr/bin/python3
import logging,os
logger = logging.getLogger()
logger.debug('you found two')

class Player:
    def __init__(self,name,ordinal):
        self.name = name
        self.ordinal = ordinal
        self.score = 0
        self.bid = 0
        self.actual = 0
        self.behind = 0
        self.dealer = False

p1 = Player('Bob',1)
p2 = Player('Donna',2)
p3 = Player('Harold',3)
p4 = Player('Cathy',4)
p5 = Player('Terry',5)
p6 = Player('Will',6)

players = (p1,p2,p3,p4,p5,p6)

def isDealer(p):
    if p.dealer:
        return('>>>> ')
    return('     ')

def showScore():
    global players
    os.system('clear')
    print('WIZARD SCORE CARD *************************************')
    print('ROUND '+str(round)+ ' of '+str(rounds))
    print('DEAL NAME----------- Score  Bid Actual Behind')
    for p in players:
        print(isDealer(p)+p.name.ljust(15,'.'),str(p.score).rjust(5,' '),str(p.bid).rjust(3,' '),str(p.actual).rjust(7,' '),str(p.behind).rjust(6,' '))

def getHand():
    global players
    global whosfirst
    global dealer
    aryR = []
    num = len(players)
    x = dealer + 1
    if dealer == num:
        x = 0
    for i in range(num):
        print(i,x)
        aryR.append(x)
        x += 1
        if x == num:
            x = 0
    print(aryR,i,x)
    return aryR

def getBids(porder):
    global players
    bids = 0
    # os.system('clear')
    #for p in players:
    for x in porder:
        #print ('Round: ' + str(round) + '  Bids: ' + str(bids))
        prompt = 'BIDS:'+ str(bids)+'  Bid for ' + players[x].name + ' :'
        bidkey = input(prompt)
        if bidkey == '':
            bidkey = 0
        players[x].bid = bidkey
        bids += int(players[x].bid)

def scoreRound(round,porder):
    global players
    global dealer
    hands = []
    for x in porder:
        prompt = players[x].name+' bid ' + str(players[x].bid) + ' enter actual take: '
        if sum(hands) < round:
            hand = input(prompt)
        else:
            hand = 0
        if hand == '': # just enter equates to zero
            hand = 0
        hands.append(int(hand))
        #p.score += scoreHand(hand,p.bid)
    i=0
    for x in porder:
        print('Player: '+players[x].name+' Bid: '+str(players[x].bid)+' Took: '+str(hands[i]))
        i += 1
    confirmkey = input('press E to edit or ENTER to confirm')
    if confirmkey.upper() == 'E':
        scoreRound(round,porder)
    i=0
    max = 0
    for x in porder: #score hand and advance dealer
        players[x].score += scoreHand(hands[i],players[x].bid)
        players[x].actual = hands[i]
        if players[x].score > max:
            max = players[x].score
        players[x].dealer = False
        i += 1
    if dealer + 1 == len(players):
        dealer = 0
    else:
        dealer += 1
    for p in players: # calculate behind
        p.behind = max - p.score

def scoreHand(hand, bid):
    if str(hand) == '':
        hand = bid
    if str(bid) == '' or type(bid) == str():
        bid = 0
    hand = int(hand)
    bid = int(bid)
    if hand == bid:
        score = 20 + (int(bid) * 10)
    print(type(hand),type(bid),hand,bid)
    if hand < bid:
        score = -10 * (int(bid) - int(hand))
    if hand > bid:
        score = -10 * (int(hand) - int(bid))
    return score

rounds = 10
dealer = 3
whosfirst = 6
for round in range(1,rounds+1):
    players[dealer].dealer = True
    showScore()
    porder = getHand()
    getBids(porder)
    showScore()
    scoreRound(round,porder)
    showScore()
    #input('Press Enter to continue...')


