# Ask user for number of lives, energy level and shield level in whole numbers

print("Please enter the number of lives:")
lives = int(input())

print("Please enter the energy level:")
energy = int(input())

print("Please enter the shield strength:")
shield = int(input())

print("Health has been set, please standby...")

print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)