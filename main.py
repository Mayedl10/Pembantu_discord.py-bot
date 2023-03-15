#IMPORTANT!
#BEFORE USING THE SHOP, USE THE COMMAND "setup"









import os
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from itertools import cycle
import json
import random
import asyncio
import this
print()

temp_user_id = ""
user__ = ""

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True




print("https://www.youtube.com/watch?v=vQw8cFfZPx0&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=7")
print("https://www.youtube.com/watch?v=q6PTrZeozBg&list=PLoFvxwcEPSPhCNdel2XcNgbgmntp4E-CE&index=3")
print()
print("https://discordpy.readthedocs.io/en/latest/")
print()
print("https://discord.com/developers/applications/1006243990934405130/oauth2/url-generator")
print()
print("Starting up Pembantu")

client = commands.Bot(command_prefix = "?", intents=intents)
client.remove_command('help')
status = cycle(["Minecraft", "Roblox", "Yo-Kai Watch"])

with open(os.path.join("assets", "mainshop.json"), "r")as f:
    data_shop = json.load(f)

mainshop = data_shop


#misc functions
@client.command()
async def setup(ctx):
    try:

        guild = ctx.guild
        await ctx.send("Creating shop roles...")

        await guild.create_role(name="Netherite",color = discord.Color.purple())
        await ctx.send("1/4")

        await guild.create_role(name="Diamond",color = discord.Color.blurple())
        await ctx.send("2/4")

        await guild.create_role(name="Gold",color = discord.Color.gold())
        await ctx.send("3/4")

        await guild.create_role(name="Copper",color = discord.Color.orange())
        await ctx.send("4/4")
        await ctx.send("Shop roles created...")
        
        await ctx.send("Setup finished successfully!")
        await ctx.send("Please DO NOT use this command again!")
    
    except:
        await ctx.send("Setup failed")

        
###
@client.command(aliases = ["dog","doggo","Doggo"])
async def Dog(ctx):
    filenames = os.listdir(os.path.join("assets","Dogs"))
    selected_file = random.choice(filenames)
    await ctx.send("Here's a cute doggo ^-^", file=discord.File(os.path.join("assets",os.path.join("Dogs",selected_file))))

                           



###

        
#debug commands
@client.command(hidden=True)
async def debug_shopdata(ctx):
    await ctx.send(mainshop)

#events and tasks
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Python"))
    change_status.start()
    print("Pembantu is online")

@tasks.loop(seconds = 30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command doesn't exist -_-")
    if isinstance(error, commands.CommandOnCooldown):
        msg = "This command is still cooling down. Try again in {:.0f} seconds".format(error.retry_after)
        await ctx.send(msg)    

#commands
@client.command(pass_context = True, hidden = True)
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, user : discord.Member, *, role : discord.Role):
    if role in user.roles:
        await ctx.send(f"{user.mention} already has that role")
    else:
        await user.add_roles(role)
        await ctx.send("Role was successfully added")
        




        
@client.command(hidden=True)
async def spam(ctx):
    reps = int(10)
    while not(reps <= 0):
        await ctx.send("WOOOOOOOOOOOOOOOO SPAM TIME!")
        reps = int(reps - 1)



@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@load.error
async def load_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")


@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@unload.error
async def unload_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")

@client.command()
async def ping(ctx):#if prefix + ping is written
    await ctx.send(f"Pong {round(client.latency * 1000)}ms")#the bot sends "Pong"

@ping.error
async def ping_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")

@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain", "Maybe","Yes", "No", "Most likely", "Very doubtful.", "Don't count on it", "Try again"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@_8ball.error
async def _8ball_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=1):
    await ctx.channel.purge(limit = amount + 1)

@purge.error
async def purge_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")

@client.command(hidden=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked user {member.mention}')

@kick.error
async def kick_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")

@client.command(hidden=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned user {member.mention}')

@ban.error
async def ban_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")


@client.command(hidden=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban_error(ctx, error):
    await ctx.send("You made a mistacke lol stupid")


@client.command()
async def help(ctx):
        file_r = open(os.path.join("assets", "help_cmd.txt"))
        content_list = file_r.readlines()
        file_r.close()

        file_r = open(os.path.join("assets", "help_cmd.txt"))
        content_r = file_r.read()
        await ctx.send(content_r)
        file_r.close()

@client.command()
async def help_economy(ctx):
        file_r = open(os.path.join("assets", "help_eco.txt"))
        content_list = file_r.readlines()
        file_r.close()

        file_r = open(os.path.join("assets", "help_eco.txt"))
        content_r = file_r.read()
        await ctx.send(content_r)
        file_r.close()


#economy commands
@client.command(aliases = ["Balance","Bal","bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    
    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await ctx.send(embed = em)

@client.command(aliases = ["Work"])
@commands.cooldown(1, 3600, commands.BucketType.user) # 1 time per 60 seconds
async def work(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(101)
    await ctx.send(f"You earned {earnings} coins!")
    users[str(user.id)]["bank"] += earnings
    with open(os.path.join("assets", "mainbank.json"), "w") as f:
        json.dump(users,f)
    
@client.command(aliases = ["Withdraw"])
async def withdraw(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Stupid. You can't withdraw nothing!")
        return
    bal = await update_bank(ctx.author)


    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("LOL IMAGINE BEING THIS POOR XD")
        await ctx.send("You don't have that much in your bank account...")
        return
    if amount < 0:
        await ctx.send("You can't withdraw negative money °_°")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "bank")
    await ctx.send(f"You withdrew {amount} coins from your bank account!")


@client.command(aliases = ["Deposit"])
async def deposit(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Stupid. You can't deposit nothing!")
        return
    bal = await update_bank(ctx.author)


    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("LOL IMAGINE BEING THIS POOR XD")
        await ctx.send("You don't have that much in your wallet...")
        return
    if amount < 0:
        await ctx.send("You can't deposit negative money °_°")
        return

    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount, "bank")
    await ctx.send(f"You deposited {amount} coins in your bank account!")



async def open_account(user):
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open(os.path.join("assets", "mainbank.json"), "w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open(os.path.join("assets", "mainbank.json"), "r")as f:
        users = json.load(f)
    return users

@client.command()
async def debug_bankdata(ctx):
    users = await get_bank_data()
    await ctx.send(users)


async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()
    
    users[str(user.id)][mode] += change

    with open(os.path.join("assets", "mainbank.json"), "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal
        

@client.command(aliases = ["Shop"])
async def shop(ctx):
    em = discord.Embed(title = "Shop", color = discord.Color(0xfa43ee))

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"Price: {price} | {desc}")

    await ctx.send(embed = em)

@client.command()
async def refresh(ctx):
    await setup()


    ctx.send(f"Refreshed bot")


        





@client.command(aliases = ["Buy"])
async def buy(ctx,item,amount = 1):
    user_ = ctx.author

            
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)
    

    if not res[0]:
        if res[1]==1:
            await ctx.send("That item doesn't exist :skull:")
            return
        if res[1]==2:
            await ctx.send("You don't have enough money :skull:")
            return


    await ctx.send(f"WOO YOU DID IT! YOU BOUGHT {amount} {item}! POG")


@client.command(aliases = ["Bag"])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title = "Bag", color = discord.Color(0xfa43ee))
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)

    await ctx.send(embed = em)




    
async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    if name_ == None:
        return[False,1]
    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]



    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name, "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name, "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open(os.path.join("assets", "mainbank.json"), "w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]



@client.command(hidden = True)
async def role_c(ctx, name_v = "Name"):
    print("started")
    guild = ctx.guild
    await guild.create_role(name=name_v, color=discord.Color.gold())
    print("done")



@client.command(aliases = ["Sell"])
async def sell(ctx,item,amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount) #add another attribute after amount to get a use cmd (it would then look like ...amount,0) it has to be 0 and replace amount with 1

    if not res[0]:
        if res[1]==1:
            await ctx.send("This item doesn't exist :pepeclown:")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item}...")
            return
        if res[1]==3:
            await ctx.send(f"YOU DON'T EVEN OWN ONE {item}!")
            return

    await ctx.send(f"You sold {amount} {item}! POG!")

async def sell_this(user,item_name,amount,price = None): #if i want a ?use command i set price here to 0
    item_name = item_name.lower()
    name = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = item["price"]
            break
        
    if name_ == None:
        return [False,1]

    cost = price*amount
    users = await get_bank_data()
    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False,3]
    except:
        return[False,3]

    with open(os.path.join("assets", "mainbank.json"), "w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

@client.command(hidden=True)
async def hack_bank(ctx,amt = 0):
    await update_bank(ctx.author,amt)


@client.command(aliases=[":("])
async def cheer_me_up(ctx):
    listtttt = ["You look nice today!","I like you!","I wish I was your friend!","Everybody likes you!","You look nice today!","I like you!","I wish I was your friend!","Everybody likes you!","You look nice today!","I like you!","I wish I was your friend!","Everybody likes you!","You look nice today!","I like you!","I wish I was your friend!","Everybody likes you!","You look nice today!","I like you!","I wish I was your friend!","Everybody likes you!",":("]
    temp = random.choice(listtttt)
    await ctx.send(temp)
#############################################################################################################################################################################################
#TETRIS######################################################################################################################################################################################
#############################################################################################################################################################################################
board = []
num_of_rows = 18
num_of_cols = 10
empty_square = ':black_large_square:'
blue_square = ':blue_square:'
brown_square = ':brown_square:'
orange_square = ':orange_square:'
yellow_square = ':yellow_square:'
green_square = ':green_square:'
purple_square = ':purple_square:'
red_square = ':red_square:'
embed_colour = 0x077ff7 #colour of line on embeds
points = 0
lines = 0 #how many lines cleared
down_pressed = False #if down button has been pressed
rotate_clockwise = False
rotation_pos = 0
h_movement = 0 #amount to move left or right
is_new_shape = False
start_higher = False #for when near top of board
game_over = False
index = 0

class Tetronimo: #Tetris pieces
    def __init__(self, starting_pos, colour, rotation_points):
        self.starting_pos = starting_pos #list
        self.colour = colour
        self.rotation_points = rotation_points #list

main_wall_kicks = [ #for J, L, T, S, Z tetronimos
                    [[0, 0], [0, -1], [-1, -1], [2, 0], [2, -1]],
                    [[0, 0], [0, 1], [1, 1], [-2, 0], [-2, 1]],
                    [[0, 0], [0, 1], [-1, 1], [2, 0], [2, 1]],
                    [[0, 0], [0, -1], [1, -1], [-2, 0], [-2, -1]]
                    ]

i_wall_kicks = [ #for I tetronimo
                [[0, 0], [0, -2], [0, 1], [1, -2], [-2, 1]],
                [[0, 0], [0, -1], [0, 2], [-2, -1], [1, 2]],
                [[0, 0], [0, 2], [0, -1], [-1, 2], [2, -1]],
                [[0, 0], [0, 1], [0, -2], [2, 1], [-1, -2]]
                ]

rot_adjustments = { #to move when rotations are slightly off
                #blue: not sure if needs any rn
                ':blue_square:': [[0, 1], [-1, -1], [0, 0], [-1, 0]], #[[0, 0], [0, 0], [0, 0], [0, 0]]
                #brown: left 1, right 1, right 1, left 1,
                ':brown_square:': [[0, 0], [0, 1], [0, 0], [0, -1]], #[[0, -1], [0, 1], [0, 1], [0, -1]]'
                #orange: left 1, nothing, right 1, nothing
                ':orange_square:': [[0, -1], [0, 0], [-1, 1], [0, 0]], #[[0, -1], [0, 0], [0, 1], [0, 0]]
                #none for yellow
                ':yellow_square:': [[0, 0], [0, 0], [0, 0], [0, 0]],
                #green: right 1, nothing, right 1, nothing
                ':green_square:': [[0, 0], [0, 0], [0, 0], [0, 0]], #[[0, 1], [0, 0], [0, 1], [0, 0]]
                #purple: nothing, right 1, left 1 (possibly up too), right 1
                ':purple_square:': [[0, 0], [1, 1], [0, -1], [0, 1]], #[[0, 0], [0, 1], [0, -1], [0, 1]]
                #red: left 1, up 1, right 1, up 1
                ':red_square:': [[1, -1], [-1, -1], [0, 2], [-1, -1]] #[[0, -1], [-1, 0], [0, 1], [-1, 0]]
                }

#starting spots, right above the board ready to be lowered. Col is 3/4 to start in middle
shape_I = Tetronimo([[0, 3], [0, 4], [0, 5], [0, 6]], blue_square, [1, 1, 1, 1])
shape_J = Tetronimo([[0, 3], [0, 4], [0, 5], [-1, 3]], brown_square, [1, 1, 2, 2])
shape_L = Tetronimo([[0, 3], [0, 4], [0, 5], [-1, 5]], orange_square, [1, 2, 2, 1])
shape_O = Tetronimo([[0, 4], [0, 5], [-1, 4], [-1, 5]], yellow_square, [1, 1, 1, 1])
shape_S = Tetronimo([[0, 3], [0, 4], [-1, 4], [-1, 5]], green_square, [2, 2, 2, 2])
shape_T = Tetronimo([[0, 3], [0, 4], [0, 5], [-1, 4]], purple_square, [1, 1, 3, 0])
shape_Z = Tetronimo([[0, 4], [0, 5], [-1, 3], [-1, 4]], red_square, [0, 1, 0, 2])


#fill board with empty squares
def make_empty_board():
    for row in range(num_of_rows):
        board.append([])
        for col in range(num_of_cols):
            board[row].append(empty_square)

def fill_board(emoji):
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            if board[row][col] != emoji:
                board[row][col] = emoji


def format_board_as_str():
    board_as_str = ''
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            board_as_str += (board[row][col]) # + " " possibly
            if col == num_of_cols - 1:
                board_as_str += "\n "
    return board_as_str

def get_random_shape():
    global index
    # ordered_shapes = [shape_J, shape_T, shape_L, shape_O, shape_S, shape_Z, shape_S, shape_T, shape_J, shape_Z, shape_S, shape_I, shape_Z, shape_O, shape_T, shape_J, shape_L, shape_Z, shape_I]
    # random_shape = ordered_shapes[index]
    shapes = [shape_I, shape_J, shape_L, shape_O, shape_S, shape_T, shape_Z]
    random_shape = shapes[random.randint(0, 6)] #0, 6
    index += 1
    if start_higher == True:
        for s in random_shape.starting_pos[:]: #for each square
            s[0] = s[0] - 1 #make row 1 above
    else:
        starting_pos = random_shape.starting_pos[:]
    random_shape = [random_shape.starting_pos[:], random_shape.colour, random_shape.rotation_points] #gets starting point of shapes and copies, doesn't change them
    global is_new_shape
    is_new_shape = True
    return random_shape #returns array with starting pos and colour

def do_wall_kicks(shape, old_shape_pos, shape_colour, attempt_kick_num):
    new_shape_pos = []

    if shape_colour == blue_square:
        kick_set = main_wall_kicks[rotation_pos]
    else:
        kick_set = i_wall_kicks[rotation_pos]

    for kick in kick_set:
        for square in shape:
            square_row = square[0]
            square_col = square[1]
            new_square_row = square_row + kick[0]
            new_square_col = square_col + kick[1]
            if (0 <= new_square_col < num_of_cols) and (0 <= new_square_row < num_of_rows): #if square checking is on board
                square_checking = board[new_square_row][new_square_col] #get the square to check if empty
                if (square_checking != empty_square) and ([new_square_row, new_square_col] not in old_shape_pos): #if square is not empty / won't be when other parts of shape have moved
                    #shape doesn't fit
                    new_shape_pos = [] #reset new_shape
                    break
                else: #shape does fit
                    new_shape_pos.append([new_square_row, new_square_col]) #store pos
                    if len(new_shape_pos) == 4:
                        return new_shape_pos #return shape with kicks added
            else:
                #shape doesn't fit
                new_shape_pos = [] #reset new_shape
                break

    return old_shape_pos #return shape without rotation


def rotate_shape(shape, direction, rotation_point_index, shape_colour):
    rotation_point = shape[rotation_point_index] #coords of rotation point
    new_shape = [] #to store coords of rotated shape

    #Rotate shape
    for square in shape:
        square_row = square[0]
        square_col = square[1]
        if direction == 'clockwise':
            new_square_row = (square_col - rotation_point[1]) + rotation_point[0] + rot_adjustments.get(shape_colour)[rotation_pos-1][0]
            new_square_col = -(square_row - rotation_point[0]) + rotation_point[1] + rot_adjustments.get(shape_colour)[rotation_pos-1][1]
        elif direction == 'anticlockwise': #currently not a thing
            new_square_row = -(square_col - rotation_point[1]) + rotation_point[0]
            new_square_col = (square_row - rotation_point[0]) + rotation_point[1]
        new_shape.append([new_square_row, new_square_col]) #store pos of rotated square
        if (0 <= square_col < num_of_cols) and (0 <= square_row < num_of_rows): #if on board
            board[square_row][square_col] = empty_square #make empty old square pos

    new_shape = do_wall_kicks(new_shape, shape, shape_colour, 0) #offset shape

    new_shape = sorted(new_shape, key=lambda l:l[0], reverse=True) #sort so that bottom squares are first in list

    #Place rotated shape (in case can't move down)
    if new_shape != shape: #if not same as old unrotated shape (in case places at start pos)
        for square in new_shape:
            square_row = square[0]
            square_col = square[1]
            board[square_row][square_col] = shape_colour

    return new_shape

def clear_lines():
    global board
    global points
    global lines
    lines_to_clear = 0
    for row in range(num_of_rows):
        row_full = True #assume line is full
        for col in range(num_of_cols):
            if board[row][col] == empty_square:
                row_full = False
                break #don't clear this row
        if row_full: #if line to clear
            lines_to_clear += 1
            #bring all lines above down
            board2 = board[:] #clone board
            for r in range(row, 0, -1): #for every row above row
                if r == 0: #if top row
                    for c in range(num_of_cols):
                        board2[r][c] = empty_square #make each spot empty
                else:
                    for c in range(num_of_cols):
                        board2[r][c] = board[r - 1][c] #make each spot the one above
            board = board2[:]
    if lines_to_clear == 1:
        points += 100
        lines += 1
    elif lines_to_clear == 2:
        points += 300
        lines += 2
    elif lines_to_clear == 3:
        points += 500
        lines += 3
    elif lines_to_clear == 4:
        points += 800
        lines += 4


def get_next_pos(cur_shape_pos):
    global h_movement
    global start_higher
    global game_over

    #Check if new pos for whole shape is available
    movement_amnt = 1

    if down_pressed == False:
        amnt_to_check = 1 #check space one below
    else:
        amnt_to_check = num_of_rows #check all rows until furthest available space

    for i in range(amnt_to_check):
        square_num_in_shape = -1
        for square in cur_shape_pos:
            next_space_free = True
            square_num_in_shape += 1
            square_row = square[0]
            square_col = square[1]
            if (0 <= square_col < num_of_cols): #if current column spot will fit
                if not (0 <= square_col + h_movement < num_of_cols): #if spot with column position changed won't fit
                    h_movement = 0 #just change row position
                if (0 <= square_row + movement_amnt < num_of_rows): #if new square row pos is on board
                    square_checking = board[square_row + movement_amnt][square_col + h_movement] #get the square to check if empty
                    if (square_checking != empty_square) and ([square_row + movement_amnt, square_col + h_movement] not in cur_shape_pos): #if square is not empty / won't be when other parts of shape have moved
                        #check if space free if not moving horizontally (in case going into wall) but still going down
                        h_movement = 0
                        square_checking = board[square_row + movement_amnt][square_col + h_movement]
                        if (square_checking != empty_square) and ([square_row + movement_amnt, square_col + h_movement] not in cur_shape_pos):
                            if movement_amnt == 1:
                                next_space_free = False #can't put shape there
                                if is_new_shape: #if can't place new shape
                                    if start_higher == True:
                                        game_over = True
                                    else:
                                        start_higher = True
                            elif movement_amnt > 1: #if sending down
                                movement_amnt -= 1 #accomodate for extra 1 added to check if its free
                            return [movement_amnt, next_space_free] #stop checking
                    elif down_pressed == True:
                        if square_num_in_shape == 3: #only on last square in shape
                            movement_amnt += 1 #increase amount to move shape by
                elif square_row + movement_amnt >= num_of_rows: #new square row isn't on board
                    if movement_amnt == 1:
                        next_space_free = False #can't put shape there
                    elif movement_amnt > 1: #if sending down
                        movement_amnt -= 1 #accomodate for extra 1 added to check if its free
                    return [movement_amnt, next_space_free] #stop checking
                elif down_pressed == True:
                    if square_num_in_shape == 3: #only on last square in shape
                        movement_amnt += 1 #increase amount to move shape by

    return [movement_amnt, next_space_free]


async def run_game(msg, cur_shape):
    global is_new_shape
    global h_movement
    global rotate_clockwise
    global rotation_pos

    cur_shape_pos = cur_shape[0]
    cur_shape_colour = cur_shape[1]

    if rotate_clockwise == True and cur_shape_colour != yellow_square:
        cur_shape_pos = rotate_shape(cur_shape_pos, 'clockwise', cur_shape[2][rotation_pos], cur_shape_colour) #rotate shape
        cur_shape = [cur_shape_pos, cur_shape_colour, cur_shape[2]] #update shape

    next_pos = get_next_pos(cur_shape_pos)[:]
    movement_amnt = next_pos[0]
    next_space_free = next_pos[1]

    #move/place shape if pos is available
    square_num_in_shape = -1
    if next_space_free:
        for square in cur_shape_pos:
            square_num_in_shape += 1
            square_row = square[0]
            square_col = square[1]
            if (0 <= square_row + movement_amnt < num_of_rows): #if new square row pos is on board
                square_changing = board[square_row + movement_amnt][square_col + h_movement] #get square to change
                board[square_row + movement_amnt][square_col + h_movement] = cur_shape_colour #changes square colour to colour of shape
                if is_new_shape == True:
                    is_new_shape = False #has been placed, so not new anymore
                if square_row > -1: #stops from wrapping around list and changing colour of bottom rows.
                    board[square_row][square_col] = empty_square #make old square empty again
                cur_shape_pos[square_num_in_shape] = [square_row + movement_amnt, square_col + h_movement] #store new pos of shape square
            else: #if new square row pos is not on board
                cur_shape_pos[square_num_in_shape] = [square_row + movement_amnt, square_col + h_movement] #store new pos of shape square
    else:
        global down_pressed
        down_pressed = False #reset it
        clear_lines() #check for full lines and clear them
        cur_shape = get_random_shape() #change shape
        rotation_pos = 0 #reset rotation

    if not game_over:
        #Update board
        embed = discord.Embed(description=format_board_as_str(), color=embed_colour)
        h_movement = 0 #reset horizontal movement
        rotate_clockwise = False #reset clockwise rotation
        await msg.edit(embed=embed)
        if not is_new_shape:
            await asyncio.sleep(1) #to keep under api rate limit
        await run_game(msg, cur_shape)
    else:
        desc = 'Score: {} \n Lines: {} \n \n Press ▶ to play again.'.format(points, lines)
        embed = discord.Embed(title='GAME OVER', description=desc, color=embed_colour)
        await msg.edit(embed=embed)
        await msg.remove_reaction("⬅", client.user) #Left
        await msg.remove_reaction("⬇", client.user) #Down
        await msg.remove_reaction("➡", client.user) #Right
        await msg.remove_reaction("🔃", client.user) #Rotate
        await msg.add_reaction("▶") #Play


async def reset_game():
    global down_pressed
    global rotate_clockwise
    global rotation_pos
    global h_movement
    global is_new_shape
    global start_higher
    global game_over
    global points
    global lines
    fill_board(empty_square)
    down_pressed = False
    rotate_clockwise = False
    rotation_pos = 0
    h_movement = 0 #amount to move left or right
    is_new_shape = False
    start_higher = False
    game_over = False
    next_space_free = True
    points = 0
    lines = 0

make_empty_board()

@client.command(aliases = ["tetris","Tetris"])
async def start(ctx): #Starts embed
    await ctx.send("||Credit: https://github.com/willcantcode/Tetris-Discord-Bot||")
    await reset_game()
    embed = discord.Embed(title='Tetris in Discord', description=format_board_as_str(), color=embed_colour)
    embed.add_field(name='How to Play:', value='Use ⬅ ⬇ ➡ to move left, down, and right respectively. \n  \n Use 🔃 to rotate the shape clockwise. \n \n Press ▶ to Play.', inline=False)

    msg = await ctx.send(embed=embed)

    #Add button choices / reactions
    await msg.add_reaction("▶") #Play

    #On new reaction:
    #Update board and board_as_str
    #await msg.edit(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    global h_movement
    global rotation_pos
    if user != client.user:
        msg = reaction.message
        if str(reaction.emoji) == "▶": #Play button pressed
            await reset_game()
            await msg.remove_reaction("❌", client.user) #Remove delete
            embed = discord.Embed(description=format_board_as_str(), color=embed_colour)
            await msg.remove_reaction("▶", user)
            await msg.remove_reaction("▶", client.user)
            await msg.edit(embed=embed)
            await msg.add_reaction("⬅") #Left
            await msg.add_reaction("⬇") #Down
            await msg.add_reaction("➡") #Right
            await msg.add_reaction("🔃") #Rotate
            await msg.add_reaction("❌") #Stop game
            starting_shape = get_random_shape()
            await run_game(msg, starting_shape)

        if str(reaction.emoji) == "⬅": #Left button pressed
            h_movement = -1 #move 1 left
            await msg.remove_reaction("⬅", user)
        if str(reaction.emoji) == "➡": #Right button pressed
            h_movement = 1 #move +1 right
            await msg.remove_reaction("➡", user)
        if str(reaction.emoji) == "⬇": #Down button pressed
            global down_pressed
            down_pressed = True
            await msg.remove_reaction("⬇", user)
        if str(reaction.emoji) == "🔃": #Rotate clockwise button pressed
            global rotate_clockwise
            rotate_clockwise = True
            if rotation_pos < 3:
                rotation_pos += 1
            else:
                rotation_pos = 0 #go back to original pos
            await msg.remove_reaction("🔃", user)
        if str(reaction.emoji) == "❌": #Stop game button pressed
            #In future maybe put score screen here or a message saying stopping.
            await reset_game()
            await msg.delete()
        if str(reaction.emoji) == "🔴":
            await message.edit(content="")


#############################################################################################################################################################################################
#TETRIS######################################################################################################################################################################################
#############################################################################################################################################################################################



#startet client
file_t = open(os.path.join("assets", "Token.txt"))
content_list = file_t.readlines()
file_t.close()

file_t = open(os.path.join("assets", "Token.txt"))
Token = file_t.read()
client.run(Token)
file_t.close()