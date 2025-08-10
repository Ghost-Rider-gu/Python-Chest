previewText = (f"Let's play a simple game.\n"
               f"I'm gonna ask you some questions and we'll see what we get in the end.\n")
print(previewText)

adjectives = []
for _ in range(0, 28):
    adjective = input("What's your adjective?: ")
    adjectives.append(adjective)

madLibs = (f"The {adjectives[0]}, {adjectives[1]} oak tree stood {adjectives[2]} on the windswept, {adjectives[3]} hilltop.\n"
           f"Its {adjectives[4]}, {adjectives[5]} bark was a testament to countless {adjectives[6]}, {adjectives[7]} winters.\n"
           f"{adjectives[8]}, {adjectives[9]} branches reached out like {adjectives[10]}, {adjectives[11]} fingers, clawing at the {adjectives[12]}, {adjectives[13]} sky.\n"
           f"Beneath the {adjectives[14]}, {adjectives[15]} tree, a {adjectives[16]}, {adjectives[17]} cottage huddled, its crooked, {adjectives[18]} roof threatening to collapse\n"
           f"under the weight of the {adjectives[19]}, {adjectives[20]} snow.\n"
           f"An {adjectives[21]}, {adjectives[22]} woman sat in a comfortable, {adjectives[23]} armchair, her {adjectives[24]}, {adjectives[25]} eyes gazing at the {adjectives[26]}, {adjectives[27]} flames.")

if __name__ == '__main__':
    print(madLibs)
