import streamlit as st

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

def draw_health_bar(health):
    bar = "["
    for _ in range(health):
        bar += "#"
    for _ in range(10 - health):
        bar += " "
    bar += "]"
    return bar

def battle():
    st.title("Battle Begins! A Fierce Monster Approaches...")
    player_hp = 10
    monster_hp = 5

    while player_hp > 0 and monster_hp > 0:
        st.write("A fierce monster stands before you:")
        draw_ascii_monster()
        st.write("Your hero:")
        draw_ascii_hero()

        action = st.selectbox("Choose your action:", options=["Attack", "Defend"])

        if action == "Attack":
            st.write("You attack the monster!")
            monster_hp -= 3
        elif action == "Defend":
            st.write("You defend against the monster's attack!")
            player_hp -= 1

        st.write("Monster HP:", draw_health_bar(monster_hp))
        st.write("Player HP:", draw_health_bar(player_hp))

    if player_hp > 0:
        st.success('Cody Sewell: Battle Won!')
    else:
        st.error('Defeat... The monster was too strong.')

if __name__ == "__main__":
    battle()
