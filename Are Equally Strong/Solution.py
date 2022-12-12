def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    your_arm_strenght = [yourLeft, yourRight]
    friends_arm_strenght = [friendsLeft, friendsRight]

    return max(your_arm_strenght) == max(friends_arm_strenght) and min(your_arm_strenght) == min(friends_arm_strenght)