def generate_language_line(language, time_spent, percentage):
    lanuage_max_limit = 25
    language = language + (" " * (lanuage_max_limit - len(language)))
    time_max_limit = 20
    time_spent = time_spent + (" " * (time_max_limit - len(time_spent)))
    blocks_total = 25
    black_block = max(int(percentage / 100 * blocks_total), 1)
    block = (black_block * "█") + ((blocks_total - black_block) * "░") + (3 * " ")
    percentage = "{} %".format(percentage)
    return language + time_spent + block + percentage