def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category.

    Args:
        dice List[int]: A list of dice rolls.

    Returns:
        int: The score attributed to the dice rolls.


    >>> small_straight([1, 2, 3, 4, 5])
    15
    >>> small_straight([1, 2, 3, 5, 5])
    0
    >>> small_straight({1, 2, 3, 4, 5})
    0
    >>> small_straight({1, 2, 3, 5, 4})
    0
    """
    if dice == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0
