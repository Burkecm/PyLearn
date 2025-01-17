bids = {}
moreBidders = True

def findHighestbidder(bids):        
    highestBidder = ""
    maxBid = 0
    for key in bids:
        bid = bids[key]
        if bid > maxBid:
            highestBidder = key
            maxBid = bid

    print(f"{highestBidder} is the winner with a bid of ${bids[highestBidder]}!")

while moreBidders == True:
    bidderName = input("What is your name, bidder?: ")
    bid = int(input("What is your bid?: $"))
    bids[bidderName] = bid
    if input("Are there any more bidders? y/n: ") == "n":
        moreBidders = False

findHighestbidder(bids)