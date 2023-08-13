import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

def draw_ascii_hero():
    st.write("""
      O
     /|\\
     / \\
    """)

def draw_ascii_monster():
    st.write("""
      /\\_ /\\
     /  o o  \\
    ( ==  ^  ==)
     )         (
    /           \\
    |           |
     \\  \\/\\/  /
      -_____-
    """)

def draw_hero(ax, x):
    hero_body = patches.Rectangle((x, 0), 1, 2, facecolor='blue')
    ax.add_patch(hero_body)

def draw_monster(ax, x):
    monster_body = patches.Circle((x, 1), 0.5, facecolor='red')
    ax.add_patch(monster_body)

def battle():
    st.title("Battle Begins! A Fierce Monster Approaches...")
    player_hp = 10
    monster_hp = 5
    hero_x = 1
    monster_x = 8

    fig, ax = plt.subplots(figsize=(8, 4))
    plt.xlim(0, 10)
    plt.ylim(0, 3)
    plt.axis('off')

    while player_hp > 0 and monster_hp > 0:
        draw_ascii_monster()
        draw_ascii_hero()
        action = st.selectbox("Choose your action:", options=["Attack", "Defend"])
        
        if action == "Attack":
            st.write("You attack the monster!")
            monster_hp -= 3
        elif action == "Defend":
            st.write("You defend against the monster's attack!")
            player_hp -= 1

        draw_hero(ax, hero_x)
        draw_monster(ax, monster_x)
        st.pyplot(fig)
        plt.clf()
        ax.clear()
        plt.xlim(0, 10)
        plt.ylim(0, 3)
        plt.axis('off')
        hero_x += 0.1
        monster_x -= 0.1

        st.write(f"Player HP: {player_hp} | Monster HP: {monster_hp}")

    if player_hp > 0:
        st.success('Cody Sewell: Battle Won!')
    else:
        st.error('Defeat... The monster was too strong.')

if __name__ == "__main__":
    battle()
