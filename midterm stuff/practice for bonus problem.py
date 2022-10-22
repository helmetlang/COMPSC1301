# write a function called draw_tree
# draw a tree of a certain height

# draw_tree(3) # limit 20
#   ---*--- # row = 0 and needs 3 spaces, 1 star
#   --***-- # row 1, 2 spaces, 3 stars
#   -*****- # row 2,1 space, 5 stars
# "   *   "
# mentioned earlier we were going to write a for loop
number = int(input("Enter the height that you would like for your tree to be: "))
# FIXME: symbol = int(input"Enter a symbol for your tree: ")

def draw_tree(height, symbol='*'):
    # draw a tree of whatever number is inserted, up to 20 in height
    if height <= 20:
        for rows in range(height):
            spaces = height - rows
            stars = (2 * rows + 1) # odd numbers
            print(' ' * spaces, end='')
            print(symbol * stars)
    else: 
        print("Height has to less than or equal to 20!")

print(draw_tree(number))

# NOTE: print(''*(height-row))
# print height - row * spaces
# print (2*row + 1) + '*'
# FIXME: make sure to remove comments late
# draw_tree(3)
# draw_tree(5)