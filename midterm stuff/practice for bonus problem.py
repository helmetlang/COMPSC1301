# write a function called draw_tree
# draw a tree of a certain height

# draw_tree(3) # limit 20
#   ---*--- # row = 0 and needs 3 spaces, 1 star
#   --***-- # row 1, 2 spaces, 3 stars
#   -*****- # row 2,1 space, 5 stars
# "   *   "
# mentioned earlier we were going to write a for loop
number = int(input("Enter the height that you would like for your tree to be: "))

def draw_tree(height):
    # draw a tree of whatever number is inserted
    if height <= 20:
        for row in range(height):



# print height - row * spaces
# print (2*row + 1) + '*'



    else: 
        print("Height has to less than or equal to 20!")


draw_tree(3)
draw_tree(5)