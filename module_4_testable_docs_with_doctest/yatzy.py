def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category.

    Args:
        dice List[int]: A list of dice rolls.

    Returns:
        int: The score attributed to the dice rolls.
    """
    if dice == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0
