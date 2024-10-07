team1_name = "Собаки-коды писаки"
team2_name = "Закодированные фисташки"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4


def find_winner(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2:
        return f"Победа команды {team1_name}!"
    elif score_1 < score_2:
        return f"Победа команды {team2_name}!"
    else:
        if team1_time < team2_time:
            return f"Победа команды {team1_name}, они оказались быстрее!"
        elif team1_time > team2_time:
            return f"Победа команды {team2_name}, они оказались быстрее!"
        else:
            return "Ничья!"


challenge_result = find_winner(score_1, score_2, team1_time, team2_time)
print("В команде Собаки-коды писаки участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("Команда Закодированные фисташки решила задач: {} !".format(score_2))
print("Закодированные фисташки решили задачи за {:.1f} с !".format(team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
print(f"Результат битвы: {challenge_result}")
